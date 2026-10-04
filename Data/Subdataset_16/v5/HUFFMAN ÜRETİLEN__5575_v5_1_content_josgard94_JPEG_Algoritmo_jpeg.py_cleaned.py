
from scipy.fftpack import dct, idct
import numpy as np
from PIL import Image
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
    for b16 in b7:
        b2[a1] = b16
        b3[b16] = b3.get(b16, 0) + 1
        a1 += 1
def fonk3(b19, b17, b10 = "b7.txt"):
    with open(b10, "w") as file:
        for key in b17:
            file.write(f"{key}\t{b19[key]:.6f}\n")
def fonk4(image_path):
    b11 = Image.open(image_path).convert('L')
    b11.save("gray.jpg")
    width, b12 = b11.size
    b13 = np.asarray(b11, dtype=np.float32)
    b14 = np.zeros((b12, width))
    for i in range(0, b12, 8):
        for j in range(0, width, 8):
            b14[i:i+8, j:j+8] = fonk1(b13[i:i+8, j:j+8])
    b15 = Image.fromarray(np.clip(b14, 0, 255).astype(np.uint8))
    b15.save("dct.jpg")
    for i in range(0, b12, 8):
        for j in range(0, width, 8):
            fonk2(b14[i:i+8, j:j+8])
    with open("dct.txt", "w") as file:
        for row in b14:
            file.write(" ".join(f"{abs(b16) if b16 = = -0.0 else b16:.1f}" for b16 in row) + "\n")
    b17 = list(b3.b17())
    b18 = list(b2.values())
    b19 = {key: b18.count(key) / len(b18) for key in b17}
    fonk3(b19, b17)
    print("Image processing completed successfully. Probability file and DCT matrix file have been generated.")
