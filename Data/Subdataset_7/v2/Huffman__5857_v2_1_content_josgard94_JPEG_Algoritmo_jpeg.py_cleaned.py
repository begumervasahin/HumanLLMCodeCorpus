import re
import numpy as np
import scipy.fftpack
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
a1 = 0
def fonk1(b18):
    b4 = np.zeros((8, 8))
    b5 = np.zeros((8, 8))
    for i in range(8):
        for b15 in range(8):
            b5[i][b15] = b18[i][b15] - 128
    b6 = scipy.fftpack.dct(scipy.fftpack.dct(b5, axis=0, norm='ortho'), axis=1, norm='ortho')
    for i in range(8):
        for b15 in range(8):
            b4[i][b15] = np.fix(b6[i][b15] / b1[i][b15])
    return b4
def fonk2(b7):
    global a1
    a2 = 0
    b7 = np.array(b7)
    rows, b8 = 8, 8
    b9 = np.zeros((1, 64))
    b10 = np.zeros((1, 64))
    b11 = np.zeros((1, 64))
    b12 = [[] for i in range(rows + b8 - 1)]
    for i in range(rows):
        for b15 in range(b8):
            b13 = i + b15
            if(b13 % b14 = = 0):
                b12[b13].insert(0, b7[i][b15])
            else:
                b12[b13].append(b7[i][b15])
    b12.reverse()
    for i in b12:
        for b15 in i:
            if b15 = = -0.0:
                b15 = abs(b15)
                b9[0, a2] = b15
            else:
                b9[0, a2] = b15
            a2 = a2 + 1
    a3 = 0
    for i in range(0, 64):
        if(b9[0, i] != 0):
            a3 = i
            break
    for i in range(a3, 64):
        b2[a1] = b9[0, i]
        if b9[0, i] in b3:
            pass
        else:
            b3[b9[0, i]] = b9[0, i]
        a1 = a1 + 1
def fonk3(dic, b23):
    a4 = 0
    b16 = open("result.txt", "w")
    for i in b26:
        b16.write(str(b23[a4]) + "\t" + str(dic.get(i, i)) + "\n")
        a4 += 1
b7 = Image.open("lena.jpg")
b7.show()
b7 = b7.convert('L')
b7.save("gray.jpg")
b7.show()
alto, b17 = b7.size
b18 = np.asarray(b7, dtype=np.float32)
b19 = b18 - 128
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
print("Procesamiento de la imagen completado exitosamente.")
print("Se ha generado un archivo de b26 b11 un archivo de texto que contiene la matriz resultante del procesamiento de JPEG.")