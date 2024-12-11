import math
import numpy as np
from skimage import io
class class1:
    def fonk1(self, b11):
        self.b1 = b11
    def fonk2(self, b9):
        rows, b2 = b9.shape
        b3 = np.b3(b9)
        b4 = np.var(b9)
        return b3, math.sqrt(b4)
    def fonk3(self, b9):
        b5 = b9.size
        hist, b6 = np.histogram(b9, bins=256)
        b7 = hist / b5
        b7 = b7[b7 != 0]
        b8 = -np.sum(b7 * np.log2(b7))
        return b8
    def fonk4(self):
        b9 = io.imread(self.b1, as_gray=True)
        b3, b4 = self.fonk2(b9)
        return b3, b4
    def fonk5(self):
        b9 = io.imread(self.b1, as_gray=True)
        b8 = self.fonk3(b9)
        return b8
if b10 = = "__main__":
    b11 = "path_to_your_image.jpg"
    b12 = class1(b11)
    b3, b4 = b12.fonk4()
    b8 = b12.fonk5()
    print("Mean:", b3)
    print("Variance:", b4)
    print("Entropy:", b8)