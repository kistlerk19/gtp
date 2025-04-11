import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(5)

print("Server listening on port 8000...")

while True:
    # Accept connections
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    # Receive data
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {data}")

    # Send response
    response = "Message received!"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()