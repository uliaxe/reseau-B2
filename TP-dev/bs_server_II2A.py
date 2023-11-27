import logging
import sys
from logging.handlers import timedRotatingFileHandler
from datetime import datetime, timedelta
import threading
import socket
import argparse

def setup_logger():
    
    logger = logging.getlogger('bs_server')
    logger.setlevel(logging.DEBUG)
 
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    file_handler = timedRotatingFileHandler('/var/log/bs_server.log', when='midnight', interval=1, backupCount=7)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    return logger

def check_last_client(logger):
    while True:
        if datetime.now() - last_client > timedelta(minutes=1):
            logger.warning('Aucun client depuis plus de une minute.')
        threading.Event().wait(60)
        
        
def start_server(port):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    logger = setup_logger()
    
    global last_client
    last_client = datetime.now()
    
    
    threading.Thread(target=check_last_client, args=(logger,), daemon=True).start()
    
    try:
        ip_addr = socket.gethostbyname(socket.gethostname())
        
        serv_socket.bind((ip_addr, port))
        
        serv_socket.listen(5)
        logger.info (f"Lancement du serveur. Le serveur tourne sur {ip_addr}:{port}")
        
        while True:
            client_socket, client_addr = serv_socket.accept()
            logger.info(f"Connexion d'un client. Un client {client_addr[0]} s'est connecté.")
            
            message = client_socket.recv(1024).decode()
            logger.info(f"Message reçu d'un client. Le client {client_addr[0]} a envoyé : {message}.")
            
            if "meo" in message.lower():
                response = "Meo à toi confrère !"
            elif "waf" in message.lower():
                response = "ptdr t ki"
            else:
                response = "Mes respects humble humain."
                
            client_socket.send(response.encode())
            logger.info(f"Message envoyé par le serveur. Réponse envoyée au client {client_addr[0]} : {response}.")
            
            last_client = datetime.now()
            
            client_socket.close()
            
    except KeyboardInterrupt:
        pass
    finally:
        serv_socket.close()
        
def main():
    parse = argparse.ArgumentParser(description="Serveur TCP avec gestion d\'options")
    parse.add_argument('-p', '--port', type=int, default=13337, help='Numéro de port pour écouter les connexions. (Par défaut : 13337)')   
    
    arg = parse.parse_args()
    
    if arg.port < 0 or arg.port > 65535:
        print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        exit(1) 
    elif arg.port <= 1024:
        print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
        exit(2)
        
    start_server(arg.port)
    
    if __name__ == '__main__':
        main()
        
    
    
    
