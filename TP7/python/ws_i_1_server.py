import asyncio
import websockets

async def handle_client(websocket, path):
    while True:
        # Attendre le message du client
        client_message = await websocket.recv()

        # Afficher le message côté serveur
        print(f"Serveur a reçu : {client_message}")

        # Construire la réponse
        server_response = f"Hello client ! Received \"{client_message}\""

        # Envoyer la réponse au client
        await websocket.send(server_response)

start_server = websockets.serve(handle_client, "localhost", 13337)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
