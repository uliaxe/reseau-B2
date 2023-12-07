import socket
import re
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    log = logging.getLogger('bs_client')
    log.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(message)s')

    log_file_path = '/var/log/bs_client/bs_client.log'
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10240, backupCount=1)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log

try:
    logger = setup_logger()

    server_ip = '10.1.2.15'  
    server_port = 13337

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_ip, server_port))
    print(f"Connecté au serveur {server_ip}:{server_port}")


    user_input = input("Saisis le message à envoyer au serveur: ")

    if not isinstance(user_input, str):
        raise TypeError("L'entrée doit être une chaîne de caractères.")

    pattern = re.compile(r'(waf|meo)', re.IGNORECASE)
    if not pattern.search(user_input):
        raise ValueError("La chaîne doit contenir soit 'waf' soit 'meo'.")

    client_socket.send(user_input.encode())

    response = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {response}")

except TypeError as te:
    logger.error(f"Erreur de type : {te}")
except ValueError as ve:
    logger.error(f"Erreur de valeur : {ve}")
except Exception as e:
    logger.error(f"Erreur inattendue : {e}")
finally:

    client_socket.close()
