# TP2 : Environnement virtuel

☀️ Sur **`node1.lan1.tp2`**

- afficher ses cartes réseau
  
```bash
[uliaxe@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:09:88:ec brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe09:88ec/64 scope link
       valid_lft forever preferred_lft forever
```

- afficher sa table de routage

```bash
[uliaxe@node1 ~]$ ip route show
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3
```

- prouvez qu'il peut joindre `node2.lan2.tp2`

```bash
[uliaxe@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=2.84 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.38 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=1.06 ms
64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=0.951 ms
64 bytes from 10.1.2.12: icmp_seq=5 ttl=63 time=1.33 ms
64 bytes from 10.1.2.12: icmp_seq=6 ttl=63 time=1.01 ms
64 bytes from 10.1.2.12: icmp_seq=7 ttl=63 time=0.949 ms
^C
--- 10.1.2.12 ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6006ms
rtt min/avg/max/mdev = 0.949/1.360/2.837/0.624 ms

```

- prouvez avec un `traceroute` que le paquet passe bien par `router.tp2`

```bash
[uliaxe@node1 ~]$ traceroute 10.1.2.11
traceroute to 10.1.2.11 (10.1.2.11), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.712 ms  0.681 ms  0.669 ms
 2  10.1.2.11 (10.1.2.11)  2.425 ms !X  2.343 ms !X  2.297 ms !X
```

## II. Interlude accès internet

☀️ **Sur `router.tp2`**

- prouvez que vous avez un accès internet (ping d'une IP publique)

```bash
[uliaxe@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=14.0 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=114 time=12.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=114 time=12.5 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=114 time=13.8 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=114 time=12.4 ms
^C
--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4009ms
rtt min/avg/max/mdev = 12.354/13.013/13.974/0.712 ms
```

- prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)

```bash
[uliaxe@router ~]$ ping ynov.com
PING ynov.com (104.26.10.233) 56(84) bytes of data.
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=1 ttl=54 time=14.4 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=2 ttl=54 time=13.7 ms
64 bytes from 104.26.10.233 (104.26.10.233): icmp_seq=3 ttl=54 time=12.1 ms

--- ynov.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 12.138/13.399/14.366/0.933 ms
```

☀️ **Accès internet LAN1 et LAN2**

- ajoutez une route par défaut sur les deux machines du LAN1

```bash
[uliaxe@node2 ~]$ sudo ip route add default via 10.1.1.254
[sudo] password for uliaxe:
[uliaxe@node2 ~]$ ip route show
default via 10.1.1.254 dev enp0s3
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.12 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3 proto static metric 100
```

- ajoutez une route par défaut sur les deux machines du LAN2

```bash
[uliaxe@node2 ~]$ sudo ip route add default via 10.1.2.254
[sudo] password for uliaxe:
[uliaxe@node2 ~]$ ip route show
default via 10.1.2.254 dev enp0s3
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.12 
metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3 proto static metric 100
```

- configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms

```bash
[uliaxe@node2 ~]$ sudo echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
nameserver 8.8.8.8
```

- dans le compte-rendu, mettez-moi que la conf des points précédents sur `node2.lan1.tp2`
- prouvez que `node2.lan1.tp2` a un accès internet :
  - il peut ping une IP publique
  - il peut ping un nom de domaine public

## III. Services réseau

## 1. DHCP

☀️ **Sur `dhcp.lan1.tp2`**

- n'oubliez pas de renommer la machine (`node2.lan1.tp2` devient `dhcp.lan1.tp2`)

```bash
[uliaxe@dhcp ~]$ hostname
dhcp.lan1.tp2
```

- changez son adresse IP en `10.1.1.253`

```bash
[uliaxe@dhcp ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:11:49:79 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.253/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe11:4979/64 scope link
       valid_lft forever preferred_lft forever
```

- setup du serveur DHCP
  - commande d'installation du paquet
  - fichier de conf
  - service actif
