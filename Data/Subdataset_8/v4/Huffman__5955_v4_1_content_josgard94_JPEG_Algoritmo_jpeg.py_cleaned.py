
from scipy.fftpack import dct
import scipy
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import matplotlib.pyplot as plt
Z = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
]
temporal = {}
frecuencia = {}
g = 0
def dct2(a):
    new_matrix = np.zeros((8, 8))
    b = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            b[i][j] = a[i][j] - 128
    c = scipy.fftpack.dct(scipy.fftpack.dct(b, axis=0, norm='ortho'), axis=1, norm='ortho')
    for i in range(8):
        for j in range(8):
            new_matrix[i][j] = np.fix(c[i][j] / Z[i][j])
    return new_matrix
def zigzag(matrix):
    global g
    con = 0
    matrix = np.array(matrix)
    rows = 8
    columns = 8
    aux = np.zeros((1, 64))
    solution = [[] for i in range(rows + columns - 1)]
    for i in range(rows):
        for j in range(columns):
            sum_ij = i + j
            if sum_ij % 2 == 0:
                solution[sum_ij].insert(0, matrix[i][j])
            else:
                solution[sum_ij].append(matrix[i][j])
    solution.reverse()
    for i in solution:
        for j in i:
            if j == -0.0:
                j = abs(j)
                aux[0, con] = j
            else:
                aux[0, con] = j
            con += 1
    indice = 0
    for i in range(0, 64):
        if aux[0, i] != 0:
            indice = i
            break
    for i in range(indice, 64):
        temporal[g] = aux[0, i]
        if aux[0, i] in frecuencia:
            pass
        else:
            frecuencia[aux[0, i]] = aux[0, i]
        g += 1
def save_probabilities(dic, keys):
    pos = 0
    with open("result.txt", "w") as file:
        for i in probabilidades:
            file.write(str(keys[pos]) + "\t" + str(dic.get(i, i)) + "\n")
            pos += 1
matrix = Image.open("lena.jpg")
matrix.show()
matrix = matrix.convert('L')
matrix.save("gray.jpg")
matrix.show()
alto, ancho = matrix.size
a = np.asarray(matrix, dtype=np.float32)
alternativo = a - 128
Image.fromarray(alternativo.astype(np.uint8)).save("restada.jpg")
I = Image.open("restada.jpg")
I.show()
im2 = np.zeros((256, 256))
for i in range(0, alto, 8):
    for j in range(0, ancho, 8):
        im2[i:(i + 8), j:(j + 8)] = dct2(a[i:(i + 8), j:(j + 8)])
Image.fromarray(im2.astype(np.uint8)).save("dct.jpg")
I = Image.open("dct.jpg")
I.show()
for i in range(0, alto, 8):
    for j in range(0, ancho, 8):
        zigzag(im2[i:(i + 8), j:(j + 8)])
with open("dct.txt", "w") as f:
    for i in range(0, alto):
        for j in range(0, ancho):
            if im2[i, j] == -0.0:
                f.write(str(abs(im2[i, j])) + " ")
            else:
                f.write(str(im2[i, j]) + " ")
        f.write("\n")
keys = list(frecuencia.keys())
elementos = list(temporal.values())
probabilidades = {}
for i in keys:
    telemento = float(elementos.count(i))
    probabilidades[i] = telemento / float(len(elementos))
save_probabilities(probabilidades, keys)
print("Image processing and probability computation completed successfully.")
print("A file of probabilities has been generated.")
print("The text file containing the result of JPEG processing has been generated.")