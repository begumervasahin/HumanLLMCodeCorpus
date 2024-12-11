import numpy as np
import xlwings as xw
@xw.func
def fonk1(st):
    b1 = list(st)
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    def fonk2():
        global b14
        a1 = 0
        b5 = 0
        for i in b1:
            if b5 = = 0:
                b7 = alpha * i + (1 - alpha) * i
                a2 += 1
            else:
                b8 = (b7 - i) ** 2
                a1 += b8
                b7 = alpha * i + (1 - alpha) * b7
        b9 = a1 / len(b1)
        b2.append(b9)
        b3.append(alpha)
        b5 = 0
        if len(b3) == 19:
            b10 = int(b2.index(min(b2)))
            b11 = b3[b10]
            print(b11)
            for alp2 in np.arange(b11 - 0.2, b11 + 0.2, 0.001):
                b4.append(alp2)
            for q in b4:
                a1 = 0
                b5 = 0
                for i in b1:
                    if b5 = = 0:
                        b7 = q * i + (1 - q) * i
                        a2 += 1
                    else:
                        b8 = (b7 - i) ** 2
                        a1 += b8
                        b7 = q * i + (1 - q) * b7
                b9 = a1 / len(b1)
                b6.append(b9)
                b5.append(q)
                b5 = 0
                if len(b5) == 400:
                    b12 = int(b6.index(min(b6)))
                    b13 = b5[b12]
                    print(b13)
                    for i in b1:
                        if b5 = = 0:
                            b14 = b13 * i + (1 - b13) * i
                            a2 += 1
                        else:
                            b14 = b13 * i + (1 - b13) * b14
    for alpha in np.arange(0.1, 2, 0.1):
        fonk2(alpha)
    return b14
if b15 = = '__main__':
    xw.Book().set_mock_caller()
    fonk1()