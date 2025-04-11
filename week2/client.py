import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

message = "Hello, From the Client Side!"
client_socket.send(message.encode('utf-8'))

response = client_socket.recv(1024).decode('utf-8')
print(f"Server response: {response}")

client_socket.close()