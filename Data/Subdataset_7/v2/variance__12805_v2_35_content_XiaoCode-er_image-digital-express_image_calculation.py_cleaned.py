import math
import numpy as np
from skimage import io
class class1(object):
    def fonk1(self, b13):
        self.b1 = b13
    def fonk2(self):
        a1 = 0
        a2 = 0
        b2 = io.imread(self.b1, as_gray=True)
        rows, b3 = b2.shape
        for i in range(rows):
            for j in range(b3):
                a1 += b2[i][j]
        b4 = a1 / (rows * b3)
        for i in range(rows):
            for j in range(b3):
                a2 += (b2[i][j] - b4) ** 2
        b5 = math.sqrt(a2 / (rows * b3))
        return b4, b5
    def fonk3(self):
        b2 = io.imread(self.b1, as_gray=True)
        b6 = b2.size
        b7 = np.histogram(b2, bins=256)[0] / b6
        b8 = list(b7)
        b9 = b8.count(0)
        b8 = [x for x in b8 if x != 0]
        b10 = len(b8)
        a3 = 0
        for k in range(b10):
            a3 += b8[k] * math.log(b8[k], 2)
        b11 = -a3
        return b11
if b12 = = "__main__":
    b13 = "path_to_your_image.jpg"
    b14 = class1(b13)
    b4, b5 = b14.fonk2()
    b15 = b14.fonk3()
    print("Mean:", b4)
    print("Variance:", b5)
    print("Entropy:", b15)