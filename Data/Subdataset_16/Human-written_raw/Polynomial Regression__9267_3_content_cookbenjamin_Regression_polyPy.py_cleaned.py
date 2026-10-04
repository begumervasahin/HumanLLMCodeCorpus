from numpy import linalg, zeros, ones, hstack, asarray
import itertools
import polynomialModel as pm
import numpy as np
class class1(object):
    def fonk1(self, b1 = .15, max_validation=5):
        self.b2 = None
        self.b3 = max_validation
        self.b4 = None
        self.b5 = b1
        self.a1 = 0
        self.b6 = []
        pass
    def fonk2(self, dataset):
        b10, b11, b12, b7 = self.fonk3(dataset)
        self.fonk4(b10, b11, b12, b7)
        b8 = self.fonk6(dataset[:,:-1], dataset[:,-1], self.a1)
        return b8
    def fonk3(self, dataset):
        np.random.shuffle(dataset)
        b9 = int(len(dataset)*self.b5)
        b10 = dataset[:b9][:,:-1]
        b11 = dataset[:b9][:,-1]
        b12 = dataset[b9:][:, :-1]
        b7 = dataset[b9:][:, -1]
        return b10, b11, b12, b7
    def fonk4(self, b10, b11, b12, b7):
        self.b4 = 5
        a2 = 1
        while self.b4 > 0:
            b8 = self.fonk6(b10, b11, a2)
            print(a2)
            print(b8)
            b13 = b8.b13(b12, b7)
            print("train b13:", b8.b13(b10, b11))
            print("test b13:", b13)
            print()
            self.b6.append(b13)
            self.fonk5(b13, a2)
            a2 += 1
    def fonk5(self, b13, a2):
        if not self.b2 or b13 < self.b2:
            self.b2 = b13
            self.a1 = a2
            self.b4 = self.b3
        else:
            self.b4 -= 1
    def fonk6(self, b16, b14, a2):
        b14 = asarray(b14).squeeze()
        b15 = b14.shape[0]
        b16 = asarray(b16)
        b17 = b16.shape[1]
        b16 = hstack((ones((b16.shape[0], 1), dtype=b16.dtype), b16))
        b18 = [self.fonk7(b17 + 1, i)
                      for i in range(b17 + 1)]
        b19 = list(map(sum,
                          itertools.combinations_with_replacement(b18,
                                                                  a2)))
        b20 = hstack(asarray([self.fonk8((b16 ** p).prod(1)) for p in b19]))
        b21 = linalg.lstsq(b20, b14)
        print(b21[1])
        b8 = pm.PolyModel(b19, b21[0], a2, b17)
        return b8
    def fonk7(self, n, i):
        b22 = zeros(n, dtype=int)
        b22[i] = 1
        return b22
    def fonk8(self, b22):
        return b22.reshape(b22.shape + (1,))