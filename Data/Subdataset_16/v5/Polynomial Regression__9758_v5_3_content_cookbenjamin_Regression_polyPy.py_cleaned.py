import numpy as np
from numpy import linalg
import itertools
import polynomialModel as pm
class class1:
    def fonk1(self, b1 = 0.15, b3=5):
        self.b2 = None
        self.b3 = b3
        self.b4 = None
        self.b5 = b1
        self.a1 = 0
        self.b6 = []
    def fonk2(self, dataset):
        b10, b11, b12, b7 = self.fonk3(dataset)
        self.fonk4(b10, b11, b12, b7)
        b8 = self.fonk6(dataset[:, :-1], dataset[:, -1], self.a1)
        return b8
    def fonk3(self, dataset):
        np.random.shuffle(dataset)
        b9 = int(len(dataset) * self.b5)
        b10 = dataset[:b9, :-1]
        b11 = dataset[:b9, -1]
        b12 = dataset[b9:, :-1]
        b7 = dataset[b9:, -1]
        return b10, b11, b12, b7
    def fonk4(self, b10, b11, b12, b7):
        self.b4 = self.b3
        a2 = 1
        while self.b4 > 0:
            b8 = self.fonk6(b10, b11, a2)
            b13 = b8.error(b12, b7)
            print(f"Degree: {a2}")
            print(b8)
            print(f"Train Error: {b8.error(b10, b11)}")
            print(f"Test Error: {b13}")
            print()
            self.b6.append(b13)
            self.fonk5(b13, a2)
            a2 += 1
    def fonk5(self, error, a2):
        if self.b2 is None or error < self.b2:
            self.b2 = error
            self.a1 = a2
            self.b4 = self.b3
        else:
            self.b4 -= 1
    def fonk6(self, b15, b14, a2):
        b14 = np.asarray(b14).squeeze()
        b15 = np.asarray(b15)
        b16 = b15.shape[1]
        b15 = np.hstack((np.ones((b15.shape[0], 1), dtype=b15.dtype), b15))
        b17 = [self.fonk7(b16 + 1, i) for i in range(b16 + 1)]
        b18 = list(map(sum, itertools.combinations_with_replacement(b17, a2)))
        b19 = np.hstack([self.fonk8((b15 ** p).prod(1)) for p in b18])
        b20 = linalg.lstsq(b19, b14, rcond=None)[0]
        b8 = pm.PolyModel(b18, b20, a2, b16)
        return b8
    @staticmethod
    def fonk7(n, i):
        b21 = np.zeros(n, dtype=int)
        b21[i] = 1
        return b21
    @staticmethod
    def fonk8(b21):
        return b21.reshape(b21.shape + (1,))