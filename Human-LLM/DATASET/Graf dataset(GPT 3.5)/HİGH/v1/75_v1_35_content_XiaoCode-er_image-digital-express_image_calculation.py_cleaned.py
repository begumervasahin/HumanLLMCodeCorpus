import math
import numpy as np
from skimage import io
class class1(object):
    def fonk1(self, b14):
        self.b1 = b14
    def fonk2(self):
        a1 = 0
        a2 = 0
        b2 = io.imread(self.b1, as_gray=True)
        b3 = len(b2)
        b4 = len(b2[0])
        for i in range(b3):
            for n in range(b4):
                a1 += b2[i][n]
        b5 = a1 / (b3 * b4)
        for a in range(b3):
            for b in range(b4):
                a2 += (b2[a][b] - b5) ** 2
        b6 = math.sqrt(a2 / (b3 * b4))
        return b5, b6
    def fonk3(self):
        b2 = io.imread(self.b1, as_gray=True)
        b7 = b2.size
        b8 = np.histogram(b2, bins=256)[0] / b7
        b9 = list(b8)
        b10 = b9.count(0)
        b9 = [x for x in b9 if x != 0]
        b11 = len(b9)
        a3 = 0
        for k in range(b11):
            a3 += b9[k] * math.log(b9[k], 2)
        b12 = -a3
        return b12
if b13 = = "__main__":
    b14 = "path_to_your_image.jpg"
    b15 = class1(b14)
    b5, b6 = b15.fonk2()
    b16 = b15.fonk3()
    print("Mean:", b5)
    print("Variance:", b6)
    print("Entropy:", b16)