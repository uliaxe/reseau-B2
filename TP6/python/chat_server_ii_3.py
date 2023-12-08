import asyncio

async def handle_client(reader, writer):
    # Obtenez les informations sur le client
    client_addr = writer.get_extra_info('peername')
    print(f"Client connecté: {client_addr}")

    while True:
        # Recevez le message du client
        data = await reader.read(1024)
        if not data:
            break

        message = data.decode()
        print(f"Message reçu de {client_addr[0]}:{client_addr[1]} : {message}")

        # Envoyer un accusé de réception au client
        ack_message = "Message reçu par le serveur"
        writer.write(ack_message.encode())
        await writer.drain()

    # Fermez la connexion
    print(f"Client déconnecté: {client_addr}")
    writer.close()

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
