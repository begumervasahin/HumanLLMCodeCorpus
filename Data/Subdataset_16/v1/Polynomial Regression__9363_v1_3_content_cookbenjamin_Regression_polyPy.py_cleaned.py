import numpy as np
import itertools
from numpy.linalg import lstsq
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b5):
        b5 = np.hstack((np.ones((b5.shape[0], 1), dtype=b5.dtype), b5))
        b6 = np.hstack(np.asarray([self.fonk12((b5 ** p).prod(1)) for p in self.b1]))
        return np.dot(b6, self.b2)
    def fonk3(self, b5, b21):
        b7 = self.fonk2(b5)
        return np.mean((b7 - b21) ** 2)
    def fonk4(self, b25):
        return b25.reshape(b25.shape + (1,))
class class2:
    def fonk5(self, b8 = 0.15, max_validation=5):
        self.b9 = None
        self.b10 = max_validation
        self.b11 = None
        self.b12 = b8
        self.a1 = 0
        self.b13 = []
    def fonk6(self, b27):
        b17, b18, b19, b14 = self.fonk7(b27)
        self.fonk8(b17, b18, b19, b14)
        b15 = self.fonk10(b27[:, :-1], b27[:, -1], self.a1)
        return b15
    def fonk7(self, b27):
        np.random.shuffle(b27)
        b16 = int(len(b27) * self.b12)
        b17 = b27[:b16][:, :-1]
        b18 = b27[:b16][:, -1]
        b19 = b27[b16:][:, :-1]
        b14 = b27[b16:][:, -1]
        return b17, b18, b19, b14
    def fonk8(self, b17, b18, b19, b14):
        self.b11 = 5
        b3 = 1
        while self.b11 > 0:
            b15 = self.fonk10(b17, b18, b3)
            print("Degree:", b3)
            print("Model Coefficients:", b15.b2)
            b20 = b15.fonk3(b19, b14)
            print("Train b20:", b15.fonk3(b17, b18))
            print("Test b20:", b20)
            print()
            self.b13.append(b20)
            self.fonk9(b20, b3)
            b3 += 1
    def fonk9(self, b20, b3):
        if self.b9 is None or b20 < self.b9:
            self.b9 = b20
            self.a1 = b3
            self.b11 = self.b10
        else:
            self.b11 -= 1
    def fonk10(self, b5, b21, b3):
        b21 = np.asarray(b21).squeeze()
        b22 = b21.shape[0]
        b5 = np.asarray(b5)
        b4 = b5.shape[1]
        b5 = np.hstack((np.ones((b5.shape[0], 1), dtype=b5.dtype), b5))
        b23 = [self.fonk11(b4 + 1, i) for i in range(b4 + 1)]
        b1 = list(map(sum, itertools.combinations_with_replacement(b23, b3)))
        b6 = np.hstack(np.asarray([self.fonk12((b5 ** p).prod(1)) for p in b1]))
        beta, b24, b24, b24 = lstsq(b6, b21, rcond=None)
        b15 = class1(b1, beta, b3, b4)
        return b15
    def fonk11(self, n, i):
        b25 = np.zeros(n, dtype=int)
        b25[i] = 1
        return b25
    def fonk12(self, b25):
        return b25.reshape(b25.shape + (1,))
if b26 = = "__main__":
    b27 = np.random.rand(100, 3)
    b28 = class2()
    b29 = b28.fonk6(b27)
    print("Best polynomial b3:", b28.a1)
    print("Model b2:", b29.b2)