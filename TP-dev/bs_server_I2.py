import socket 

host =''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

s.listen(5)
print(f"Serveur en écoute sur le port {host}{port}")

while true :
    
    client_socket, client_address = s.accept()
    print(f"Un client vient de se connecter et son IP c'est {client_address[0]}.")
    
    message = client_socket.recv(1024).decode()
    print(f"Message du client : {message}")
    
    if "meo" in message.lower():
        response = "Meo à toi confrère !"
    elif "waf" in message.lower():
        response = "ptdr t ki"
    else:
        response = "Mes respects humble humain"
        
    client_socket.sendall(response.encode())
    
    client_socket.close()
    
