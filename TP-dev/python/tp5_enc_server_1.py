def rec_msg(client_socket):
    # Lit l'en-tête pour définir la taille du message
    header = client_socket.recv(4)
    if not header:
        return None

    # Lit la valeur de la taille du message depuis l'en-tête
    msg_length = int.from_bytes(header, byteorder='big')

    print(f"Reading {msg_length} bytes")

    # Lit les octets suivants pour reconstruire le message
    chunks = []
    bytes_received = 0

    while bytes_received < msg_length:
        # Lit 1024 octets ou moins à la fois
        chunk = client_socket.recv(min(msg_length - bytes_received, 1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received')

        # Ajoute le morceau à la liste
        chunks.append(chunk)

        # Ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # Assemble la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')

    # Vérifie que le message se termine bien par la séquence de fin
    if not message_received.endswith('<clafin>'):
        raise RuntimeError(f'Invalid message format. Received: {message_received}')

    # Retourne le message sans la séquence de fin
    return message_received[:-7]
