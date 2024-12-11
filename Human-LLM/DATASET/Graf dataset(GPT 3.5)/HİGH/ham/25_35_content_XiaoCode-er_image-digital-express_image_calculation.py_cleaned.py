from skimage import io
import math
import numpy as np
class class1(object):
    def fonk1(self, image_path):
        self.b1 = image_path
    def fonk2(self):
        a1 = 0
        a2 = 0
        b2 = io.imread(self.b1, as_grey=True)
        b3 = len(b2)
        b4 = len(b2[0])
        for i in range(b4):
            for n in range(b4):
                a1 += b2[i][n]
        b5 = a1 / (b3*b4)
        for a in range(b3):
            for b in range(b4):
                a2 += (b2[a][b] - b5) ** 2
        b6 = math.sqrt(a2 / (b3 * b4))
        return b5, b6
    def fonk3(self):
        b2 = io.imread(self.b1, as_grey=True)
        b7 = b2.size
        b8 = np.histogram(b2, bins=256)[0] / b7
        b9 = list(b8)
        a3 = 0
        for i in range(len(b9)):
            if b9[i] == 0:
                a3 += 1
        for n in range(a3):
            b9.remove(0)
        b10 = len(b9)
        a4 = 0
        for k in range(b10):
            a4 += b9[k] * math.log(b9[k], 2)
        b11 = -a4
        return b11