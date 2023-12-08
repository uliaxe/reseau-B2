import asyncio

# Variable globale pour stocker les informations des clients
CLIENTS = {}

async def handle_client(reader, writer):
    # Obtenez les informations sur le client
    client_addr = writer.get_extra_info('peername')

    # Vérifie si le client est déjà connecté
    if client_addr in CLIENTS:
        print(f"Client déjà connecté: {client_addr}")
        return

    print(f"Client connecté: {client_addr}")

    # Stocke les informations du client dans CLIENTS
    CLIENTS[client_addr] = {"r": reader, "w": writer}

    try:
        # Attendre les messages du client
        await receive_messages(client_addr)
    finally:
        # Retirez le client de CLIENTS lorsqu'il se déconnecte
        del CLIENTS[client_addr]
        print(f"Client déconnecté: {client_addr}")

async def receive_messages(sender_addr):
    # Obtenez le reader du client
    reader = CLIENTS[sender_addr]["r"]

    while True:
        # Recevez le message du client
        data = await reader.read(1024)
        if not data:
            break

        message = data.decode()

        # Diffuser le message à tous les clients
        await broadcast_message(sender_addr, message)

async def broadcast_message(sender_addr, message):
    # Formatage du message pour la diffusion
    sender_ip, sender_port = sender_addr
    broadcast_msg = f"{sender_ip}:{sender_port} a dit : {message}"

    # Envoi du message à tous les clients sauf à l'expéditeur
    for addr, client_info in CLIENTS.items():
        if addr != sender_addr:
            writer = client_info["w"]
            writer.write(broadcast_msg.encode())
            await writer.drain()

async def main():
    # Créer le serveur
    server = await asyncio.start_server(
        handle_client, '10.1.2.20', 13337)

    # Obtenir les informations d'adresse du serveur
    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        # Attendre indéfiniment que le serveur soit fermé
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
