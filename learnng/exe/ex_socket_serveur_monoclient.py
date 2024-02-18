import socket
## socket serveur
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = '127.0.0.1' # l'ip locale de l'ordinateur
Port = 5000         # choix d'un port
# on bind notre socket
Sock.bind((Host, Port))
# On est a l'ecoute d'une seule et unique connexion (1)
Sock.listen(1)
# la socket du serveur attends jusqu'à la connexion d'un client
client, adresse = Sock.accept() # accepte les connexions de l'exterieur
print ("Un client dont l'adresse est : ", adresse, " vient de se connecter au serveur !")
while 1:        
        RequeteDuClient = client.recv(255).decode() # on recoit 255 caracteres max
        if not RequeteDuClient: # si on ne recoit plus rien
                print("Connexion perdue")
                client.close()
        print (RequeteDuClient)         # affiche les donnees venants de client
        
