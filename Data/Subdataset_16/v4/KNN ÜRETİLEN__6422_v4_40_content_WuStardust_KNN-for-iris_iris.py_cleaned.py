import numpy as np
import operator
def fonk1():
    b8, b1 = fonk2()
    b2 = np.zeros((30, 4))
    b3 = np.zeros(30)
    b4 = np.zeros((120, 4))
    b5 = np.zeros(120)
    for i in range(3):
        b2[i * 10: i * 10 + 10] = b8[i * 50: i * 50 + 10]
        b3[i * 10: i * 10 + 10] = b1[i * 50: i * 50 + 10]
        b4[i * 10 * 4: i * 10 * 4 + 40] = b8[i * 50 + 10: i * 50 + 50]
        b5[i * 10 * 4: i * 10 * 4 + 40] = b1[i * 50 + 10: i * 50 + 50]
    a1 = 0
    for i in range(30):
        b6 = fonk3(b2[i], b4, b5, 5)
        print(f"The classifier came back with: {b6}, the real answer is: {b3[i]}")
        if b6 != b3[i]:
            a1 += 1
    print(f"The total error rate is: {a1 / float(30):.2f}")
def fonk2():
    b7 = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    b8 = b7[:, 1:5]
    b1 = b7[:, 5].astype(int)
    return b8, b1
def fonk3(inX, dataSet, b1, k):
    b9 = dataSet.shape[0]
    b10 = np.tile(inX, (b9, 1)) - dataSet
    b11 = b10 ** 2
    b12 = b11.sum(axis=1)
    b13 = b12 ** 0.5
    b14 = b13.argsort()
    b15 = {}
    for i in range(k):
        b16 = b1[b14[i]]
        b15[b16] = b15.get(b16, 0) + 1
    b17 = sorted(b15.items(), key=operator.itemgetter(1), reverse=True)
    return b17[0][0]
if b18 = = "__main__":
    fonk1()