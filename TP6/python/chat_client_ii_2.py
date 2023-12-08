import socket

def main():
    # Créer un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Définir l'adresse et le port du serveur
    server_address = ('10.1.2.20', 133337)

    try:
        # Se connecter au serveur
        client_socket.connect(server_address)

        # Envoyer "Hello" au serveur
        message = "Hello"
        client_socket.sendall(message.encode())

        # Attendre la réponse du serveur
        data = client_socket.recv(1024)
        response = data.decode()

        # Afficher la réponse du serveur
        print(f"Réponse du serveur: {response}")

    finally:
        # Fermer la connexion
        client_socket.close()

if __name__ == "__main__":
    main()
