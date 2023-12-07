import socket
import re 


host='10.1.2.15'
port=13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.connect((host, port))
    print(f"Connecté au serveur {host}:{port}")
    
    user_input = input("Saisir le message à envoyer au serveur: ")
    
    if not isinstance(user_input, str):
        raise TypeError("Le message doit être une chaîne de caractères")
    
    pattern = re.compile(r'(waf|meo)', re.IGNORECASE)
    if not pattern.search(user_input):
        raise ValueError("Le message doit contenir soit 'waf' soit 'meo'.")
    
    s.sendall(user_input.encode())
    
    response = s.recv(1024).decode()
    print(f"Réponse du serveur: {response}")
    
except TypeError as te :
    print(f"Erreur de type : {te}")
except ValueError as ve :
    print(f"Erreur de valeur : {ve}")
except Exception as e:
    print(f"Erreur inattendue : {e}")
    

 


finally:
    s.close()
    