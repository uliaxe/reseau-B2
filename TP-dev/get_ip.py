import psutil

def get_wifi_ip_address():
    interfaces = psutil.net_if_addrs()
    
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == 2 and "Wi-Fi" in interface: 
                print(f"Ton adresse IP c'est :{addr.address}")

get_wifi_ip_address()


