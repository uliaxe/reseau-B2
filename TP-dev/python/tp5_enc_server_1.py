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
        
      
        # Ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # Assemble la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')

    # Vérifie que le message se termine bien par la séquence de fin
    if not message_received.endswith('<clafin>'):
        raise RuntimeError('Invalid message format')

    # Retourne le message sans la séquence de fin
    return message_received[:-7]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.1.2.11', 9999))
sock.listen()
client, client_addr = sock.accept()

while True:
    try:
        # Attend la réception des messages du client
        received_message = rec_msg(client)
        if received_message is None:
            break

        print(f"Received from client: {received_message}")

    except RuntimeError as e:
        print(f"Error: {e}")
        break

client.close()
sock.close() 
    