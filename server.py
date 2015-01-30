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
        while conn.