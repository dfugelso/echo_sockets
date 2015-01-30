'''
Server side socket handler. Echos back all input back to the client. Handles multiple clients using select.

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
        self.portNUmber = portNumber
        self.bytesReceived = 0
        self.bytesSent = 0
        
    def startServer (self):
        '''
        Bind and accept connections.
        '''
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
        server_socket.bind(('127.0.0.1', 50000))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        self.handleConnection(conn, addr)
        
        
    def handlConnection (conn, addr):
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
    s = server()
    s.startServer()
   
 