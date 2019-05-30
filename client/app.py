import time
import socket
import pywifi
from pywifi import const

HOST = '192.168.0.4'  # The server's hostname or IP address
PORT = 8888    # The port used by the server

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()

iface.scan()
time.sleep(5)

print(iface.scan_results())
wifis = iface.scan_results()
for wifi in wifis:
    if("DOOR" in wifi.ssid):
        profile = pywifi.Profile()
        profile.ssid = wifi.ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = '123456789'

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)      
        time.sleep(5)
        if(iface.status() == const.IFACE_CONNECTED):
            print("Connected to " + wifi.ssid) 
            try:
                client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client_socket.connect((HOST,PORT))
                client_socket.sendall(b'OPEN THE DOOR!')

                data = client_socket.recv(16)
                print(data.decode())

            except Exception as e:
                print(e)
            iface.disconnect()



        

