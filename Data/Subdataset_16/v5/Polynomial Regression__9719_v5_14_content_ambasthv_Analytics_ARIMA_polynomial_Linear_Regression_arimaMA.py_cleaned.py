import numpy as np
import lmfit as lm
import itertools
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    @staticmethod
    def fonk2(b12, b9, b10, b11, data):
        b5 = b12['b5']
        b6 = b12['b6']
        b7 = b12['b7']
        b8 = [b7 * b7 for b7 in b9] + [b5 * i for i in b10] + [b6 * i for i in b11]
        return [m - d for m, d in zip(b8, data)]
    def fonk3(self, b1, b24):
        b9 = b24
        b10 = b24[1:]
        b11 = b24[2:]
        b12 = lm.Parameters()
        b12.add('b5', b13 = 0, min=-1, max=1)
        b12.add('b6', b13 = 0, min=-1, max=1)
        b12.add('b7', b13 = 0, min=-1, max=1)
        b14 = lm.minimize(self.fitter_fn, b12, args=(b9, b10, b11, b1))
        b15 = [
            b14.b12['b5'].b13,
            b14.b12['b6'].b13,
            b14.b12['b7'].b13
        ]
        return b15
    def fonk4(self, b2, b3):
        b16 = [[1 - b2[1], 1, -b2[1]]]
        b17 = []
        b18 = np.roots(b16[0]).tolist()
        for val in b18:
            if not isinstance(val, complex) and (val > 1 or val < -1):
                b17.append(val)
        b19 = [val for val in b18 if val not in b17]
        if b3 = = 2:
            b20 = []
            b17 = []
            for b7 in b19:
                b16.append([b2[1] + b2[2], 1 - 2 * b7, b2[1] + b2[2] + (b2[1] + b2[2]) * b7 ** 2 + b7])
                b21 = np.roots(b16.pop()).tolist()
                for val in b21:
                    if not isinstance(val, complex) and (val > 1 or val < -1):
                        b17.append(val)
                b20 = [val for val in b21 if val not in b17]
            b22 = list(itertools.product(b19, b20))
        else:
            b22 = b19
        return b22
    def fonk5(self):
        b22 = self.fonk4(self.b2, self.b3)
        b23 = []
        if len(self.b1) < 10:
            print("Input time series not suitable for forecasting")
            return
        for b19 in b22:
            if isinstance(b19, float):
                b24 = [0, self.b1[0], self.b1[1] + b19 * self.b1[0]]
            else:
                b24 = [
                    0,
                    self.b1[0],
                    self.b1[1] + b19[0] * self.b1[0],
                    self.b1[2] + b19[1] * self.b1[1] + b19[1] * b19[0] * self.b1[0]
                ]
            b23.append(b24)
        b15 = [self.fonk3(self.b1, b24) for b24 in b23]
        if self.b4 >= len(b15):
            self.b4 = 0
        return b15[self.b4][:self.b3]
b1 = [some_time_series_data]
b2 = [some_acf_values]
b3 = 2
b4 = 0
b25 = class1(b1, b2, b3, b4)
b26 = b25.fonk5()
print(b26)