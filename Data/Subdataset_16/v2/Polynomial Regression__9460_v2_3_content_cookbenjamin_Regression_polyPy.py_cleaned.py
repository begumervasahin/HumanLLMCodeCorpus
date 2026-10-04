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
        b5 = np.hstack((np.ones((b5.shape[0], 1)), b5))
        b6 = np.hstack([self.fonk11((b5 ** p).prod(axis=1)) for p in self.b1])
        return np.dot(b6, self.b2)
    def fonk3(self, b5, Y):
        b7 = self.fonk2(b5)
        return np.mean((b7 - Y) ** 2)
    @staticmethod
    def fonk4(x):
        return x.reshape(-1, 1)
class class2:
    def fonk5(self, b8 = 0.15, max_validation=5):
        self.b9 = b8
        self.b10 = max_validation
        self.b11 = None
        self.a1 = 0
        self.b12 = []
    def fonk6(self, b26):
        train_X, train_Y, test_X, b13 = self.fonk7(b26)
        self.fonk8(train_X, train_Y, test_X, b13)
        return self.fonk9(b26[:, :-1], b26[:, -1], self.a1)
    def fonk7(self, b26):
        np.random.shuffle(b26)
        b14 = int(len(b26) * self.b9)
        train, b15 = b26[:b14], b26[b14:]
        return train[:, :-1], train[:, -1], b15[:, :-1], b15[:, -1]
    def fonk8(self, train_X, train_Y, test_X, b13):
        b16 = self.b10
        b3 = 1
        while b16 > 0:
            b17 = self.fonk9(train_X, train_Y, b3)
            b18 = b17.fonk3(train_X, train_Y)
            b19 = b17.fonk3(test_X, b13)
            print(f"Degree: {b3}")
            print(f"Model Coefficients: {b17.b2}")
            print(f"Train error: {b18}")
            print(f"Test error: {b19}\n")
            self.b12.append(b19)
            if self.b11 is None or b19 < self.b11:
                self.b11 = b19
                self.a1 = b3
                b16 = self.b10
            else:
                b16 -= 1
            b3 += 1
    def fonk9(self, b5, Y, b3):
        b20 = Y.shape[0]
        b4 = b5.shape[1]
        b21 = np.hstack((np.ones((b20, 1)), b5))
        b22 = [self.fonk10(b4 + 1, i) for i in range(b4 + 1)]
        b1 = [sum(comb) for comb in itertools.combinations_with_replacement(b22, b3)]
        b6 = np.hstack([self.fonk11((b21 ** p).prod(axis=1)) for p in b1])
        b2, b23, b23, b23 = lstsq(b6, Y, rcond=None)
        return class1(b1, b2, b3, b4)
    @staticmethod
    def fonk10(length, index):
        b24 = np.zeros(length, dtype=int)
        b24[index] = 1
        return b24
    @staticmethod
    def fonk11(x):
        return x.reshape(-1, 1)
if b25 = = "__main__":
    b26 = np.random.rand(100, 3)
    b27 = class2()
    b28 = b27.fonk6(b26)
    print("Best polynomial b3:", b27.a1)
    print("Model b2:", b28.b2)