#Leggere, scrivere e visualizzare immagini in OpenCV e Python
import argparse

import cv2

#definiamo la variabile ap, e la relativa classe
ap = argparse.ArgumentParser()
#Specifichiamo l'argomento che passeremo al nostro script definendolo come obbligatorio
ap.add_argument("-i","--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
#Leggere l'immagine da file system definendo la gamma di colori BGR
image = cv2.imread(args["image"], cv2.IMREAD_COLOR)

#Stampiamo la forma della nostra figura
print("image.shape: {}".format(image.shape))
#Stampiamo il formato che avranno i singoli pixel della nostra matrice 
print("image.shape: {}".format(image.dtype))

#Stampiamo a video la larghezza dell'immagine
print("width: {}".format(image.shape[1]))
##Stampiamo a video l'altezza dell'immagine
print("hight: {}".format(image.shape[0]))

#Accetta in input una stringa, ovvero il titolo che verrà attribuito alla finestra in cui comparirà l'immagine  e 
# "image" indica l'immagine da mostrare
cv2.imshow("Logo New Mig", image)
#tempo per cui la finsetra aspetta un nostro input in ms prima di chiudersi
cv2.waitKey()

#Scrive su file system l'immagine su un path di destinazione
cv2.imwrite("out/01_image.jpg", image)
