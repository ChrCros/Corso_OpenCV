#Cropping di immagini

import argparse

import cv2

from src.colors import Colors

# definiamo la variabile ap, e la relativa classe
ap = argparse.ArgumentParser()
# Specifichiamo l'argomento che passeremo al nostro script definendolo come obbligatorio
ap.add_argument("-i","--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Leggere l'immagine da file system definendo la gamma di colori BGR
image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey()

# coordinates of the "import cv2" text inside the image
## coordinate angolo in alto a sx
x1, y1 = 145, 275
##coordinate angolo in basso a dx
x2, y2 = 305, 321

#effettuiamo il cropping tramite lo slicing di array numpy contenente
#la nostra immagine
cropped = image[y1:y2, x1:x2]
cv2.imshow("Cropped", cropped)
cv2.waitKey()

##Prendiamo tutti i pixel della nostra immagine cropped e li impostiamo tutti 
##al valore BLU direttamente sull'immagine originale
cropped[:, :] = Colors.BLUE
cv2.imshow("Source image modified", image)
cv2.waitKey()


##Prendiamo tutti i pixel della nostra immagine cropped e li impostiamo tutti 
#al valore ROSSO su una copia dell'immagine originale
cropped_copy = image[y1:y2, x1:x2].copy()
cropped_copy[:, :] = Colors.RED

cv2.imshow("Cropped copy", cropped_copy)
cv2.waitKey()

#Mostriamo immagine originale per dimostrare che è immutata rispetto ultima visualizzazione
cv2.imshow("Source image not modified again", image)
cv2.waitKey()



