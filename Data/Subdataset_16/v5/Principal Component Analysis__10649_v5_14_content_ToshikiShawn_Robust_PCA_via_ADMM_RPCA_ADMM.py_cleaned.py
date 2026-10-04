import numpy as np
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = 1.5, b2=1e-3, b3=1e10, b4=1000):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b13, b14, b20, b16, b17, b5 = 1e-8):
        b6 = np.max(b16 - b13) < b5
        b7 = np.max(b17 - b14) < b5
        b8 = np.max(b16 + b17 - b20) < b5
        return b6 and b7 and b8
    def fonk3(self, b20, tau):
        return np.sign(b20) * np.maximum(np.abs(b20) - tau, 0)
    def fonk4(self, b20, tau):
        u, s, b9 = svd(b20, full_matrices=False)
        b10 = self.fonk3(s, tau)
        return np.dot(u, np.dot(np.diag(b10), b9))
    def fonk5(self, b20):
        m, b11 = b20.shape
        b12 = 1 / np.sqrt(max(m, b11))
        b13 = np.zeros((m, b11), float)
        b14 = np.zeros((m, b11), float)
        b15 = np.zeros((m, b11), float)
        for iteration in range(self.b4):
            b16 = self.fonk4(b20 - b14 - (1 / self.b2) * b15, 1 / self.b2)
            b17 = self.fonk3(b20 - b16 - (1 / self.b2) * b15, b12 / self.b2)
            b15 += self.b2 * (b16 + b17 - b20)
            self.b2 = min(self.b1 * self.b2, self.b3)
            if self.fonk2(b13, b14, b20, b16, b17):
                break
            b13, b14 = b16, b17
            print(f"Iteration {iteration + 1}, error: {np.max(b20 - b13 - b14)}")
        return b16, b17
def fonk6(b24):
    return np.array(Image.open(b24).convert('b13'))
def fonk7(b13, b22, b20):
    plt.figure(b18 = (15, 5))
    plt.subplot(131)
    plt.imshow(b13, b19 = 'gray')
    plt.title('Low-rank')
    plt.subplot(132)
    plt.imshow(b22, b19 = 'gray')
    plt.title('Sparse')
    plt.subplot(133)
    plt.imshow(b20, b19 = 'gray')
    plt.title('Original')
    plt.show()
def fonk8(b24):
    b20 = fonk6(b24)
    b21 = class1()
    b13, b22 = b21.fonk5(b20)
    fonk7(b13, b22, b20)
if b23 = = '__main__':
    b24 = 'set your path'
    fonk8(b24)