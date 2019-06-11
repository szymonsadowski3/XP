import machine
import time
import socket
import network
from src.configuration import USERS,ADMINS

HOST = '192.168.0.4'
PORT = 8888


def start():
    ap_if = setupAP()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    pin = machine.Pin(2, machine.Pin.OUT)
    pin.off()

    while True:
        print(ap_if.isconnected())
        time.sleep(1)
        if(ap_if.isconnected()):
            try:
                conn, addr = server_socket.accept()
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        continue
                    response = analyzeMessage(data.decode())
                    conn.sendall(response.encode())
            except Exception as e:
                print(str(e))
                continue
                time.sleep(1)


def setupAP():
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

def analyzeMessage(message):
    temp = message.split(';')
    command = temp[0]
    if(command == "OPEN"):
        if(int(temp[1]) in (USERS or ADMINS)):
            return("DOOR OPENED")
        else:
            return("ACCESS DENIED")

    elif(command == "ADD_USER"):
        if(int(temp[1]) in ADMINS and int(temp[2]) not in USERS):
            USERS.append(int(temp[2]))
            return("USER ADDED")
        else:
            return("ACCESS DENIED OR USER ALREADY IN DATABASE")

    elif(command == "REMOVE_USER"):
        if(int(temp[1]) in ADMINS and int(temp[2]) in USERS):
            USERS.remove(int(temp[2]))
            return("USER REMOVED")
        else:
            return("ACCESS DENIED OR USER DONT EXISTS IN DATABASE")

    else:
        return("COMMAND NOT FOUND : " + command)


