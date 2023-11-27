import logging
from logging.handlers import RotatingFileHandler
import re
import select
import socket


def setup_logger():
    
    log = logging.getLogger('bs_client')
    log.setLevel(logging.DEBUG)
    
    formate = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formate)
    log.addHandler(console_handler)
    
    path_log_file =  '/var/log/bs_client/bs_client.log'
    file_handler = RotatingFileHandler(path_log_file, maxBytes=10240, backupCount=1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formate)
    log.addHandler(file_handler)
    
    return log

try:
    logg = setup_logger()
    
    operation = input("Saisis une opération arithmétique (addition, soustraction, multiplication) : ")
    
    pattern = re.compile(r'^(-?\d+)\s*([-+*/])\s*(-?\d+)$')
    match = pattern.match(operation)
    
    if not match:
        raise ValueError('Opération invalide. Utilisez seulement des opérations arithmétiques avec des nombres entiers.')
    
    serv_ip = '10.1.2.15'
    serv_port = 13337
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serv_ip, serv_port))
    logg.info(f"Connecté au serveur {serv_ip}:{serv_port}")
    
    client.send(operation.encode())
    
    ready, _, _ = select.select([client], [], [], 5)
    if ready:
        response = client.recv(1024).decode()
        logg.info(f"Réponse du serveur: {response}")
    else:
        raise TimeoutError("Timeout : aucune réponse du serveur dans le délai imparti.")
    
except ValueError as ve:
    logg.error(f"Erreur de valeur : {ve}")
except TimeoutError as te:
    logg.error(f"Erreur de valeur : {te}")
except Exception as e:
    logg.error(f"Erreur inattendue : {e}")
finally:
    client.close()
    
    