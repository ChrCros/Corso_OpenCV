#Leggere il valore di un pixel ed impostarlo ad un colore di nostra scelta

import argparse

import cv2

#definiamo la variabile ap, e la relativa classe
ap = argparse.ArgumentParser()
#Specifichiamo l'argomento che passeremo al nostro script definendolo come obbligatorio
ap.add_argument("-i","--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
#Leggere l'immagine da file system definendo la gamma di colori BGR
image = cv2.imread(args["image"])

#visualizzaimo a video la nostra immagine e diamo titolo alla finestra
cv2.imshow("Original", image)
#attende che venga premuto un tasto
cv2.waitKey()

x = 0
y = 0
#estraiamo dalla matrice tridimensionale, i valori relativi al pixel sulle cordinate (x, y)
(b, g, r) = image[y, x]
#Visualizzaimo il valore sui singoli canali
print("pixel value at ({}, {}) - Red: {}, Green {}, Blu {}".format(x, y, r, g, b))

#impostiamo il colore rosso al pixel
image[0, 0] = (0, 0, 255)
(b, g, r) = image[y, x]
#andiamo a leggere qual è adesso il vaore del pixel alle cordinate (0,0)
print("pixel value at ({}, {}) - Red: {}, Green {}, Blu {}".format(x, y, r, g, b))

#crea una finestra di dimensione 100x100
x1 = 0
x2 = 100
y1 = 0
y2 = 100
top_left_crop = image[y1:y2, x1:x2]
cv2.imshow("Top Left Crop", top_left_crop)
#tempo per cui la finsetra aspetta un nostro input in ms prima di chiudersi
cv2.waitKey()

#definiamo l'area di cropping con i colore blu
image[y1:y2, x1:x2] = (255, 0, 0)
#Accetta in input una stringa, ovvero il titolo che verrà attribuito alla finestra in cui comparirà l'immagine  e 
# "image" indica l'immagine da mostrare
cv2.imshow("Updated", image)
#tempo per cui la finsetra aspetta un nostro input in ms prima di chiudersi
cv2.waitKey()

