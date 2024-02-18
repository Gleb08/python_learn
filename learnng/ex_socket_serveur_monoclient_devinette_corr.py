import socket
## socket serveur
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 2345         # choix d'un port 
# on bind notre socket
Sock.bind((Host,Port))
# On est a l'ecoute d'une seule et unique connexion 
Sock.listen(1)
# la socket du serveur attends jusqu'à la connexion d'un client
client, adresse = Sock.accept() # accepte les connexions de l'exterieur
print ("Un client (",adresse,") arrive. Début du jeu")

# la règle du jeu
# Etape 1 : le serveur envoie un message d'accueil au client
# Etape 2 : le client donne une valeur et envoie au serveur
#           le serveur recoit la valeur devinnée par le client et renvoie des msg correspondants
msg_send=""
msg_rcv=""
chiffre_devinner=78   # ou utiliser une génération aléatoire
# étape 1 : le serveur envoie un msg d'accueil au client
msg_send = "Deviner un chiffre"
client.send(msg_send.encode())

while 1 : # une boucle infini... mais peut être remplacée par une "bonne" condition de jeux        
        msg_rcv = client.recv(255).decode() # on recoit 255 caracteres max
        print("Chiffre du joueur : ",msg_rcv)
        if not msg_rcv: # si on ne recoit plus rien
                print("Connexion perdue")
                client.close()
        #en fonction de la donnée reçue
        int_rcv=int(msg_rcv)
        if (int_rcv<chiffre_devinner):
                msg_send="plus grand"
        elif (int_rcv==chiffre_devinner):
                msg_send="bravo"
        else:
                msg_send="plus petit"
        client.send(msg_send.encode())
        # traiter pour sortir la boucle???
