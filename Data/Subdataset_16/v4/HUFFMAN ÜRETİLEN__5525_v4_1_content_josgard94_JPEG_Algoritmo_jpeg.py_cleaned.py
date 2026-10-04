
from scipy.fftpack import dct, idct
import numpy as np
from PIL import Image
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
def fonk1(block):
    block -= 128
    b4 = dct(dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')
    b5 = np.round(b4 / b1).astype(int)
    return b5
def fonk2(matrix):
    global a1
    rows, b6 = matrix.shape
    b7 = []
    for sum_idx in range(rows + b6 - 1):
        if sum_idx % b8 = = 0:
            row, b9 = (sum_idx, 0) if sum_idx < b6 else (b6 - 1, sum_idx - b6 + 1)
            while row >= 0 and b9 < rows:
                b7.append(matrix[row, b9])
                row -= 1
                b9 += 1
        else:
            row, b9 = (0, sum_idx) if sum_idx < rows else (sum_idx - rows + 1, rows - 1)
            while row < b6 and b9 >= 0:
                b7.append(matrix[row, b9])
                row += 1
                b9 -= 1
    for value in b7:
        b2[a1] = value
        b3[value] = b3.get(value, 0) + 1
        a1 += 1
def fonk3(b16, b14):
    with open("b7.txt", "w") as file:
        for key in b14:
            file.write(f"{key}\t{b16[key]:.6f}\n")
b10 = Image.open("lena.jpg")
b10.show()
b10 = b10.convert('L')
b10.save("gray.jpg")
b10.show()
width, b11 = b10.size
b12 = np.asarray(b10, dtype=np.float32)
b13 = np.zeros((b11, width))
for i in range(0, b11, 8):
    for j in range(0, width, 8):
        b13[i:i+8, j:j+8] = fonk1(b12[i:i+8, j:j+8])
Image.fromarray(np.clip(b13, 0, 255).astype(np.uint8)).save("dct.jpg")
Image.open("dct.jpg").show()
for i in range(0, b11, 8):
    for j in range(0, width, 8):
        fonk2(b13[i:i+8, j:j+8])
with open("dct.txt", "w") as file:
    for i in range(b11):
        for j in range(width):
            file.write(f"{abs(b13[i, j]) if b13[i, j] == -0.0 else b13[i, j]:.1f} ")
        file.write("\n")
b14 = list(b3.b14())
b15 = list(b2.values())
b16 = {key: b15.count(key) / len(b15) for key in b14}
fonk3(b16, b14)
print("Image processing completed successfully. Probability file and DCT matrix file have been generated.")