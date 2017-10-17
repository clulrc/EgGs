import threading
from tbmode.socketpac.SocketServer import SocketServer
from tbmode.socketpac.SocketClient import SocketClient

ss = SocketServer()
t = threading.Thread(target=ss.startServer)
t.start()
sc = SocketClient()

sc.connectServer()
sc.communicat()