import socket
import re


def valid_expression(expr):
    #vérifie si l'expression est une opération arithmétique valide
    pattern = re.compile(r'^\d{1,5}\s*[\+\-\*]\s*\d{1,5}$')
    return bool(pattern.match(expr))

def send_message(s, msg):
    # Encode le message et envoie sur le réseau avec une séquence de fin
    encoded_msg = msg.encode('utf-8')
    msg_length = len(encoded_msg) + len(b'<clafin>')
    header = msg_length.to_bytes(4, byteorder='big')
    payload = header + encoded_msg + b'<clafin>'
    s.send(payload)

    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.2.15', 13337))

# Demande à l'utilisateur de saisir une expression arithmétique valide
while True:
    expr = input("Entrez une expression arithmétique valide: ")
    if valid_expression(expr):
        break
    else:
        print("Expression invalide. Veuillez réessayer.")

# Convertit l'expression en chaîne de caractères avant de l'envoyer
send_message(s, str(expr))
s.close()
