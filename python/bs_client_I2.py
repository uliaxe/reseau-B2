import socket
import sys

host='10.1.2.15'
port=13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    
    message = input("Que veux-tu envoyer au serveur : ")
    s.sendall(message.encode())
    
    response = s.recv(1024).decode()
    print(f"Réponse du serveur : {response}")

except Exception as e:
    print(f"Erreur : {e}")
    sys.exit(1)

finally:
    s.close()
    sys.exit(0)  
    
    