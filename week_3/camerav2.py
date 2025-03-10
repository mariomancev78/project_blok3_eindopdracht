import cv2
import os

def maak_foto(opslag_pad="C:/Pad/Om/OpTeSlaan", beginbestandsnaam="foto"):
    os.makedirs(opslag_pad, exist_ok=True)
    bestandsnummer = 1
    volledig_pad = None

    while True:
        bestandsnaam = f"{beginbestandsnaam}{bestandsnummer}.png"
        volledig_pad = os.path.join(opslag_pad, bestandsnaam)
        
        if not os.path.exists(volledig_pad):
            break
        
        bestandsnummer += 1
    
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        return None, "Kan de camera niet openen :( "

    retval, img = camera.read()
    
    camera.release()
    cv2.destroyAllWindows()

    if not retval:
        return None, "$ERROR$"

    cv2.imwrite(volledig_pad, img)
    return volledig_pad, "Foto gemaakt en opgeslagen :) "

