import numpy as np
def fonk1(b15):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    def fonk2(alpha):
        a1 = 0
        b4 = 0
        for i in b15:
            if b4 = = 0:
                b6 = alpha * i + (1 - alpha) * i
                a2 += 1
            else:
                b7 = (b6 - i) ** 2
                a1 += b7
                b6 = alpha * i + (1 - alpha) * b6
        b8 = a1 / len(b15)
        b1.append(b8)
        b2.append(alpha)
        if len(b2) == 19:
            b9 = b1.index(min(b1))
            b10 = b2[b9]
            print(b10)
            for alp2 in np.arange(b10 - 0.2, b10 + 0.2, 0.001):
                b3.append(alp2)
            for q in b3:
                a1 = 0
                b4 = 0
                for i in b15:
                    if b4 = = 0:
                        b6 = q * i + (1 - q) * i
                        a2 += 1
                    else:
                        b7 = (b6 - i) ** 2
                        a1 += b7
                        b6 = q * i + (1 - q) * b6
                b8 = a1 / len(b15)
                b5.append(b8)
                b4.append(q)
                if len(b4) == 400:
                    b11 = b5.index(min(b5))
                    b12 = b4[b11]
                    print(b12)
                    for i in b15:
                        if b4 = = 0:
                            b13 = b12 * i + (1 - b12) * i
                            a2 += 1
                        else:
                            b13 = b12 * i + (1 - b12) * b13
    for alp in np.arange(0.1, 2, 0.1):
        fonk2(alp)
    return b13
if b14 = = '__main__':
    b15 = np.array([1, 2, 3, 4, 5])
    b16 = fonk1(b15)
    print("Result:", b16)