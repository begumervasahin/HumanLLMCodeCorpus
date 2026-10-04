import os
from PIL import Image
import piexif
from random import randint
import random
def fonk1(dir1, imgg):
    b1 = piexif.load(imgg)
    if str(b1['GPS'][2]) and str(b1['GPS'][4]) and str(b1['GPS'][6]):
        print(b1['GPS'][2],"   ",b1['GPS'][4],"   ",b1['GPS'][6])
    os.chdir(dir1)
    b2 = os.listdir(dir1)
    for dirlist in b2:
        b3 = random.randint(-99, 99)
        b4 = random.randint(-99, 99)
        b5 = Image.open(dirlist)
        b6 = piexif.load(b5.info["b8"])
        if str(b1['GPS'][2]) and str(b6['GPS'][2]):
            b6['GPS'][2] = (
            (b1['GPS'][2][0][0], b1['GPS'][2][0][1]), (b1['GPS'][2][1][0], b1['GPS'][2][1][1]),
            (b1['GPS'][2][2][0] + b3, b1['GPS'][2][2][1]))
        if str(b1['GPS'][4]) and str(b6['GPS'][4]):
            b6['GPS'][4] = (
            (b1['GPS'][4][0][0], b1['GPS'][4][0][1]), (b1['GPS'][4][1][0], b1['GPS'][4][1][1]),
            (b1['GPS'][4][2][0] + b4, b1['GPS'][4][2][1]))
        if str(b1['GPS'][6]) and str(b6['GPS'][6]):
            b6['GPS'][6] = b1['GPS'][6]
        print(b6['GPS'][2],"   ",b6['GPS'][4],"   ",b6['GPS'][6])
        try:
            b7 = piexif.dump(b6)
            b5.save(dirlist, "jpeg", b8 = b7)
        except:
            print("Error ")
b9 = input(" Ingresa el nombre de la imagen:")
b10 = input(" Ingresa el nombre de la carpeta:")
fonk1(b10, b9)