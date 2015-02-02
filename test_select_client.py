'''
client.py

This client accetps input and goes until user quits. used to test select server.

Dave Fugelso January, 2015
'''

import socket

class client (object):
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
        self.connected = False
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
        self.client_socket.connect((ip, portNumber))
        
    @property
    def Connected (self):
        return self.connected
        
    def send (self, msg):
        '''
        Send a message.
        '''
        sent = self.client_socket.sendall(msg)
        if sent == 0:
            self.connected= False
        self.bytesSent += sent
        
        
    def read(self):
        msg = self.client_socket.rec()
        if msg == '':
            self.connected = False
        self.bytesRecieved = len (msg)
        return msg
        
        
        
         
        
if __name__ == "__main__":
    c = client('127.0.0.1', 50000)

        
    while True:
        if not c.Connected:
            print 'No server connection'
            break
        input = raw_input ('Enter a message to send: ')
        if input == 'Q' or input == 'Quit':
            break
        c.send(input)
        print c.read()
   