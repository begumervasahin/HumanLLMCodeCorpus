import sys, os
import numpy as np
import glob
from matplotlib import pylab as plt
from numpy.linalg import svd
from PIL import Image
import time
class b15:
    def fonk1(self, b9, b10, b14, b12, b13):
        a1 = 1e-8
        b1 = np.max(b12 - b9) < a1
        b2 = np.max(b13 - b10) < a1
        b3 = np.max(b12 + b13 - b14) < a1
        return b1 and b2 and b3
    def fonk2(self, b14, tau):
        b4 = np.sign(b14) * (abs(b14) - tau) * (np.sign(abs(b14) - tau) + 1)/ 2
        return b4
    def fonk3(self, b14, tau):
        u, s, b5 = svd(b14, full_matrices = False)
        b6 = self.fonk2(s, tau)
        return np.dot(np.dot(u, np.diag(b6)), b5)
    def fonk4(self, b14):
        m, b7 = b14.shape
        a2 = 1.5
        a3 = 1e-3
        a4 = 1e10
        a5 = 1000
        b8 = 1/np.sqrt(max(m, b7))
        b9 = np.zeros((m, b7), float)
        b10 = np.zeros((m, b7), float)
        b11 = np.zeros((m, b7), float)
        a6 = 0
        while True:
            a6 += 1
            b12 = self.fonk3(b14 - b10 - (1/a3) * b11, 1/a3)
            b13 = self.fonk2(b14 - b12 - (1/a3) * b11, b8/a3)
            b11 += a3 * (b12 + b13 - b14)
            a3 = min(a2 * a3, a4)
            if self.fonk1(b9, b10, b14, b12, b13) or a6 >= a5:
                return b12, b13
            else:
                b9, b10 = b12, b13
                print(np.max(b14 - b9 - b10))
b14 = np.array(Image.open('set your path').convert('b9'))
b15 = b15()
b9, b16 = b15.fonk4(b14)
plt.subplot(131)
plt.imshow(b9)
plt.gray()
plt.subplot(132)
plt.imshow(b16)
plt.gray()
plt.subplot(133)
plt.imshow(b14)
plt.gray()
plt.show()