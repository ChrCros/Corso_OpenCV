#come effettuare la rotazione delle immagini

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

## definiamo il centr dell'immagine
center = (w // 2, h // 2)

cv2.imshow("image", image)
cv2.waitKey()


# definiamo matrice di rotazione
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("rotated by 45 degrees", rotated)
cv2.waitKey()


# definiamo matrice di rotazione
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("rotated by 90 degrees", rotated)
cv2.waitKey()


def rotate(image, angle, center=None, Scale=1.0):
    h, w = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, Scale)

    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated

rotated = rotate(image, 45)
cv2.imshow("rotated by 45 degrees with our function", rotated)
cv2.waitKey()


# cv2.ROTATE_90_CLOCKWISE | cv2.ROTATE_90_COUNTERCLOCKWISE | cv2.ROTATE_180
rotated = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("rotated by 180 degrees with our custom function", rotated)
cv2.waitKey()
    



