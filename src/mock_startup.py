import machine
import time
import socket
import network
from src.configuration import USERS, ADMINS
from src.persistence.MicroDatabaseAccess import MicroDatabaseAccess

HOST = '192.168.0.4'
PORT = 8888
LOGGED_USER = None
databaseAccess = MicroDatabaseAccess()


def start():
    global LOGGED_USER
    ap_if = setup_ap()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    pin = machine.Pin(2, machine.Pin.OUT)
    pin.off()

    while True:
        print(ap_if.isconnected())
        LOGGED_USER = None
        time.sleep(1)
        if ap_if.isconnected():
            try:
                conn, addr = server_socket.accept()
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        continue
                    if LOGGED_USER is not None:
                        response = analyze_message(data.decode())
                    else:
                        response = identify(data.decode())
                    conn.sendall(response.encode())
            except Exception as e:
                print(str(e))
                continue
                time.sleep(1)


def setup_ap():
    ap_if = network.WLAN(network.AP_IF)

    ap_if.config(essid="DOOR 1")
    print(ap_if.config('essid'))

    ap_if.config(authmode=network.AUTH_WPA_WPA2_PSK)
    ap_if.config(password='123456789')
    ap_if.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    print(ap_if.ifconfig())

    ap_if.active(True)

    print("AP state = " + str(ap_if.active()))

    return ap_if


def analyze_message(message):
    global LOGGED_USER,databaseAccess
    temp = message.split(';')
    command = temp[0]
    if command == "OPEN":
        databaseAccess.add_log("Door opened by user: " + LOGGED_USER.username,"INFO")
        return "DOOR OPENED"
        
    elif command == "ADD_USER" and len(temp) > 1:
        if LOGGED_USER.is_admin:
            databaseAccess.add_user(temp[1])
            databaseAccess.add_log("Added user: " + str(temp[1]) + " by: " + LOGGED_USER.username)
            return "USER ADDED"
        else:
            return "ACCESS DENIED"

    elif command == "REMOVE_USER" and len(temp) > 1:
        if LOGGED_USER.is_admin:
            databaseAccess.remove_user_by_username(temp[1])
            databaseAccess.add_log("Removed user: " + str(temp[1]) + " by: " + LOGGED_USER.username)
            return "USER REMOVED"
        else:
            return "ACCESS DENIED"

    elif command == "GET_ALL_LOGS":
        if LOGGED_USER.is_admin:
            string_to_send = ""
            logs = databaseAccess.get_all_logs()
            print(str(logs))
            for log in logs:
                string_to_send += str(log.message) + " " + str(log.level) + " " + str(log.source) + " " + str(log.timestamp) + "\n"
                
            databaseAccess.add_log("All logs get by: " + LOGGED_USER.username)
            return string_to_send
        else:
            return "ACCESS DENIED"
    else:
        return "COMMAND NOT FOUND : " + command


def identify(user):
    global LOGGED_USER,databaseAccess
    LOGGED_USER = databaseAccess.get_user_by_username(user)
    if LOGGED_USER != None:
        return "SUCCESS"
    else:
        return "FAILED"
