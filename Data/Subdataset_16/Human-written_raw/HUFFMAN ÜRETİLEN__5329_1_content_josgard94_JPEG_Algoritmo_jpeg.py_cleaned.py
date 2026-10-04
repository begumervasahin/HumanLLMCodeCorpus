
from scipy.fftpack import dct,idct
import scipy
import numpy as np
from PIL import Image, ImageDraw,ImageFont
import os
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
def fonk1(b21):
    b5 = np.zeros((8,8));
    b6 = np.zeros((8,8));
    for i in range(8):
        for b16 in range(8):
            b6[i][b16] = b21[i][b16] - 128;
    b7 = scipy.fftpack.dct( scipy.fftpack.dct( b6, axis=0, norm='ortho' ), axis=1, norm='ortho' )
    for i in range(8):
        for b16 in range(8):
            b5[i][b16] = np.fix(b7[i][b16]/b1[i][b16])
    return b5
def fonk2(b8):
    global b4
    a1 = 0
    b8 = np.array(b8)
    a2 = 8
    a3 = 8
    b9 = np.zeros((1,64))
    b10 = np.zeros((1,64))
    b11 = np.zeros((1,64))
    b12 = [[] for i in range(a2+a3-1)]
    for i in range(a2):
        for b16 in range(a3):
            b13 = i+b16
            if(b13%b14 = =0):
                b12[b13].insert(0,b8[i][b16])
            else:
                b12[b13].append(b8[i][b16])
    b15 = b12.reverse()
    for i in b12:
        for b16 in i:
            if b16 = = -0.0:
                b16 = abs(b16)
                b9[0,a1] = b16
            else:
                b9[0,a1] = b16
            a1 = a1 + 1;
    b17 = 0;
    for i in range(0,64):
        if(b9[0,i]!= 0):
            b17 = i
            break
    for i in range(b17,64):
        b2[b4] = b9[0,i];
        if b9[0,i] in b3:
            pass
        else:
            b3[b9[0,i]] = b9[0,i]
        b4 = b4+1
def fonk3(dic,b26):
    b18 = 0;
    b19 = open("result.txt","w")
    for i in b29:
        b19.write(str(b26[b18]) +"\t"+ str(dic.get(i,i))+"\n");
        b18+= 1
b8 = Image.open("lena.jpg")
b8.show()
b8 = b8.convert('L')
b8.save("gray.jpg")
b8.show()
alto, b20 = b8.size
b21 = np.asarray(b8,dtype=np.float32)
b22 = b21;
b22 = b22 - 128;
Image.fromarray(b22.astype(np.uint8)).save("restada.jpg")
b23 = Image.open("restada.jpg");
b23.show()
b24 = np.zeros((256,256))
for i in range(0,alto,8):
    for b16 in range(0,b20,8):
        b24[i:(i+8),b16:(b16+8)] = fonk1(b21[i:(i+8),b16:(b16+8)])
Image.fromarray(b24.astype(np.uint8)).save("dct.jpg")
b23 = Image.open("dct.jpg");
b23.show()
for i in range(0,alto,8):
        for b16 in range(0,b20,8):
            fonk2(b24[i:(i+8),b16:(b16+8)])
b25 = open("dct.txt","w")
for i in range(0,alto):
    for b16 in range(0,b20):
        if b24[i,b16] == -0.0:
            b25.write(str(abs(b24[i,b16]))+" ")
        else:
            b25.write(str(b24[i,b16])+" ")
    b25.write("\n")
b26 = list(b3.b26())
b27 = list(b2.values())
b28 = len(b26)
b29 = {}
for i in b26:
    b30 = float(b27.count(i));
    b29[i] = b30/float(len(b27));
fonk3(b29,b26)
print("Se b21 realizado exitosamente el procesamiento de la imagen. \n Se ha generado un archivo de b29.\n Se ha generado el archivo de texto que contiene la matriz resultante del procesamiento de JPEG")