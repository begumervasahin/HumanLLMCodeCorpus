import numpy as np
import operator
def fonk1():
    b1 = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    b2 = b1[:, 1:5]
    b3 = b1[:, 5].astype(int)
    return b2, b3
def fonk2(inX, dataSet, b3, k):
    b4 = np.sqrt(((dataSet - inX) ** 2).sum(axis=1))
    b5 = b4.argsort()
    b6 = {}
    for i in range(k):
        b7 = b3[b5[i]]
        b6[b7] = b6.get(b7, 0) + 1
    b8 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk3():
    b2, b3 = fonk1()
    b9 = np.zeros((30, 4))
    b10 = np.zeros(30)
    b11 = np.zeros((120, 4))
    b12 = np.zeros(120)
    for i in range(3):
        start, b13 = i * 50, i * 50 + 50
        b9[i * 10: i * 10 + 10] = b2[start: start + 10]
        b10[i * 10: i * 10 + 10] = b3[start: start + 10]
        b11[i * 40: i * 40 + 40] = b2[start + 10: b13]
        b12[i * 40: i * 40 + 40] = b3[start + 10: b13]
    a1 = 0
    for i in range(30):
        b14 = fonk2(b9[i], b11, b12, 5)
        b15 = b10[i]
        print(f"The classifier came back with: {b14}, the real answer is: {b15}")
        if b14 != b15:
            a1 += 1
    print(f"The total error rate is: {a1 / 30.0:.2%}")
if b16 = = "__main__":
    fonk3()