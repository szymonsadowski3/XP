import machine
import time
import socket
import network
import ujson

from src.commands import get_command
from src.persistence.MicroDatabaseAccess import MicroDatabaseAccess

HOST = '192.168.0.4'
PORT = 8888
LOGGED_USER = None
PASSWORD = '123456789'
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
                while conn:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if LOGGED_USER is not None:
                        print("Anlizing message")
                        response = analyze_message(data.decode())
                    else:
                        print("Trying to log in...")
                        response = identify(data.decode())
                    conn.sendall(response.encode())
            except Exception as e:
                print(str(e))
                continue


def setup_ap():
    ap_if = network.WLAN(network.AP_IF)

    ap_if.config(essid=readConfig("SSID"))
    print(ap_if.config('essid'))

    ap_if.config(authmode=network.AUTH_WPA_WPA2_PSK)
    ap_if.config(password=readConfig("PASSWORD"))
    ap_if.ifconfig((readConfig("IP"), '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    print(ap_if.ifconfig())

    ap_if.active(True)

    print("AP state = " + str(ap_if.active()))

    return ap_if

def readConfig(key):
    f = open('src/configuration.json','r')
    json_data = ujson.load(f)
    f.close()
    return json_data[key]



def changePassword(newPass):
    f = open('src/configuration.json','r')
    json_data = ujson.load(f)
    f.close()
    f = open('src/configuration.json','w')
    json_data['PASSWORD'] = newPass
    ujson.dump(json_data,f)
    f.close()

def changeConfig(key,value):
    f = open('src/configuration.json','r')
    json_data = ujson.load(f)
    f.close()
    
    if key in json_data:
        json_data[key] = value
        f = open('src/configuration.json','w')
        ujson.dump(json_data,f)
        f.close()
        return "CONFIG " + key + " CHANGED"
    else:
        return "CONFIG " + key + " DOES NOT EXIST"

def showConfig():
    f = open('src/configuration.json','r')
    json_data = ujson.load(f)
    f.close()
    return str(json_data)

def analyze_message(message):
    global LOGGED_USER,databaseAccess
    command_arguments = message.split(';')
    command = command_arguments[0]

    args = [LOGGED_USER, databaseAccess, command_arguments, readConfig, changePassword, showConfig]

    return get_command(command, *args).execute()

def identify(user):
    global LOGGED_USER,databaseAccess
    LOGGED_USER = databaseAccess.get_user_by_username(user)
    if LOGGED_USER != None:
        print("SUCCESS")
        return "SUCCESS"
    else:
        print("FAILED")
        return "FAILED"
