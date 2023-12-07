import socket
import argparse
import sys 

def start_server(port) :
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        ip_adress = socket.gethostbyname(socket.gethostname())
    
        server_socket.bind((ip_adress, port))
    
        server_socket.listen(5)
        print(f"Serveur écoute sur {ip_adress}:{port}")
    
        while True:
        
            client_socket, client_address = server_socket.accept()
            print(f"Un client vient de se connecter et son IP c'est {client_address}")
        
            message = client_socket.recv(1024).decode()
            print(f"Message du client: {message}")
        
            if "meo" in message.lower():
                response = "Meo à toi confrère ."
            elif "waf" in message.lower():
                response = "ptdr t ki"
            else:
                response ="Mes respects humble humain."
            
            client_socket.sendall(response.encode())
            
            client_socket.close()
            
    finally: 
        server_socket.close()
    
def main():
    parser = argparse.ArgumentParser(description='Serveur TCP avec gestion d\'options.')
    parser.add_argument ('-p', '--port', type=int, default=13337, help='Numéro de port pour écouter les connexions. (Par défaut : 13337)')
    
    args = parser.parse_args()
    
    if args.port < 0 or args.port > 65535:
        print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        exit(1)
    elif args.port <= 1024: 
        print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
        exit(2)
        
    start_server(args.port)
    
if __name__ == '__main__':
    main()
    
        



    