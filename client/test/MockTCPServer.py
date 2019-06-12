import socket
import time
import unittest
from client_test_config import CLIENT_CONFIG

class MockTCPServer:
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((CLIENT_CONFIG['HOST'], CLIENT_CONFIG['PORT']))
        server_socket.listen(5)
        
        conn, addr = server_socket.accept()
        data = conn.recv(16)
        if not data:
            conn.sendall(b'')
        conn.sendall(data)
        server_socket.close()
        


