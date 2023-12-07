import logging
from logging.handlers import TimedRotatingFileHandler
import socket
from datetime import datetime
import re
import argparse


def setup_logger():
    
    log = logging.getLogger('bs_server')
    log.setLevel(logging.DEBUG)
    
    formate = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formate)
    log.addHandler(console_handler)
    
    file_handler = TimedRotatingFileHandler('/var/log/bs_server/bs_server.log', when='midnight', interval=1, backupCount=7)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formate)
    log.addHandler(file_handler)
    
    return log

def start_serv(port):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    logg = setup_logger()
    
    try:
        ip_addr = socket.gethostbyname(socket.gethostname())
        
        serv_socket.bind((ip_addr, port))
        
        serv_socket.listen(5)
        logg.info(f"Lancement du serveur. Le serveur tourne sur {ip_addr}:{port}")
        
        while True:
            
            client_socket, client_addr = serv_socket.accept()
            logg.info(f"Connexion d'un client. Un client {client_addr[0]} s'est connecté.")
            
            client_request = client_socket.recv(1024).decode()
            logg.info(f"Message reçu d'un client. Le client {client_addr[0]} a envoyé : {client_request}.")
            
            if not re.match(r'^\s*([-+]?\d+)\s*([+\-*/])\s*([-+]?\d+)\s*$', client_request):
                logg.error("Opération invalide. Veuillez saisir une opération arithmétique valide.")
                client_socket.send("Opération invalide. Veuillez saisir une opération arithmétique valide.".encode())
                continue
            res = eval(client_request)
            logg.info(f"Résultat de l'opération : {res}")
            
            client_socket.send(str(res).encode())
            
            client_socket.close()
            
    except KeyboardInterrupt:
        pass
    finally:
        serv_socket.close()
        
def main():
    parse = argparse.ArgumentParser(description='Serveur TCP avec gestion d\'options.')
    parse.add_argument('-p', '--port', type=int, default=13337, help='Numéro de port pour écouter les connexions. (Par défaut : 13337)')
    
    arg = parse.parse_args()
    
    if arg.port < 0 or arg.port > 65535:
        print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        exit(1)
    elif arg.port <= 1024:
        print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
        exit(2)
    start_serv(arg.port)
    
    if __name__ == '__main__':
        main()

            
            
        
    

