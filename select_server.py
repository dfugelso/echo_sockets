'''

select_server.py

This builds on echo_server.py to add select processing to handle multiple clients.

I followed the example from http://pymotw.com/2/select/ to do this.

Dave Fugelso January, 2015

'''

import select
import socket
import sys
import Queue

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
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
        self.server_socket.bind((self.ip, self.portNumber))
        
    def startServer (self):
        '''
        Bind and accept connections.
        '''

        try:
            self.server_socket.listen(1)
            
            # Create server, outputs, and queues for input into select
            inputs = [ self.server_socket ]
            outputs = [ ]
            message_queues = {}

            # Loop and on inputs not empty and block on select callable
            while inputs:
                #block on incoming
                readable, writable, exceptional = select.select(inputs, outputs, inputs)
                
                # Check if there are readables
                for s in readable:
                    # Check for new connection
                    if s is self.server_socket:
                        conn, addr =  s.accept()
                        print 'new connection from', addr
                        conn.setblocking(0)
                        #Add connection to inputs list and block on select
                        inputs.append(conn)
                        message_queues[conn] = Queue.Queue()
                    else:
                        str = s.recv(1024)
                        if str:
                            # A readable client socket has data
                            print 'received : {}'.format(str)
                            #I tested writing the echo write here... works fine as well
                            message_queues[s].put(str)
                            if s not in outputs:
                                outputs.append(s)  
                        else:
                            print 'A client socket closed.'
                            if s in outputs:
                                outputs.remove(s)
                            inputs.remove(s)
                            s.close()
                            del message_queues[s]
                
                # Handle the writable list from select                
                for s in writable:
                    try:
                        msg = message_queues[s].get_nowait()
                    except Queue.Empty:
                        outputs.remove(s)
                    else:
                        print 'Sending: {}'.format(msg)
                        s.sendall(msg)            
                 
                #And the exceptions
                for s in exceptional:
                    print 'Close out socket.'
                    inputs.remove(s)
                    if s in outputs:
                        outputs.remove(s)
                    s.close()
                    del message_queues[s]
            
           
        except KeyboardInterrupt:
            print "Done. Server closing."
            self.server_socket.close()       

         
if __name__ == "__main__":
    s = server('127.0.0.1', 50000)
    s.startServer()


   
 