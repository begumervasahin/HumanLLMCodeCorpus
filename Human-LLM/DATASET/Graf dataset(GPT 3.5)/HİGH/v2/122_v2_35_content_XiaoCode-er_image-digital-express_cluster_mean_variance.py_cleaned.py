from skimage import io
import math
import numpy as np
import os
def fonk1(path):
    b1 = os.listdir(path)
    b2 = []
    b3 = []
    for filename in b1:
        b4 = os.path.join(path, filename)
        b5 = io.imread(b4, as_gray=True)
        b6 = np.mean(b5)
        b7 = np.std(b5)
        b2.append(b6)
        b3.append(b7)
    return b2, b3
def fonk2(b2, b3):
    b8 = np.mean(b2)
    b9 = np.mean(b3)
    return b8, b9
def fonk3(b2, b3, b11):
    b10 = sum(math.sqrt((m - b11[0]) ** 2 + (v - b11[1]) ** 2)
                         for m, v in zip(b2, b3))
    return b10 / len(b2)
def fonk4(path):
    b2, b3 = fonk1(path)
    b11 = fonk2(b2, b3)
    b12 = fonk3(b2, b3, b11)
    return b11, b12
b13 = "path_to_your_images_directory"
b11, b12 = fonk4(b13)
print("Cluster Center:", b11)
print("Cluster Radius:", b12)