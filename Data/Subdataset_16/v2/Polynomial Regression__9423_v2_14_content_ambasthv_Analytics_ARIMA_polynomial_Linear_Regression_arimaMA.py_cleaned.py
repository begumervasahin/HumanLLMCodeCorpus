import numpy as np
import lmfit as lm
import itertools
class class1:
    def fonk1(self, b3, b4, b2, b1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b12, b9, b10, b11, data):
        b5 = b12['b5']
        b6 = b12['b6']
        b7 = b12['b7']
        b8 = [b7 * b7 for b7 in b9] + [b5 * i for i in b10] + [b6 * i for i in b11]
        return [k1 - k2 for k1, k2 in zip(b8, data)]
    def fonk3(self, b3, b21):
        b9 = b21
        b10 = b21[1:]
        b11 = b21[2:]
        b12 = lm.Parameters()
        b12.add('b5', b13 = 0, min=-1, max=1)
        b12.add('b6', b13 = 0, min=-1, max=1)
        b12.add('b7', b13 = 0, min=-1, max=1)
        b14 = lm.minimize(self.fitter_fn, b12, args=(b9, b10, b11, b3))
        return [b14.b12['b5'].b13, b14.b12['b6'].b13, b14.b12['b7'].b13]
    def fonk4(self, b4, b2):
        b15 = []
        b16 = []
        b17 = []
        b15.append([1 - b4[1], 1, -b4[1]])
        b18 = np.roots(b15[0]).tolist()
        b19 = [i for i in b18 if isinstance(i, complex) or i > 1 or i < -1]
        b17.append([x for x in b18 if x not in b19])
        if b2 = = 2:
            b20 = []
            for b7 in b17[0]:
                b15 = [b4[1] + b4[2], 1 - 2 * b7, b4[1] + b4[2] + (b4[1] + b4[2]) * b7 ** 2 + b7]
                b20 = np.roots(b15).tolist()
                b19 = [i for i in b20 if isinstance(i, complex) or i > 1 or i < -1]
            b17.append([x for x in b20 if x not in b19])
        else:
            print("b2>2 not supported")
        if len(b17) > 1:
            b16 = list(itertools.product(*b17))
        else:
            b16 = b17[0]
        return b16
    def fonk5(self):
        b16 = self.fonk4(self.b4, self.b2)
        if len(self.b3) < 10:
            print("Input time series not suitable for forecasting")
            return []
        b21 = []
        for b17 in b16:
            if isinstance(b17, float):
                b21.append([0, self.b3[0], self.b3[1] + b17 * self.b3[0]])
            else:
                b21.append([0, self.b3[0], self.b3[1] + b17[0] * self.b3[0],
                           self.b3[2] + b17[1] * self.b3[1] + b17[1] * b17[0] * self.b3[0]])
        b22 = [self.fonk3(self.b3, e) for e in b21]
        if self.b1 >= len(b22):
            self.b1 = 0
        return b22[self.b1][:self.b2]
b3 = [1, 2, 3, 4, 5]
b4 = [1, 0.5, 0.2]
b2 = 2
b1 = 0
b23 = class1(b3, b4, b2, b1)
b24 = b23.fonk5()
print(b24)