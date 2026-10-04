import numpy as np
import lmfit as lm
import itertools
class class1:
    def fonk1(self, b3, b4, b2, b1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, b13, b9, b10, b11, data):
        b5 = b13['b5']
        b6 = b13['b6']
        b7 = b13['b7']
        b8 = [b7 * b7 for b7 in b9] + [b5 * i for i in b10] + [b6 * i for i in b11]
        return [k1 - k2 for (k1, k2) in zip(b8, data)]
    def fonk3(self, b3, b22):
        b9 = b22
        b10 = b22[1:]
        b11 = b22[2:]
        b12 = []
        b13 = lm.Parameters()
        b13.add('b5', b14 = 0, min=-1, max=1)
        b13.add('b6', b14 = 0, min=-1, max=1)
        b13.add('b7', b14 = 0, min=-1, max=1)
        b15 = lm.minimize(self.fitterfn, b13, args=(b9, b10, b11, b3))
        b12.append(b15.b13.get('b5').b14)
        b12.append(b15.b13.get('b6').b14)
        b12.append(b15.b13.get('b7').b14)
        return b12
    def fonk4(self, b4, b2):
        b16 = []
        b17 = []
        b18 = []
        b16.append([1 - b4[1], 1, -b4[1]])
        b19 = []
        b20 = np.roots(b16[0]).tolist()
        for i in b20:
            if not isinstance(i, complex):
                if i > 1 or i < -1:
                    b19.append(i)
            else:
                b19.append(i)
        b18.append([x for x in b20 if x not in b19])
        if b2 = = 2:
            b19 = []
            b21 = []
            for b7 in b18[0]:
                b16.append([b4[1] + b4[2], 1 - 2 * b7, b4[1] + b4[2] + (b4[1] + b4[2]) * b7 ** 2 + b7])
                b21 = np.roots(b16.pop()).tolist()
                for i in b21:
                    if not isinstance(i, complex):
                        if i > 1 or i < -1:
                            b19.append(i)
                    else:
                        b19.append(i)
            b18.append([x for x in b21 if x not in b19])
        else:
            print("b2>2 not supported")
        if len(b18) > 1:
            b17 = list(itertools.product(*b18))
        else:
            b17 = b18[0]
        return b17
    def fonk5(self):
        b17 = self.fonk4(self.b4, self.b2)
        b22 = []
        if len(self.b3) < 10:
            print("Input time series not suitable for forecasting")
            return
        for b7 in range(len(b17)):
            if isinstance(b17[b7], float):
                b23 = [0, self.b3[0], self.b3[1] + b17[b7] * self.b3[0]]
            else:
                b23 = [0, self.b3[0], self.b3[1] + b17[b7][0] * self.b3[0],
                         self.b3[2] + b17[b7][1] * self.b3[1] + b17[b7][1] * b17[b7][0] * self.b3[0]]
            b22.append(b23)
        b12 = []
        for b7 in range(len(b22)):
            b12.append(self.fonk3(self.b3, b22[b7]))
        if self.b1 > len(b12):
            self.b1 = 0
        return b12[self.b1][0:self.b2]
b3 = [1, 2, 3, 4, 5]
b4 = [1, 0.5, 0.2]
b2 = 2
b1 = 0
b24 = class1(b3, b4, b2, b1)
b25 = b24.fonk5()
print(b25)