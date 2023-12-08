import asyncio
import sys

async def send_messages(writer):
    while True:
        # Saisie utilisateur
        message = input("Entrez votre message (ou Ctrl+C pour quitter): ")

        # Envoi du message au serveur
        writer.write(message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        # Réception des messages du serveur
        data = await reader.read(1024)
        if not data:
            break

        message = data.decode()
        print(f"Message reçu : {message}")

async def main():
    # Définir l'adresse et le port du serveur
    server_address = ('10.1.2.20', 13337)

    # Créer un socket TCP/IP
    client_socket = asyncio.StreamReader()
    client_writer = asyncio.StreamWriter(None, None, None, asyncio.get_running_loop())

    # Connexion au serveur
    await asyncio.gather(
        asyncio.open_connection(*server_address, limit=2**16, ssl=False),
        send_messages(client_writer),
        receive_messages(client_socket)
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
