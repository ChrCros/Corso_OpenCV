# Effettuare il dimensionamento delle nostre immagini

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


# resize by width
new_width = 300
resize_ratio = new_width / w
dim = (new_width, int(h * resize_ratio))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized by width", resized)
cv2.waitKey()


# resize by height
new_height = 300
resize_ratio = new_height / w
dim = (int(w * resize_ratio), new_height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized by height", resized)
cv2.waitKey()


# resize by percent
## effettrua un resize del 50% dell'immagine sia sul asse delle ascisse che sulle ordinate
resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized by 50 percent", resized)
cv2.waitKey()