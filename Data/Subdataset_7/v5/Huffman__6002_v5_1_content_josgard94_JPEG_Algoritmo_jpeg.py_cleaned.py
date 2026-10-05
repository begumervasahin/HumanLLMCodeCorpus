
import numpy as np
from PIL import Image
from scipy.fftpack import dct
b1 = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])
b2 = {}
b3 = {}
def fonk1(a):
    b4 = a - 128
    b5 = dct(dct(b4, axis=0, norm='ortho'), axis=1, norm='ortho')
    return np.fix(b5 / b1)
def fonk2(matrix):
    global b2
    a1 = 0
    rows, b6 = 8, 8
    b7 = np.zeros((1, 64))
    b8 = [[] for _ in range(rows + b6 - 1)]
    for i in range(rows):
        for b11 in range(b6):
            b9 = i + b11
            if b9 % b10 = = 0:
                b8[b9].insert(0, matrix[i][b11])
            else:
                b8[b9].append(matrix[i][b11])
    b8.reverse()
    for i in b8:
        for b11 in i:
            if b11 = = -0.0:
                b11 = abs(b11)
                b7[0, a1] = b11
            else:
                b7[0, a1] = b11
            a1 += 1
    b12 = next((i for i, value in enumerate(b7[0]) if value != 0), None)
    for i in range(b12, 64):
        b2[a1] = b7[0, i]
        b3[b7[0, i]] = b7[0, i]
        a1 += 1
b13 = Image.open("lena.jpg").convert('L')
b13.show()
b14 = np.asarray(b13, dtype=np.float32)
b15 = b14 - 128
Image.fromarray(b15.astype(np.uint8)).save("restada.jpg")
b16 = Image.open("restada.jpg")
b16.show()
b17 = np.zeros((256, 256))
for i in range(0, b14.shape[0], 8):
    for b11 in range(0, b14.shape[1], 8):
        b17[i:(i + 8), b11:(b11 + 8)] = fonk1(b14[i:(i + 8), b11:(b11 + 8)])
        fonk2(b17[i:(i + 8), b11:(b11 + 8)])
np.savetxt("dct.txt", b17)
b18 = list(b2.values())
b19 = {i: float(b18.count(i)) / len(b18) for i in b3}
with open("result.txt", "w") as file:
    for key in b3:
        file.write(f"{key}\t{b19.get(key, key)}\n")
print("Image processing and probability computation completed successfully.")
print("A file of probabilities has been generated.")
print("The text file containing the result of JPEG processing has been generated.")