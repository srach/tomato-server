import socket

CHUNK_SIZE = 4096

def echo(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", port))
    print "Client: connected"
    soc.sendall("Client message")
    # make a variable for incoming data
    data = soc.recv(CHUNK_SIZE)
    soc.close()
    return data
    
if __name__ == "__main__":
    print "Received from server: {msg}".format(msg=echo(5000))