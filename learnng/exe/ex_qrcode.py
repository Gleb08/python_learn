# pip3 install pyqrcode
# pip3 install pypng
import pyqrcode
#créer un qrcode
qrcode = pyqrcode.create("Hello")
qrcode.png("hello.png", scale=6)
qrcode.png("hello1.png", scale=60)
#scale parameter sets how large to draw a single module.
#By default one point (1/72 inch) is used to draw a single module

### Exo d'application
### Faire un programme qui saisit le nom, le prenom, l'adresse, le mail...
### Le programme crée un QRcode pour la personne
### Le programme demande le nom de fichier de sortie, ou par défaut, NOM_Prenom

# pip3 install opencv-python  --> une biblio. pour traiter les images
# pip3 install pyzbar
from pyzbar.pyzbar import decode
import cv2
### éventuelle err. (avec Windows, à cause de l'envi. C++) : https://www.microsoft.com/en-us/download/details.aspx?id=40784
img =cv2.imread("exLireQR.png")
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))

### Exo d'application
### Faire un programme avec un menu de 2 options :
### Créer un QRcode
### Lire un QRcode : l'utilisateur saisit le nom du fichier





