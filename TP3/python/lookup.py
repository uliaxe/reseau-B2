from socket import gethostbyname

name = input("Enter a hostname: ")
ip = gethostbyname(name)
print("L'adresse IP de ", name, " est ", ip)
