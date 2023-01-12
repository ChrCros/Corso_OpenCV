# Applicazione di un Offeset alla nostra immagine

import argparse

import numpy as np

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

# definiamo la matrice di traslazione
## [1, 0, tx]
## [0, 1, ty]
M = np.float32([[1, 0, 25], [0, 1, 509]])
#defibiamo la nuova matrice che conterrà l'immagine traslata
shifted = cv2.warpAffine(image, M, (w,h))
cv2.imshow("shifted down and right", image)
cv2.waitKey()

# definiamo la matrice di traslazione
## [1, 0, tx]
## [0, 1, ty]
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("shifted top and left", image)
cv2.waitKey()

#creiamo una funzione di utility per evutare di pover riscrivere la funzione d traslazione ogni volta
def translate(image, x, y):
    h, w = image.shape[:2]

    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (w,h))

    return shifted

shifted = translate(image, x=0, y=100)
cv2.imshow("shifted with custom function", image)
cv2.waitKey()