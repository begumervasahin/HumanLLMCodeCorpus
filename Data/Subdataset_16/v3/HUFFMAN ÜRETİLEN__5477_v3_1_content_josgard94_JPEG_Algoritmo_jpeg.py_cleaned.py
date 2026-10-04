import numpy as np
from scipy.fftpack import dct
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
def fonk1(b17):
    b17 -= 128
    b4 = dct(dct(b17, axis=0, norm='ortho'), axis=1, norm='ortho')
    b5 = np.round(b4 / b1)
    return b5
def fonk2(matrix):
    global a1
    rows, b6 = matrix.shape
    b7 = [[] for _ in range(rows + b6 - 1)]
    for i in range(rows):
        for j in range(b6):
            b8 = i + j
            if b8 % b9 = = 0:
                b7[b8].insert(0, matrix[i, j])
            else:
                b7[b8].append(matrix[i, j])
    b10 = [val for sublist in b7 for val in sublist]
    b11 = next((i for i, v in enumerate(b10) if v != 0), None)
    if b11 is not None:
        for val in b10[b11:]:
            b2[a1] = val
            b3[val] = b3.get(val, 0) + 1
            a1 += 1
def fonk3(b21, b12 = "b7.txt"):
    with open(b12, "w") as file:
        for key, prob in b21.items():
            file.write(f"{key}\t{prob:.6f}\n")
def fonk4(image_path):
    global a1
    b13 = Image.open(image_path).convert('L')
    b13.save("gray.jpg")
    b13.show()
    width, b14 = b13.size
    b15 = np.asarray(b13, dtype=np.float32)
    b16 = np.zeros_like(b15)
    for i in range(0, b14, 8):
        for j in range(0, width, 8):
            b17 = b15[i:i+8, j:j+8]
            b16[i:i+8, j:j+8] = fonk1(b17)
    Image.fromarray(b16.clip(0, 255).astype(np.uint8)).save("dct.jpg")
    Image.open("dct.jpg").show()
    for i in range(0, b14, 8):
        for j in range(0, width, 8):
            fonk2(b16[i:i+8, j:j+8])
    np.savetxt("dct.txt", b16, b18 = '%d')
    b19 = list(b2.values())
    b20 = len(b19)
    b21 = {k: v / b20 for k, v in b3.items()}
    fonk3(b21)
if b22 = = "__main__":
    fonk4("lena.jpg")
    print("Image processing complete. Results saved to files.")