import socket
## socket client
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
# l'adresse du serveur : IP + port
Host = '127.0.0.1'
Port = 2345
# le client connect au server 
Sock.connect((Host,Port))
donnee_send=""
donnee_rcv=""

# la règle du jeu
# Etape 1 : le serveur envoie un message d'accueil au client
# Etape 2 : le client donne une valeur et envoie au serveur
#           le serveur recoit la valeur devinnée par le client et renvoie des msg correspondants

donnee_rcv=Sock.recv(255).decode()
print(donnee_rcv)
        
while 1: # une boucle infini... mais peut être remplacée par une condition
        donnee_send=input("Une proposition? ")
        Sock.send(donnee_send.encode())
        donnee_rcv=Sock.recv(255).decode()
        print(donnee_rcv)
        # traiter pour sortir la boucle???
