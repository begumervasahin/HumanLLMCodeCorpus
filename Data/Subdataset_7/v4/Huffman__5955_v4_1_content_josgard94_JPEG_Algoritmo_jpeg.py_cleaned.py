
from scipy.fftpack import dct
import scipy
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import matplotlib.pyplot as plt
b1 = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
]
b2 = {}
b3 = {}
a1 = 0
def fonk1(b14):
    b4 = np.zeros((8, 8))
    b5 = np.zeros((8, 8))
    for i in range(8):
        for b12 in range(8):
            b5[i][b12] = b14[i][b12] - 128
    b6 = scipy.fftpack.dct(scipy.fftpack.dct(b5, axis=0, norm='ortho'), axis=1, norm='ortho')
    for i in range(8):
        for b12 in range(8):
            b4[i][b12] = np.fix(b6[i][b12] / b1[i][b12])
    return b4
def fonk2(b7):
    global a1
    a2 = 0
    b7 = np.array(b7)
    a3 = 8
    a4 = 8
    b8 = np.zeros((1, 64))
    b9 = [[] for i in range(a3 + a4 - 1)]
    for i in range(a3):
        for b12 in range(a4):
            b10 = i + b12
            if b10 % b11 = = 0:
                b9[b10].insert(0, b7[i][b12])
            else:
                b9[b10].append(b7[i][b12])
    b9.reverse()
    for i in b9:
        for b12 in i:
            if b12 = = -0.0:
                b12 = abs(b12)
                b8[0, a2] = b12
            else:
                b8[0, a2] = b12
            a2 += 1
    a5 = 0
    for i in range(0, 64):
        if b8[0, i] != 0:
            a5 = i
            break
    for i in range(a5, 64):
        b2[a1] = b8[0, i]
        if b8[0, i] in b3:
            pass
        else:
            b3[b8[0, i]] = b8[0, i]
        a1 += 1
def fonk3(dic, b18):
    a6 = 0
    with open("result.txt", "w") as file:
        for i in b20:
            file.write(str(b18[a6]) + "\t" + str(dic.get(i, i)) + "\n")
            a6 += 1
b7 = Image.open("lena.jpg")
b7.show()
b7 = b7.convert('L')
b7.save("gray.jpg")
b7.show()
alto, b13 = b7.size
b14 = np.asarray(b7, dtype=np.float32)
b15 = b14 - 128
Image.fromarray(b15.astype(np.uint8)).save("restada.jpg")
b16 = Image.open("restada.jpg")
b16.show()
b17 = np.zeros((256, 256))
for i in range(0, alto, 8):
    for b12 in range(0, b13, 8):
        b17[i:(i + 8), b12:(b12 + 8)] = fonk1(b14[i:(i + 8), b12:(b12 + 8)])
Image.fromarray(b17.astype(np.uint8)).save("dct.jpg")
b16 = Image.open("dct.jpg")
b16.show()
for i in range(0, alto, 8):
    for b12 in range(0, b13, 8):
        fonk2(b17[i:(i + 8), b12:(b12 + 8)])
with open("dct.txt", "w") as f:
    for i in range(0, alto):
        for b12 in range(0, b13):
            if b17[i, b12] == -0.0:
                f.write(str(abs(b17[i, b12])) + " ")
            else:
                f.write(str(b17[i, b12]) + " ")
        f.write("\n")
b18 = list(b3.b18())
b19 = list(b2.values())
b20 = {}
for i in b18:
    b21 = float(b19.count(i))
    b20[i] = b21 / float(len(b19))
fonk3(b20, b18)
print("Image processing and probability computation completed successfully.")
print("A file of probabilities has been generated.")
print("The text file containing the result of JPEG processing has been generated.")