# TP3 DEV : Python et réseau

## I. Ping

🌞 **`ping_simple.py`**

[ping_simple.py](python/ping_simple.py)

```bash
Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=15 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=15 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=18 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=15 ms TTL=114

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 15ms, Maximum = 18ms, Moyenne = 15ms
```

---

🌞 **`ping_arg.py`**

[ping_arg.py](./python/ping_arg.py)

```bash
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\ping_arg.py' 8.8.8.8

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114
Réponse de 8.8.8.8 : octets=32 temps=16 ms TTL=114

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 16ms, Maximum = 16ms, Moyenne = 16ms
```

🌞 **`is_up.py`**

[is_up.py](./python/is_up.py)

```bash
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\is_up.py' 8.8.8.8
UP !
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\is_up.py' papapaa
DOWN !
```

## II. DNS

🌞 **`lookup.py`**

[lookup.py](./python/lookup.py)

```bash
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\lookup.py'
rentrer le hostname : ynov.com
adresse IP : 104.26.10.233
PS C:\Users\lukas\reseau-B2> 
```

## III. Get your IP

🌞 **`get_ip.py`**

[get_ip.py](./python/get_ip.py)

```bash
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\get_ip.py'
Ton adresse IP c'est :10.33.76.171
```

## IV. Mix

🌞 **`network.py`**

[network.py](python/network.py)

```bash
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\network.py' lookup ynov.com
l'adresse IP de  ynov.com est 172.67.74.226
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\network.py' ping 8.8.8.8
 Is up!
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\network.py' ip
Ton adresse IP c'est :10.33.76.171
PS C:\Users\lukas\reseau-B2> python '.\TP-Dev\network.py' nanvrmrendlargen 
nanvrmrendlargen is not an available command. Déso.
```
