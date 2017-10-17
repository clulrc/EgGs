#!/usr/bin/python3

import socket
import sys

class SocketServer:
    def __init__(self):
        #创建实例
        self.serversocket = socket.socket(
            socket.AF_INET,socket.SOCK_STREAM
        )
        self.host = socket.gethostname()
        self.port = 12315

        #AF_INET模式下，bind绑定地址信息为元祖形式
        self.serversocket.bind((self.host,self.port))
        self.serversocket.listen(5)
    def startServer(self):
        while True:
                clientsocket,addr = self.serversocket.accept()

                print("连接地址: %s"% str(addr))

                msg='welcom to %s\r\n' % str(self.host)

                clientsocket.send(msg.encode('utf-8'))

                clientsocket.close()