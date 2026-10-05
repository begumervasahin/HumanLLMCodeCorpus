import re
import numpy as np
import scipy.fftpack
from PIL import Image
import matplotlib.pyplot as plt
b1 = np.b11([[16, 11, 10, 16, 24, 40, 51, 61],
                                [12, 12, 14, 19, 26, 58, 60, 55],
                                [14, 13, 16, 24, 40, 57, 69, 56],
                                [14, 17, 22, 29, 51, 87, 80, 62],
                                [18, 22, 37, 56, 68, 109, 103, 77],
                                [24, 35, 55, 64, 81, 104, 113, 92],
                                [49, 64, 78, 87, 103, 121, 120, 101],
                                [72, 92, 95, 98, 112, 100, 103, 99]])
b2 = {}
b3 = {}
a1 = 0
def fonk1(matrix):
    b4 = matrix - 128
    b5 = scipy.fftpack.dct(scipy.fftpack.dct(b4, axis=0, norm='ortho'), axis=1, norm='ortho')
    b6 = np.round(b5 / b1)
    return b6
def fonk2(matrix):
    global a1
    b7 = []
    for i in range(8):
        for j in range(8):
            b7.append(matrix[i][j])
    b7 = list(filter(lambda x: x != -0.0, b7))
    for b16 in b7:
        b2[a1] = b16
        if b16 not in b3:
            b3[b16] = b16
        a1 += 1
def fonk3(b19, b17):
    with open("result.txt", "w") as file:
        for key in b17:
            file.write(f"{key}\t{b19.get(key, key)}\n")
b8 = Image.open("lena.jpg")
b8.show()
b9 = b8.convert('L')
b9.save("gray.jpg")
b9.show()
width, b10 = b9.size
b11 = np.asarray(b9, dtype=np.float32)
b12 = b11 - 128
Image.fromarray(b12.astype(np.uint8)).save("restada.jpg")
b13 = Image.open("restada.jpg")
b13.show()
b14 = np.zeros((256, 256))
for i in range(0, width, 8):
    for j in range(0, b10, 8):
        b14[i:(i+8), j:(j+8)] = fonk1(b11[i:(i+8), j:(j+8)])
Image.fromarray(b14.astype(np.uint8)).save("dct.jpg")
b15 = Image.open("dct.jpg")
b15.show()
for i in range(0, width, 8):
    for j in range(0, b10, 8):
        fonk2(b14[i:(i+8), j:(j+8)])
with open("dct.txt", "w") as f:
    for row in b14:
        for b16 in row:
            f.write(str(abs(b16)) + " " if b16 = = -0.0 else str(b16) + " ")
        f.write("\n")
b17 = list(b3.b17())
b18 = list(b2.values())
b19 = {key: b18.count(key) / len(b18) for key in b17}
fonk3(b19, b17)
print("Image processing completed successfully.")
print("A b19 file and a text file containing the processed JPEG matrix have been generated.")