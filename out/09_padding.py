#paddig di immagini: aggiungere un bordo o replicare un bordo esistente
# alle nostre immagini

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

# cv2.BORDER_REPLICATE replicates the very last pixel - aaaaaa|abcdefgh|hhhhhhh
## definiamo la nuostra nuova immagine, che sarà l'immagine originale a cui abbiamo 
## aggiunto un padding secondola policy di replicate -->aggiungiamo un bordo alla nst immagine
replicate = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_REPLICATE)

# cv2.BORDER_REFLECT: reflect the outer-most border - hfedcab|abcdefh|hfedcba
reflect = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_REFLECT)

# cv2.BORDER_REFLECT_101: the outer-most border in not parts of the reflected border hfedcb|abcdefh|fedcba
reflect_101 = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)

#cv2.BORDER_WRAP: cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_WRAP)

#cv2.BORDER_CONSTANT:
constant = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=Colors.BLACK)

cv2.imshow("replicate", replicate)
cv2.waitKey()

cv2.imshow("reflect", reflect)
cv2.waitKey()

cv2.imshow("reflect 101", reflect_101)
cv2.waitKey()

cv2.imshow("wrap", wrap)
cv2.waitKey()

cv2.imshow("constant", constant)
cv2.waitKey()