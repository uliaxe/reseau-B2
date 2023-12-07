import socket

server_address = ('10.1.2.20', 13337)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

client_socket.sendall(b"Hello")

response = client_socket.recv(1024)

print(response.decode())

client_socket.close()
