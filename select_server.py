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
        print "Done. Server closing."
        
        
    def handleConnection (self, conn, addr):
        while True:
            str = conn.recv(1024) 
            if not str:
                break
            self.bytesReceived += len(str)
            if conn.sendall(str):
                break
            self.bytesSent += len(str)
        print 'Connection closed'
        print 'Bytes received: {}'.format(self.bytesReceived)
        print 'Bytes sent: {}'.format(self.bytesSent)
         
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # To do miltiple clients w/o threads set tonon blocking
    sock.setblocking(0)
    
    # log that we are building a server
    print >>log_buffer, "making a server on {0}:{1}".format(*address)

    # Bind
    sock.bind(address)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print >>log_buffer, 'waiting for a connection'

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            sock.listen(1)
            conn, addr = sock.accept()
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    data = conn.recv(16) 
                    if not data:
                        break

                    print >>log_buffer, 'received "{0}"'.format(data)

                    if conn.sendall(data):
                        break

            finally:
                print >>log_buffer, 'Done with this client. Close client socket and exit.'

                conn.close()
                

    except KeyboardInterrupt:
        print >>log_buffer, 'Done with server. Close server socket and exit.'
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)        

   
 