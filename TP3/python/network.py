import psutil
from socket import gethostbyname
from sys import argv
import os
import sys


def lookup(name):
    try:
        ip = gethostbyname(name)
        print("l'adresse IP de ", name, "est", ip)
    except:
        print("le hostname", name, "n'existe pas.")
        exit(1)

def ping(ip):
    ping_command = f"ping {ip}"
    ping_output = os.popen(ping_command).read()
    if "TTL=" in ping_output:
        print(" Is up!")
    else:
        print("Is down!")

def get_wifi_ip_address():
    interfaces = psutil.net_if_addrs()
    
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == 2 and "Wi-Fi" in interface: 
                print(f"Ton adresse IP c'est :{addr.address}")




if argv[1] == "lookup":
    lookup(argv[2])

elif argv[1] == "ping":
    ping(argv[2])

elif argv[1] == "ip":
    get_wifi_ip_address()

else:
    print(f"{argv[1]} is not an available command. Déso."  )
    exit(1)
