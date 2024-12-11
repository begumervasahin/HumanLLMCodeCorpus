import numpy as np
import operator
def fonk1():
    b9, b1 = fonk2()
    b2 = np.zeros((30, 4))
    b3 = np.zeros(30)
    b4 = np.zeros((120, 4))
    b5 = np.zeros(120)
    for i in range(3):
        b2[i * 10: i * 10 + 10] = b9[i * 50: i * 50 + 10]
        b3[i * 10: i * 10 + 10] = b1[i * 50: i * 50 + 10]
        b4[i * 10: i * 10 + 40] = b9[i * 50: i * 50 + 40]
        b5[i * 10: i * 10 + 40] = b1[i * 50: i * 50 + 40]
    a1 = 0
    for i in range(30):
        b6 = fonk3(b2[i], b4, b5, k=5)
        print(f"The classifier came back with: {b6}, the real answer is: {b3[i]}")
        if b6 != b3[i]:
            a1 += 1
    b7 = a1 / float(30)
    print(f"The total error rate is: {b7:.2f}")
def fonk2():
    b8 = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    b9 = b8[:, 1:5]
    b1 = b8[:, 5].astype(int)
    return b9, b1
def fonk3(in_x, data_set, b1, k):
    b10 = data_set.shape[0]
    b11 = np.tile(in_x, (b10, 1)) - data_set
    b12 = b11 ** 2
    b13 = b12.sum(axis=1)
    b14 = b13 ** 0.5
    b15 = b14.argsort()
    b16 = {}
    for i in range(k):
        b17 = b1[b15[i]]
        b16[b17] = b16.get(b17, 0) + 1
    b18 = sorted(b16.items(), key=operator.itemgetter(1), reverse=True)
    return b18[0][0]
if b19 = = "__main__":
    fonk1()