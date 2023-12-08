import asyncio

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

    try:
        # Connexion au serveur
        reader, writer = await asyncio.open_connection(*server_address)

        # Exécuter les tâches en parallèle
        await asyncio.gather(
            send_messages(writer),
            receive_messages(reader)
        )

    except KeyboardInterrupt:
        pass
    finally:
        # Fermer la connexion après Ctrl+C
        if not writer.is_closing():
            writer.close()

if __name__ == "__main__":
    asyncio.run(main())
