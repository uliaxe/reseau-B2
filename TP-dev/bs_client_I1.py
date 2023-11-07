import socket 

host='10.1.2.15'
port=13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b"Meooooo !")

data = s.recv(1024)

s.close

print('Received', repr(data))