import numpy as np
import operator
def fonk1():
    b1 = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    b2 = b1[:, 1:5]
    b3 = b1[:, 5].astype(int)
    return b2, b3
def fonk2(inX, dataSet, b3, k):
    b4 = dataSet.shape[0]
    b5 = np.tile(inX, (b4, 1)) - dataSet
    b6 = b5 ** 2
    b7 = b6.sum(axis=1)
    b8 = np.sqrt(b7)
    b9 = b8.argsort()
    b10 = {}
    for i in range(k):
        b11 = b3[b9[i]]
        b10[b11] = b10.get(b11, 0) + 1
    b12 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
    return b12[0][0]
def fonk3():
    b2, b3 = fonk1()
    b13 = np.zeros((30, 4))
    b14 = np.zeros(30)
    b15 = np.zeros((120, 4))
    b16 = np.zeros(120)
    for i in range(3):
        b13[i * 10: i * 10 + 10] = b2[i * 50: i * 50 + 10]
        b14[i * 10: i * 10 + 10] = b3[i * 50: i * 50 + 10]
        b15[i * 10: i * 10 + 40] = b2[i * 50 + 10: i * 50 + 50]
        b16[i * 10: i * 10 + 40] = b3[i * 50 + 10: i * 50 + 50]
    a1 = 0
    for i in range(30):
        b17 = fonk2(b13[i], b15, b16, 5)
        print(f"The classifier came back with: {b17}, the real answer is: {b14[i]}")
        if b17 != b14[i]:
            a1 += 1
    print(f"The total error rate is: {a1 / 30.0:.2f}")
if b18 = = "__main__":
    fonk3()