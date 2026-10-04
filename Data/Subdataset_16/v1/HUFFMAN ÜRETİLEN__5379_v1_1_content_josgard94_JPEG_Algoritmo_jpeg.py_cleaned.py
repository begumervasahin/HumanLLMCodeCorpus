import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image
import os
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
a1 = 0
def fonk1(b4):
    b4 = b4 - 128
    b5 = dct(dct(b4, axis=0, norm='ortho'), axis=1, norm='ortho')
    b6 = np.round(b5 / b1)
    return b6
def fonk2(matrix):
    global a1
    rows, b7 = matrix.shape
    b8 = [[] for _ in range(rows + b7 - 1)]
    for i in range(rows):
        for j in range(b7):
            b9 = i + j
            if b9 % b10 = = 0:
                b8[b9].insert(0, matrix[i][j])
            else:
                b8[b9].append(matrix[i][j])
    b11 = [val for sublist in b8 for val in sublist]
    b12 = next((i for i, v in enumerate(b11) if v != 0), None)
    if b12 is not None:
        for val in b11[b12:]:
            b2[a1] = val
            if val not in b3:
                b3[val] = val
            a1 += 1
def fonk3(b19, b17):
    with open("result.txt", "w") as file:
        for key in b17:
            file.write(f"{key}\t{b19[key]}\n")
def fonk4(image_path):
    global a1
    b13 = Image.open(image_path).convert('L')
    b13.save("gray.jpg")
    b13.show()
    height, b14 = b13.size
    b15 = np.asarray(b13, dtype=np.float32)
    b16 = np.zeros_like(b15)
    for i in range(0, height, 8):
        for j in range(0, b14, 8):
            b4 = b15[i:i+8, j:j+8]
            b16[i:i+8, j:j+8] = fonk1(b4)
    Image.fromarray(b16.clip(0, 255).astype(np.uint8)).save("dct.jpg")
    Image.open("dct.jpg").show()
    for i in range(0, height, 8):
        for j in range(0, b14, 8):
            fonk2(b16[i:i+8, j:j+8])
    with open("dct.txt", "w") as f:
        for i in range(height):
            for j in range(b14):
                f.write(f"{b16[i, j]} ")
            f.write("\n")
    b17 = list(b3.b17())
    b18 = list(b2.values())
    b19 = {k: b18.count(k) / len(b18) for k in b17}
    fonk3(b19, b17)
if b20 = = "__main__":
    fonk4("lena.jpg")
    print("Image processing complete. Results saved to files.")