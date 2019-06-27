import time
import socket
import pywifi
import getpass
from pywifi import const

from client_config import CLIENT_CONFIG


wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[CLIENT_CONFIG['INTERFACE_NUMBER']]

iface.disconnect()

iface.scan()
time.sleep(CLIENT_CONFIG['DELAY_AFTER_SCAN'])

print(iface.scan_results())
wifis = iface.scan_results()
for wifi in wifis:
    if "DOOR" in wifi.ssid:
        profile = pywifi.Profile()
        profile.ssid = wifi.ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = CLIENT_CONFIG['PROFILE_KEY']

        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)
        time.sleep(CLIENT_CONFIG['DELAY_AFTER_CONNECT'])

        if iface.status() == const.IFACE_CONNECTED:
            print("Connected to " + wifi.ssid)
            try:
                client_socket = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(
                    (CLIENT_CONFIG['HOST'], CLIENT_CONFIG['PORT']))
                command = 1
                user_logged = False
                while True:
                    if user_logged:
                        print("Write command:")
                        command = input()
                        if command == "exit":
                            break
                        client_socket.sendall(command.encode())
                        data = client_socket.recv(1024)
                        print("Response: " + data.decode())
                    else:
                        print("User: ")
                        username = input()
                        if username == "exit":
                            break
                        client_socket.sendall(username.encode())
                        data = client_socket.recv(1024)
                        if data.decode() == "SUCCESS":
                            user_logged = True
                        print("Response: " + data.decode())
            except Exception as e:
                print(e)
            iface.disconnect()
