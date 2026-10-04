import numpy as np
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b8, b9, b14, b11, b12):
        a1 = 1e-8
        b1 = np.max(np.abs(b11 - b8)) < a1
        b2 = np.max(np.abs(b12 - b9)) < a1
        b3 = np.max(np.abs(b11 + b12 - b14)) < a1
        return b1 and b2 and b3
    def fonk2(self, b14, tau):
        return np.sign(b14) * np.maximum(np.abs(b14) - tau, 0)
    def fonk3(self, b14, tau):
        u, s, b4 = svd(b14, full_matrices=False)
        b5 = self.fonk2(s, tau)
        return np.dot(u, np.dot(np.diag(b5), b4))
    def fonk4(self, b14):
        m, b6 = b14.shape
        a2 = 1.5
        a3 = 1e-3
        a4 = 1e10
        a5 = 1000
        b7 = 1 / np.sqrt(max(m, b6))
        b8 = np.zeros((m, b6), float)
        b9 = np.zeros((m, b6), float)
        b10 = np.zeros((m, b6), float)
        a6 = 0
        while True:
            a6 += 1
            b11 = self.fonk3(b14 - b9 - (1/a3) * b10, 1/a3)
            b12 = self.fonk2(b14 - b11 - (1/a3) * b10, b7/a3)
            b10 += a3 * (b11 + b12 - b14)
            a3 = min(a2 * a3, a4)
            if self.fonk1(b8, b9, b14, b11, b12) or a6 >= a5:
                return b11, b12
            else:
                b8, b9 = b11, b12
                print(np.max(b14 - b8 - b9))
b13 = 'set_your_path_here'
b14 = np.array(Image.open(b13).convert('b8'))
b15 = class1()
b8, b16 = b15.fonk4(b14)
plt.figure(b17 = (15, 5))
plt.subplot(131)
plt.imshow(b8, b18 = 'gray')
plt.title('Low-rank Matrix b8')
plt.subplot(132)
plt.imshow(b16, b18 = 'gray')
plt.title('Sparse Matrix b16')
plt.subplot(133)
plt.imshow(b14, b18 = 'gray')
plt.title('Original Image b14')
plt.show()