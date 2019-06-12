import unittest
import threading
import socket
from client_test_config import CLIENT_CONFIG
from MockTCPServer import MockTCPServer

class TestTCPClient(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTCPClient, self).__init__(*args, **kwargs)
        self.tcp_client = None

    def setUp(self):
        self.tcp_client = MockTCPServer()

    def testReturnValue(self):
        threading.Thread(target=self.tcp_client.run).start()
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((CLIENT_CONFIG['HOST'], CLIENT_CONFIG['PORT']))
        client_socket.sendall(b'OPEN')

        data = client_socket.recv(16)
        client_socket.close()

        self.assertEqual("OPEN",data.decode())



