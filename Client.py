import socket

def start_client(host, port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socket:
        # Connect to the server at the specified host and port
        Socket.connect((host, port))
        print("Connected to the server. Type 'exit' to quit.")
        while True:
            # Prompt the user for a message
            message = input("Enter message: ")
            if message.lower() == 'exit':  # Exit condition / also to make sure that any way of typing exit is recognised
                print("Exiting client.")
                break
            # Send the message to the server
            Socket.sendall(message.encode())
            # Receive the response from the server (up to 1024 bytes)
            data = Socket.recv(1024)
            # Print the received response
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    server_ip = input("Enter the server IP address: ")  # Prompt the user to enter the server'sockt IP address
    start_client(server_ip)  # Start the client with the specified server IP address