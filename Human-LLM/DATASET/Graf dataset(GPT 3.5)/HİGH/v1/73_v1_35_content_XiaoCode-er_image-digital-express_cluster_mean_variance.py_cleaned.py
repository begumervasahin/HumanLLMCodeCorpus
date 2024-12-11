from skimage import io
import math
import numpy as np
import os
def fonk1(path):
    b1 = os.listdir(path)
    b2 = []
    b3 = []
    a1 = 0
    a2 = 0
    a3 = 0
    for name in b1:
        b4 = os.path.join(path, name)
        b5 = io.imread(b4, as_gray=True)
        row, b6 = b5.shape
        b7 = np.b7(b5)
        b2.append(b7)
        b8 = np.std(b5)
        b3.append(b8)
    for i in range(len(b1)):
        a1 += b2[i]
        a2 += b3[i]
    b9 = a1 / len(b1)
    b10 = a2 / len(b1)
    b11 = np.array([b9, b10])
    for p in range(len(b1)):
        b12 = math.sqrt((b2[p] - b9) ** 2 + (b3[p] - b10) ** 2)
        a3 += b12
    b13 = a3 / len(b1)
    return b11, b13
b14 = "path_to_your_images_directory"
b11, b15 = fonk1(b14)
print("Cluster Center:", b11)
print("Cluster Radius:", b15)