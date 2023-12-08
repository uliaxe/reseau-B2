import asyncio

async def handle_client(reader, writer):
    # Obtenez les informations sur le client
    client_addr = writer.get_extra_info('peername')
    print(f"Client connecté: {client_addr}")

    # Recevez le message du client
    data = await reader.read(1024)
    message = data.decode()

    # Affiche le message du client
    print(f"Message du client ({client_addr}): {message}")

    # Envoyer un message de salutation au client
    response = f"Hello {client_addr[0]}:{client_addr[1]}"
    writer.write(response.encode())
    await writer.drain()

    # Fermez la connexion
    writer.close()

async def main():
    # Créer le serveur
    server = await asyncio.start_server(
        handle_client, '10.1.2.20', 133337)

    # Obtenir les informations d'adresse du serveur
    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        # Attendre indéfiniment que le serveur soit fermé
        await server.serve_forever()

# Exécute le serveur
asyncio.run(main())
