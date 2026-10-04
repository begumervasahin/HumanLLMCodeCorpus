import numpy as np
import operator
def fonk1(b1 = "./Iris.csv"):
    b2 = np.loadtxt(open(b1, "rb"), delimiter=",", skiprows=1)
    b3 = b2[:, 1:5]
    b4 = b2[:, 5].astype(int)
    return b3, b4
def fonk2(inX, dataSet, b4, k):
    b5 = np.sqrt(((dataSet - inX) ** 2).sum(axis=1))
    b6 = b5.argsort()
    b7 = {}
    for i in range(k):
        b8 = b4[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)
    return b9[0][0]
def fonk3(b3, b4):
    b10 = np.zeros((120, 4))
    b11 = np.zeros(120)
    b12 = np.zeros((30, 4))
    b13 = np.zeros(30)
    for i in range(3):
        start, b14 = i * 50, i * 50 + 50
        b12[i * 10: i * 10 + 10] = b3[start: start + 10]
        b13[i * 10: i * 10 + 10] = b4[start: start + 10]
        b10[i * 40: i * 40 + 40] = b3[start + 10: b14]
        b11[i * 40: i * 40 + 40] = b4[start + 10: b14]
    return b10, b11, b12, b13
def fonk4(b10, b11, b12, b13, k):
    a1 = 0
    for i in range(len(b12)):
        b15 = fonk2(b12[i], b10, b11, k)
        b16 = b13[i]
        print(f"The classifier came back with: {b15}, the real answer is: {b16}")
        if b15 != b16:
            a1 += 1
    b17 = a1 / len(b12)
    return b17
def fonk5():
    b3, b4 = fonk1()
    b10, b11, b12, b13 = fonk3(b3, b4)
    b17 = fonk4(b10, b11, b12, b13, 5)
    print(f"The total error rate is: {b17:.2%}")
if b18 = = "__main__":
    fonk5()