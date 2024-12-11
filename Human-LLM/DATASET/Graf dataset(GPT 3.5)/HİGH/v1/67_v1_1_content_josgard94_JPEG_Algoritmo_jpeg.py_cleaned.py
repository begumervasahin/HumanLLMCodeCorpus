import re
import scipy
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
b1 = [[16, 11, 10, 16, 24, 40, 51, 61],
     [12, 12, 14, 19, 26, 58, 60, 55],
     [14, 13, 16, 24, 40, 57, 69, 56],
     [14, 17, 22, 29, 51, 87, 80, 62],
     [18, 22, 37, 56, 68 ,109 ,103 ,77],
     [24, 35, 55, 64, 81 ,104 ,113 ,92],
     [49, 64, 78, 87, 103, 121, 120, 101],
     [72, 92, 95, 98, 112, 100, 103, 99]]
b2 = {}
b3 = {}
b4 = 0;
def fonk1(b18):
    b5 = np.zeros((8, 8))
    b6 = np.zeros((8, 8))
    for i in range(8):
        for b15 in range(8):
            b6[i][b15] = b18[i][b15] - 128
    b7 = scipy.fftpack.dct(scipy.fftpack.dct(b6, axis=0, norm='ortho'), axis=1, norm='ortho')
    for i in range(8):
        for b15 in range(8):
            b5[i][b15] = np.fix(b7[i][b15] / b1[i][b15])
    return b5
def fonk2(b8):
    global b4
    a1 = 0
    b8 = np.array(b8)
    a2 = 8
    a3 = 8
    b9 = np.zeros((1, 64))
    b10 = np.zeros((1, 64))
    b11 = np.zeros((1, 64))
    b12 = [[] for i in range(a2 + a3 - 1)]
    for i in range(a2):
        for b15 in range(a3):
            b13 = i + b15
            if(b13 % b14 = = 0):
                b12[b13].insert(0, b8[i][b15])
            else:
                b12[b13].append(b8[i][b15])
    b12.reverse()
    for i in b12:
        for b15 in i:
            if b15 = = -0.0:
                b15 = abs(b15)
                b9[0, a1] = b15
            else:
                b9[0, a1] = b15
            a1 = a1 + 1
    a4 = 0
    for i in range(0, 64):
        if(b9[0, i] != 0):
            a4 = i
            break
    for i in range(a4, 64):
        b2[b4] = b9[0, i]
        if b9[0, i] in b3:
            pass
        else:
            b3[b9[0, i]] = b9[0, i]
        b4 = b4 + 1
def fonk3(dic, b23):
    a5 = 0
    b16 = open("result.txt", "w")
    for i in b26:
        b16.write(str(b23[a5]) + "\t" + str(dic.get(i, i)) + "\n")
        a5 += 1
b8 = Image.open("lena.jpg")
b8.show()
b8 = b8.convert('L')
b8.save("gray.jpg")
b8.show()
alto, b17 = b8.size
b18 = np.asarray(b8, dtype=np.float32)
b19 = b18
b19 = b19 - 128
Image.fromarray(b19.astype(np.uint8)).save("restada.jpg")
b20 = Image.open("restada.jpg")
b20.show()
b21 = np.zeros((256, 256))
for i in range(0, alto, 8):
    for b15 in range(0, b17, 8):
        b21[i:(i+8), b15:(b15+8)] = fonk1(b18[i:(i+8), b15:(b15+8)])
Image.fromarray(b21.astype(np.uint8)).save("dct.jpg")
b20 = Image.open("dct.jpg")
b20.show()
for i in range(0, alto, 8):
    for b15 in range(0, b17, 8):
        fonk2(b21[i:(i+8), b15:(b15+8)])
b22 = open("dct.txt", "w")
for i in range(0, alto):
    for b15 in range(0, b17):
        if b21[i, b15] == -0.0:
            b22.write(str(abs(b21[i, b15])) + " ")
        else:
            b22.write(str(b21[i, b15]) + " ")
    b22.write("\n")
b23 = list(b3.b23())
b24 = list(b2.values())
b25 = len(b23)
b26 = {}
for i in b23:
    b27 = float(b24.count(i))
    b26[i] = b27 / float(len(b24))
fonk3(b26, b23)
print("Se ha realizado exitosamente el procesamiento de la imagen.\nSe ha generado un archivo de b26.\nSe ha generado el archivo de texto que contiene la matriz resultante del procesamiento de JPEG.")