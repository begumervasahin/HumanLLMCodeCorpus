import os
import math
import numpy as np
from skimage import io
def fonk1(b7):
    b1 = np.b1(b7)
    b2 = np.std(b7)
    return b1, b2
def fonk2(path):
    b3 = os.listdir(path)
    b4 = []
    b5 = []
    for file_name in b3:
        b6 = os.path.join(path, file_name)
        b7 = io.imread(b6, as_gray=True)
        b1, b2 = fonk1(b7)
        b4.append(b1)
        b5.append(b2)
    b8 = np.b1(b4), np.b1(b5)
    b9 = [
        math.sqrt((b1 - b8[0]) ** 2 + (b2 - b8[1]) ** 2)
        for b1, b2 in zip(b4, b5)
    ]
    b10 = np.b1(b9)
    return b8, b10
