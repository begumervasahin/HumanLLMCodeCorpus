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
        b6 = np.hstack([self.fonk13((b5 ** p).prod(axis=1)) for p in self.b1])
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
            self.fonk14(b3, b17.b2, b18, b19)
            self.b12.append(b19)
            if self.b11 is None or b19 < self.b11:
                self.b11 = b19
                self.a1 = b3
                b16 = self.b10
            else:
                b16 -= 1
            b3 += 1
    def fonk9(self, b5, Y, b3):
        b20 = self.fonk10(b5)
        b1 = self.fonk11(b5.shape[1] + 1, b3)
        b6 = np.hstack([self.fonk13((b20 ** p).prod(axis=1)) for p in b1])
        b2, b21, b21, b21 = lstsq(b6, Y, rcond=None)
        return class1(b1, b2, b3, b5.shape[1])
    @staticmethod
    def fonk10(b5):
        b22 = b5.shape[0]
        return np.hstack((np.ones((b22, 1)), b5))
    @staticmethod
    def fonk11(b4, b3):
        b23 = [class2.fonk12(b4, i) for i in range(b4)]
        return [sum(comb) for comb in itertools.combinations_with_replacement(b23, b3)]
    @staticmethod
    def fonk12(length, index):
        b24 = np.zeros(length, dtype=int)
        b24[index] = 1
        return b24
    @staticmethod
    def fonk13(x):
        return x.reshape(-1, 1)
    @staticmethod
    def fonk14(b3, b2, b18, b19):
        print(f"Degree: {b3}")
        print(f"Model Coefficients: {b2}")
        print(f"Train error: {b18}")
        print(f"Test error: {b19}\n")
if b25 = = "__main__":
    b26 = np.random.rand(100, 3)
    b27 = class2()
    b28 = b27.fonk6(b26)
    print("Best polynomial b3:", b27.a1)
    print("Model b2:", b28.b2)