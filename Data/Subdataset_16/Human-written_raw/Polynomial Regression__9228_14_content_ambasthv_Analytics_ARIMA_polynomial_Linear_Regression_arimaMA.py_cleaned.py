import numpy as np
import lmfit as lm
import itertools
def fonk1(self,y,acf,a2,a1):
        self.a1 = 0
        self.a2 = 1
def fonk2(b9, b5, b6, b7, data):
        b1 = b9['b1']
        b2 = b9['b2']
        b3 = b9['b3']
        b4 = [b3 * b3 for b3 in b5] + [b1 * i for i in b6] + [b2 * i for i in b7]
        return [k1 - k2 for (k1, k2) in zip(b4, data)]
def fonk3(y, b18):
        b5 = b18
        b6 = b18[1:]
        b7 = b18[2:]
        b8 = []
        b9 = lm.Parameters()
        b9.add('b1', b10 = 0, min=-1, max=1)
        b9.add('b2', b10 = 0, min=-1, max=1)
        b9.add('b3', b10 = 0, min=-1, max=1)
        b11 = lm.minimize(fitterfn, b9, args=(b5, b6, b7, y))
        b8.append(b11.b9.get('b1').b10)
        b8.append(b11.b9.get('b2').b10)
        b8.append(b11.b9.get('b3').b10)
        return b8
def fonk4(acf, a2):
        b12 = []
        b13 = []
        b14 = []
        b12.append([1 - acf[1], 1, -acf[1]])
        b15 = []
        b16 = np.ndarray.tolist(np.roots(b12[0]))
        for i in b16:
            if not isinstance(i, complex):
                if i > 1 or i < -1:
                    b15.append(i)
            else:
                b15.append(i)
        b14.append([x for x in b16 if x not in b15])
        if a2 = = 2:
            b15 = []
            b17 = []
            for b3 in b14[0]:
                b12.append([acf[1] + acf[2], 1 - 2 * b3, acf[1] + acf[2] + (acf[1] + acf[2]) * b3 ** 2 + b3])
                b17 = np.ndarray.tolist(np.roots(b12.pop()))
                for i in b17:
                    if not isinstance(i, complex):
                        if i > 1 or i < -1:
                            b15.append(i)
                    else:
                        b15.append(i)
            b14.append([x for x in b16 if x not in b15])
        else:
            print("a2>2 not supported")
        if len(b14) > 1:
            b13 = list(itertools.product(b14[0], b14[1]))
        else:
            b13 = b14[0]
        return b13
def fonk5(y, acf, a2, a1):
        b13 = fonk4(acf, a2)
        b18 = []
        if len(y) < 10:
            print("Input time series not suitable for forecasting")
            return
        for b3 in range(len(b13)):
            if isinstance(b13[b3], float):
                b19 = [0, y[0], y[1] + b13[b3] * y[0]]
            else:
                b19 = [0, y[0], y[1] + b13[b3][0] * y[0],
                         y[2] + b13[b3][1] * y[1] + b13[b3][1] * b13[b3][0] * y[0]]
            b18.append(b19)
        b8 = []
        for b3 in range(len(b18)):
            b8.append(fonk3(y, b18[b3]))
        if a1 > len(b8):
            a1 = 0
        return b8[a1][0:a2]