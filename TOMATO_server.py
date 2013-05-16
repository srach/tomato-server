import socket
import sys

CHUNK_SIZE = 4096

def run_server(port):
    '''
    socket.socket([family[,type[,proto]]]) creates a socket using the given:
    address family: AF_INET (default), AF_INET6, or AF_UNIX
    socket type: SOCK_STREAM (default), SOCK_DGRAM or one of the other SOCK_ constants
    protocol number: is usually zero and may be omitted in that case
    '''
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''
    soc.bind(address) binds the socket to the address.
    The format of the address param depends on the address family used.
    AF_INET accepts addresses in the form (host, port)
    where host is a string representing either a hostname in internet domain notation 
    like 'daring.cwi.nl' or an IPv4 address like '100.50.200.5' and port is an int.
    '''
    soc.bind(('localhost', port))
    '''
    socket.listen(backlog) listens for client connections made to the socket.
    `backlog` specifies the number of queued connections (max=5)
    '''
    soc.listen(2)
    print "Server listening on port {portnum}".format(portnum = port)
    try:
        '''
        returns (conn, address)
        conn: a new socket object that can be used to send and receive data on the connection
        address: the address bound to the socket on the other end of the connection
        '''
        connection, client_addr = soc.accept()
        print "Connected to {ip_address} at {portnum}".format(ip_address=client_addr[0],portnum=client_addr[1])
        '''
        socket.recv() receives data from the socket and returns string representing data received.
        `bufsize` specifies the maximum amount of data to be received at once.
        The value of `bufsize` should be a small power of 2, such as 4096.
        '''
        while True:
            data = connection.recv(CHUNK_SIZE)
            if not data: break
            connection.send(data + " TOMATO")
        # close client socket
        connection.close()
    except KeyboardInterrupt:
        print "Got Ctrl-C. Exiting......."
        # close the socket that the listening server is bound to
        soc.close()
    
    
if __name__ == "__main__":
    run_server(5000)