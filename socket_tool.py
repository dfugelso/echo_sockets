'''
   Dave Fugelso, 2015
   Python Certification Session 4 Homework

  * Write a python function that lists the services provided by a given range of
  ports.

  * accept the lower and upper bounds as arguments
  * provide sensible defaults
  * Ensure that it only accepts valid port numbers (0-65535)


'''

import socket

def get_service_info(lowest_port, highest_port):
    '''
    Loop through input range of ports and print out it's service.
    '''
    #Check for valid range
    if lowest_port < 0 or lowest_port > 65535 or highest_port < 0 or highest_port > 65535:
        raise ValueError('Input out of range. Must be between 0 and 65535')
    if lowest_port > highest_port:
        raise ValueError('High range must be higher than lowest port')
    for portnumber in range(lowest_port, highest_port+1):
        print '{0:5} : '.format(portnumber),
        try:
            service = socket.getservbyport(portnumber)
            print service
        except:
            print 'None found'


def run_test():
    '''
    Get input on port range and fire off get_service Info.
    '''
    lowest_port = -1
    while lowest_port < 0 or lowest_port > 65535:
        port = raw_input ('Enter lower port range (0-65535): ')
        try:
            lowest_port = int(port)
        except:
            print 'bad input or out of range'
            lowest_port = -1
        
    highest_port = 65536
    prompt = 'Enter high port range ({}-65535): '.format(lowest_port)
    while highest_port < lowest_port or highest_port > 65535:
        port = raw_input (prompt)
        try:
            highest_port = int(port)
        except:
            print 'bad input or out of range'
            highest_port = 65536
    get_service_info (lowest_port, highest_port)   
            

            

        
if __name__ == "__main__":

    run_test()
    try:
        get_service_info (-1, 65535)    
    except ValueError, e:
        print e
    try:
        get_service_info (0, 65536)    
    except ValueError, e:
        print e
    try:
        get_service_info (10, 0)
    except ValueError, e:
        print e
 