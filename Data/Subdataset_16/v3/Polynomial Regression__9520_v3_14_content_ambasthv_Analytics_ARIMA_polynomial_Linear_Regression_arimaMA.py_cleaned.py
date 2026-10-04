import numpy as np
import lmfit as lm
import itertools
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b9, x1, x2, b11, data):
        b5 = b9['b5']
        b6 = b9['b6']
        b7 = b9['b7']
        b8 = [b7 ** 2 for _ in x1] + [b5 * val for val in x2] + [b6 * val for val in b11]
        return [m - d for m, d in zip(b8, data)]
    def fonk3(self, b1, b19):
        b9 = lm.Parameters()
        b9.add('b5', b10 = 0, min=-1, max=1)
        b9.add('b6', b10 = 0, min=-1, max=1)
        b9.add('b7', b10 = 0, min=-1, max=1)
        x1, x2, b11 = b19, b19[1:], b19[2:]
        b12 = lm.minimize(self.fitter_fn, b9, args=(x1, x2, b11, b1))
        return [b12.b9['b5'].b10, b12.b9['b6'].b10, b12.b9['b7'].b10]
    def fonk4(self, b2, b3):
        b13 = []
        b14 = [1 - b2[1], 1, -b2[1]]
        b15 = np.b15(b14).tolist()
        b16 = [r for r in b15 if not isinstance(r, complex) and -1 <= r <= 1]
        if b3 = = 2:
            b17 = []
            for b7 in b16:
                b14 = [b2[1] + b2[2], 1 - 2 * b7, b2[1] + b2[2] + (b2[1] + b2[2]) * b7 ** 2 + b7]
                b15 = np.b15(b14).tolist()
                b18 = [r for r in b15 if not isinstance(r, complex) and -1 <= r <= 1]
                b17.extend(b18)
            b13 = list(itertools.product(b16, b17))
        elif b3 = = 1:
            b13 = b16
        else:
            print("b3>2 not supported")
        return b13
    def fonk5(self):
        b13 = self.fonk4(self.b2, self.b3)
        if len(self.b1) < 10:
            print("Input time series not suitable for forecasting")
            return []
        b19 = []
        for theta in b13:
            if isinstance(theta, float):
                b19.append([0, self.b1[0], self.b1[1] + theta * self.b1[0]])
            else:
                b19.append([
                    0, self.b1[0],
                    self.b1[1] + theta[0] * self.b1[0],
                    self.b1[2] + theta[1] * self.b1[1] + theta[1] * theta[0] * self.b1[0]
                ])
        b20 = [self.fonk3(self.b1, e) for e in b19]
        if self.b4 >= len(b20):
            self.b4 = 0
        return b20[self.b4][:self.b3]
b1 = [1, 2, 3, 4, 5]
b2 = [1, 0.5, 0.2]
b3 = 2
b4 = 0
b21 = class1(b1, b2, b3, b4)
b22 = b21.fonk5()
print(b22)