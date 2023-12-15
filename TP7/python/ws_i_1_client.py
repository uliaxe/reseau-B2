import asyncio
import websockets

async def user_input():
    uri = "ws://10.1.2.20:13337"  # Mettez l'adresse IP et le port appropriés du serveur

    async with websockets.connect(uri) as websocket:
        while True:
            # L'utilisateur saisit une chaîne
            user_message = input("Saisissez une chaîne : ")

            # Envoyer la chaîne au serveur
            await websocket.send(user_message)

            # Recevoir la réponse du serveur
            server_response = await websocket.recv()

            # Afficher la réponse côté client
            print(f"Client a reçu : {server_response}")

# Lancer la boucle d'événements pour le client
asyncio.get_event_loop().run_until_complete(user_input())
