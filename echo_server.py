'''

echo_server.py

Server side socket handler. Echoes back all input back to the client. Handles multiple clients using select.

Dave Fugelso January, 2015

'''

import socket

class server (object):
    ''' 
    Server class to store data and do unit testing.
    '''
    def __init__ (self, ip, portNumber):
        '''
        Allow configurable IP address and port number.
        '''
        self.ip = ip
        self.portNumber = portNumber
        self.bytesReceived = 0
        self.bytesSent = 0
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
        self.server_socket.bind((self.ip, self.portNumber))
        
    def startServer (self):
        '''
        Bind and accept connections.
        '''

        self.server_socket.listen(1)
        conn, addr = self.server_socket.accept()
        self.handleConnection(conn, addr)
        
        
    def handleConnection (self, conn, addr):
        while True:
            str = conn.recv(1024) 
            if not str:
                break
            self.bytesReceived += len(str)
            sent = conn.senall(str)
            if sent == 0:
                break
            self.bytesSent += sent
        print 'Connection closed'
        print 'Bytes received: {}'.format(self.bytesReceived)
        print 'Bytes sent: {}'.format(self.bytesSent)
         
        
if __name__ == "__main__":
    s = server('127.0.0.1', 50000)
    s.startServer()
   
 