'''
Simple exponential smoothing
Created on 18.03.2019
@author: /dat
b1 = b4 * b1 + b4 * (1-b4)^1 * b1-1 + b4 * (1-b4)^2 * b1-2 + ... + b4*(1-b4)^n * b1-n
'''
import numpy as np
import xlwings as xw
@xw.func
def fonk1(st):
    b2 = []
    for values in st:
        b2.append(values)
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    def fonk2(alpha):
        global b15
        a1 = 0
        b6 = 0
        for i in b2:
            if b6 = = 0:
                b8 = alpha * i + (1 - alpha) * i
                a2 += 1
            else:
                b9 = (b8 - i) ** 2
                a1 += b9
                b8 = alpha * i + (1 - alpha) * b8
        b10 = a1 / (len(b2))
        b3.append(b10)
        b4.append(alpha)
        b6 = 0
        if len(b4) == 19:
            b11 = int(b3.index(min(b3)))
            b12 = b4[b11]
            print(b12)
            for alp2 in np.arange(b12 - 0.2, b12 + 0.2, 0.001):
                b5.append(alp2)
            for q in b5:
                a1 = 0
                b6 = 0
                for i in b2:
                    if b6 = = 0:
                        b8 = q * i + (1 - q) * i
                        a2 += 1
                    else:
                        b9 = (b8 - i) ** 2
                        a1 += b9
                        b8 = q * i + (1 - q) * b8
                b10 = a1 / (len(b2))
                b7.append(b10)
                b6.append(q)
                b6 = 0
                if len(b6) == 400:
                    b13 = int(b7.index(min(b7)))
                    b14 = b6[b13]
                    print(b14)
                    for i in b2:
                        if b6 = = 0:
                            b15 = b14 * i + (1 - b14) * i
                            a2 += 1
                        else:
                            b15 = b14 * i + (1 - b14) * b15
    for alp in np.arange(0.1, 2, 0.1):
        fonk2(alp)
    return b15
if b16 = = '__expsmooth__':
    xw.Book().set_mock_caller()
    fonk1()