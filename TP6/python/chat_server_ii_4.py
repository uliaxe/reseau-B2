import asyncio

CLIENTS = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')  # Adresse du client (IP, port)

    # Vérifier si le client est déjà dans la liste
    if addr not in CLIENTS:
        CLIENTS[addr] = {}
        CLIENTS[addr]["r"] = reader
        CLIENTS[addr]["w"] = writer

        print(f"Nouveau client connecté: {addr}")

    else:
        print(f"Client déjà connecté: {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Message reçu de {addr}: {message}")

            # Envoyer le message à tous les clients
            for client_addr, client_data in CLIENTS.items():
                if client_addr != addr:
                    ip, port = client_addr
                    response = f"{addr[0]}:{addr[1]} a dit : {message}"
                    client_data["w"].write(response.encode())
                    await client_data["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:
        # Le client a été déconnecté
        del CLIENTS[addr]
        print(f"Client déconnecté: {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '10.1.2.20', 13337)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexions sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
