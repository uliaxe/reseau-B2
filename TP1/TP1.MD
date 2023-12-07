# TP1 : Maîtrise réseau du poste

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
  - [I. Basics](#i-basics)
  - [II. Go further](#ii-go-further)
  - [III. Le requin](#iii-le-requin)

## I. Basics

☀️ **Carte réseau WiFi**

```bash
C:\Users\lukas>ipconfig /all

Carte réseau sans fil Wi-Fi :

   Adresse physique . . . . . . . . . . . : 14-13-33-F9-BB-EB
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.171
```

- en notation CIDR, par exemple `/20`
- ET en notation décimale, par exemple `255.255.240.0`

  ☀️ **Déso pas déso**

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi :  10.33.64.0
- l'adresse de broadcast : 10.33.79.255
- le nombre d'adresses IP disponibles dans ce réseau : 4096

☀️ **Hostname**

- déterminer le hostname de votre PC : DESKTOP-57DVPQP

---

☀️ **Passerelle du réseau**

Déterminer...

```bash
C:\Users\lukas>ipconfig /all
 Passerelle par défaut. . . . . . . . . : 10.33.79.254
```

```bash
C:\Users\lukas>arp -a
[...]
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```

---

☀️ **Serveur DHCP et DNS**

```bash
C:\Users\lukas>ipconfig /all
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
      Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

☀️ **Table de routage**

Déterminer...

- dans votre table de routage, laquelle est la route par défaut

 ```bash

 C:\Users\lukas>route print -4
 
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.171     30
 ```

## II. Go further

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`

```bash
C:\Windows\System32\drivers\etc> cat hosts

1.1.1.1 b2.hello.vous
```

- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`

```bash
C:\Users\lukas>ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 10ms, Maximum = 11ms, Moyenne = 10ms
```

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo
- le port du serveur auquel vous êtes connectés

```bash
C:\Users\lukas>nslookup youtube.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    youtube.com
Addresses:  2a00:1450:4007:80c::200e
          172.217.20.174
```

- le port que votre PC a ouvert en local pour se connecter au port du serveur distant

```bash
C:\Users\lukas>netstat -n

Connexions actives

[...]
 TCP    10.33.76.171:63939     172.217.20.174:443     ESTABLISHED
[...]
```

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`

```bash
C:\Users\lukas>nslookup wwww.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    reverseproxy.ynov.com
Address:  178.32.154.7
Aliases:  wwww.ynov.com
```

- à quel nom de domaine correspond l'IP `174.43.238.89`

```bash
C:\Users\lukas>nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

☀️ **Hop hop hop**

Déterminer...

- par combien de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`

```bash
C:\Users\lukas>tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     4 ms     1 ms     1 ms  10.33.79.254
  2     3 ms     3 ms     3 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     4 ms     3 ms     3 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     4 ms     3 ms     3 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    12 ms    11 ms    13 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    11 ms    12 ms    12 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    17 ms    11 ms    10 ms  141.101.67.48
  8    20 ms    12 ms    12 ms  172.71.124.4
  9    12 ms    11 ms    11 ms  172.67.74.226

Itinéraire déterminé.
```

☀️ **IP publique**

Déterminer...

- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

```bash
195.7.117.146
```

---
☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés
  
 ```bash
 
C:\Users\lukas>arp -a |select-String "10.33"

Interface : 10.33.76.171 --- 0xf
  Adresse Internet      Adresse physique      Type
  10.33.69.34           c8-58-c0-63-5a-92     dynamique
  10.33.71.107          84-c5-a6-e4-58-1d     dynamique
  10.33.71.223          3c-06-30-1f-93-51     dynamique
  10.33.72.0            c0-b5-d7-c2-40-91     dynamique
  10.33.73.192          70-cf-49-3f-fc-fa     dynamique
  10.33.75.102          6a-d1-b5-cd-37-18     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
 ```

## III. Le requin

☀️ **Capture ARP**

[Lien vers capture ARP](./wireshark/arp.pcapng)

☀️ **Capture DNS**

[Lien vers capture DNS](./wireshark/dns.pcapng)

☀️ **Capture TCP**

[Lien vers capture TCP](./wireshark/tcp.pcapng)
