import os,sys
import threading
import socketserver
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import variable
from sockets import tcpServer

def startServer():
    s = socketserver.ThreadingTCPServer(variable.ip_port,tcpServer.Myserver)
    s.serve_forever()

if __name__ == '__main__':
    serverThread = threading.Thread(target=startServer)
    serverThread.start()
