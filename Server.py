import socket
import sys

def start_server(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket:
            Socket.bind((host, port))
            Socket.listen()#will wait for tyhe message from the client
            print(f"Server listening on {host}:{port}")
            # Accept a connection from a client (Intialising the parameters)
            #returns a new Socket object #Return Value: When a client connects, Socket.accept() returns a tuple containing two values:
            #clientConnectionSocket  Socket object)--- address (Ip address and portnumber)
            clientConnectionSocket, address = Socket.accept()
        with clientConnectionSocket:
                print(f"Connected by {address}")
                while True:
                    data = clientConnectionSocket.recv(1024)
                    if data is None:
                        break
                    print(f"Received: {data.decode()}")
                    clientConnectionSocket.sendall(data)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()

