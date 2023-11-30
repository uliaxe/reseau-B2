import socket

def rec_msg (client_socket):
    #lit l'en tete pour definir la taille du message
    header = client_socket.recv(4)
    if not header:
        return None
    
    #lit la valeur de la taille message depuis l'en tete
    msg_length = int.from_bytes(header, byteorder='big')
    
    print(f"Reading {msg_length} bytes")
    
    #lit les octets suivants pour reconstruire le message
    
    chunks = []
    bytes_recd = 0
    
    while bytes_recd < msg_length:
        #lit 1024 octets ou moins à la fois
        chunk = client_socket.recv(min(msg_length - bytes_recd, 1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received')
        
        #ajouter le morceau à la liste
        chunks.append(chunk)
        
        #ajoute le morceau à la liste
        bytes_recd += len(chunk)
        
        #assemble    
    