import asyncio

# Déclaration du dictionnaire global
global CLIENTS
CLIENTS = {}

async def handle_client(reader, writer):
    # Récupération de l'adresse IP et du port du client
    addr = writer.get_extra_info('peername')

    # Vérification si le client est déjà connecté
    if addr in CLIENTS:
        print(f"Client {addr} is already connected.")
        return

    # Stockage des informations du client dans le dictionnaire
    CLIENTS[addr] = {"r": reader, "w": writer}
    print(f"Client {addr} connected.")

    try:
        while True:
            # Attente de la réception des données du client
            data = await reader.read(100)
            message = data.decode()

            # Vérification si le client a fermé la connexion
            if not data:
                break

            print(f"Received message from {addr}: {message}")

            # Envoi du message à tous les clients
            await broadcast_message(addr, message)

    except asyncio.CancelledError:
        pass
    finally:
        # Suppression des informations du client lorsqu'il se déconnecte
        del CLIENTS[addr]
        print(f"Client {addr} disconnected.")
        writer.close()
        await writer.wait_closed()

async def broadcast_message(sender_addr, message):
    sender_ip, sender_port = sender_addr

    msg_to_send = f"{sender_ip}:{sender_port} said: {message}"

    # Parcours du dictionnaire CLIENTS
    for addr, client_info in CLIENTS.items():
        if addr != sender_addr:
            try:
                # Envoi du message au client
                client_info["w"].write(msg_to_send.encode())
                await client_info["w"].drain()
                print(f"Sent message to {addr}: {msg_to_send}")
            except asyncio.CancelledError:
                pass

async def main():
    server = await asyncio.start_server(handle_client, '10.1.2.20', 13337)

    async with server:
        print("Server started. Listening for incoming connections...")
        await server.serve_forever()

# Lancement du serveur
asyncio.run(main())
