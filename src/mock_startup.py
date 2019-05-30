import machine
import time
import socket
import network

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
        if(ap_if.isconnected()):
            try:
                conn, addr = server_socket.accept()
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode())
                    conn.sendall(b'Door opened.')
                    pin.on()
                    time.sleep(2)
                    pin.off()
                    break
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
