#Riflettere immagini sull'asse x e sull'asse y

import argparse

import cv2

# definiamo la variabile ap, e la relativa classe
ap = argparse.ArgumentParser()
# Specifichiamo l'argomento che passeremo al nostro script definendolo come obbligatorio
ap.add_argument("-i","--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Leggere l'immagine da file system definendo la gamma di colori BGR
image = cv2.imread(args["image"], cv2.IMREAD_COLOR)

## ricaviamo altezza e larghezza dell'immagine
h, w = image.shape[:2]
cv2.imshow("image", image)
cv2.waitKey()

#riflesso orrizzontale
flipped = cv2.flip(image, 1)
cv2.imshow("flipped horizontally", flipped)
cv2.waitKey()

#riflesso verticale
flipped = cv2.flip(image, 0)
cv2.imshow("flipped vertically", flipped)
cv2.waitKey()
