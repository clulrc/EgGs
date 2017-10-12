import socket
import sys

class SocketClient:
    def __init__(self):
        self.sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 12315
    def connectServer(self):


        self.sc.connect((self.host,self.port))

        msg = self.sc.recv(1024)

        self.sc.close()

        print (msg.decode('utf-8'))