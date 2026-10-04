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
    def fonk2(self, b13, b14, b21, b17, b18):
        b6 = np.max(np.abs(b17 - b13))
        b7 = np.max(np.abs(b18 - b14))
        b8 = np.max(np.abs(b17 + b18 - b21))
        return (b6 < self.b5) and (b7 < self.b5) and (b8 < self.b5)
    def fonk3(self, b21, tau):
        return np.sign(b21) * np.maximum(np.abs(b21) - tau, 0)
    def fonk4(self, b21, tau):
        U, b23, b9 = svd(b21, full_matrices=False)
        b10 = self.fonk3(b23, tau)
        return U @ np.diag(b10) @ b9
    def fonk5(self, b21):
        m, b11 = b21.shape
        b12 = 1 / np.sqrt(max(m, b11))
        b13 = np.zeros((m, b11), dtype=float)
        b14 = np.zeros((m, b11), dtype=float)
        b15 = np.zeros((m, b11), dtype=float)
        b16 = self.b2
        a1 = 0
        while a1 < self.b4:
            a1 += 1
            b17 = self.fonk4(b21 - b14 - b15 / b16, 1 / b16)
            b18 = self.fonk3(b21 - b17 - b15 / b16, b12 / b16)
            b15 += b16 * (b17 + b18 - b21)
            b16 = min(self.b1 * b16, self.b3)
            if self.fonk2(b13, b14, b21, b17, b18):
                break
            b13, b14 = b17, b18
            print(f"Iteration {a1}, max residual: {np.max(np.abs(b21 - b13 - b14))}")
        return b17, b18
if b19 = = "__main__":
    b20 = 'set_your_path_here'
    b21 = np.array(Image.open(b20).convert('b13'))
    b22 = class1()
    b13, b23 = b22.fonk5(b21)
    plt.figure(b24 = (15, 5))
    plt.subplot(131)
    plt.imshow(b13, b25 = 'gray')
    plt.title('Low-rank Matrix b13')
    plt.subplot(132)
    plt.imshow(b23, b25 = 'gray')
    plt.title('Sparse Matrix b23')
    plt.subplot(133)
    plt.imshow(b21, b25 = 'gray')
    plt.title('Original Image b21')
    plt.show()