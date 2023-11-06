import socket
def lookup(domain_name):
    try:
        ip = socket.gethostbyname(domain_name)
        return ip
    except socket.gaierror:
        return f"'{domain_name}' n'est pas un domaine valide."