'''

echo_client.py

Client side socket handler. Sends string to the server and prints the return.

Dave Fugelso January, 2015

'''

import socket
import sys
                   

def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print >>log_buffer, 'connecting to {0} port {1}'.format(*server_address)
    try:
        sock.connect(server_address)
    except Exception, e:
        print 'Failed  to connect to: %s:%d. Exception: %s' % (address, port, `e`)


    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print >>log_buffer, 'sending "{0}"'.format(msg)
        if not sock.sendall(msg):
            #get return message
            msglen = len(msg)
            returnmsglen = 0
            while True:
                chunk = sock.recv (16)
                if not chunk:
                    break
                print >>log_buffer, 'received "{0}"'.format(chunk) 
                returnmsglen += len(chunk)
                if  len(chunk) < 16 or returnmsglen == msglen:
                    break


    finally:
        print >>log_buffer, 'closing socket'
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)

