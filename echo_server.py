'''

echo_server.py

Server side socket handler. Echoes back all input back to the client. Handles multiple clients using select.

Dave Fugelso January, 2015

'''

import socket
import sys


def server(log_buffer=sys.stderr):
    '''
    Listen on a port number and echo back incoming messages.
    '''
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
    # log that we are building a server
    print >>log_buffer, "making a server on {0}:{1}".format(*address)

    # Bind socket of local host and port number
    sock.bind(address)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print >>log_buffer, 'waiting for a connection'

            # Listen for connection
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
                
    # Note: This doesn't work on Windows 7/ Tested on Linux and works like a champ
    except KeyboardInterrupt:
        print >>log_buffer, 'Done with server. Close server socket and exit.'
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)        

   
 