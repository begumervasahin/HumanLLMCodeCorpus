import numpy as np
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = 1.5, b2=1e-3, b3=1e10, b4=1000, b5=1e-8):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self, b13, b14, b23, b17, b18):
        b6 = np.max(np.abs(b17 - b13))
        b7 = np.max(np.abs(b18 - b14))
        b8 = np.max(np.abs(b17 + b18 - b23))
        return (b6 < self.b5) and (b7 < self.b5) and (b8 < self.b5)
    def fonk3(self, b23, tau):
        return np.sign(b23) * np.maximum(np.abs(b23) - tau, 0)
    def fonk4(self, b23, tau):
        U, b25, b9 = svd(b23, full_matrices=False)
        b10 = self.fonk3(b25, tau)
        return U @ np.diag(b10) @ b9
    def fonk5(self, b23):
        m, b11 = b23.shape
        b12 = 1 / np.sqrt(max(m, b11))
        b13 = np.zeros((m, b11), dtype=float)
        b14 = np.zeros((m, b11), dtype=float)
        b15 = np.zeros((m, b11), dtype=float)
        b16 = self.b2
        a1 = 0
        while a1 < self.b4:
            a1 += 1
            b17 = self.fonk4(b23 - b14 - b15 / b16, 1 / b16)
            b18 = self.fonk3(b23 - b17 - b15 / b16, b12 / b16)
            b15 += b16 * (b17 + b18 - b23)
            b16 = min(self.b1 * b16, self.b3)
            if self.fonk2(b13, b14, b23, b17, b18):
                break
            b13, b14 = b17, b18
            print(f"Iteration {a1}, max residual: {np.max(np.abs(b23 - b13 - b14))}")
        return b17, b18
def fonk6(b22):
    return np.array(Image.open(b22).convert('b13'))
def fonk7(b23, b13, b25):
    plt.figure(b19 = (15, 5))
    plt.subplot(131)
    plt.imshow(b13, b20 = 'gray')
    plt.title('Low-rank Matrix b13')
    plt.subplot(132)
    plt.imshow(b25, b20 = 'gray')
    plt.title('Sparse Matrix b25')
    plt.subplot(133)
    plt.imshow(b23, b20 = 'gray')
    plt.title('Original Image b23')
    plt.show()
if b21 = = "__main__":
    b22 = 'set_your_path_here'
    b23 = fonk6(b22)
    b24 = class1()
    b13, b25 = b24.fonk5(b23)
    fonk7(b23, b13, b25)