import socket
## socket client
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # on cree notre socket
# l'adresse du serveur : IP + port
Host = '127.0.0.1'
Port = 5000
# le client connect au server 
Sock.connect((Host, Port))
while 1:
        msg = input("Saisir un message pour envoyer au serveur : ")
        Sock.send(msg.encode()) # on envoie ces donnees
