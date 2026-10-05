from numpy import loadtxt, zeros, tile, argsort, sum, sqrt
import operator
def fonk1():
    b9, b1 = fonk2()
    b2 = zeros((30, 4))
    b3 = zeros(30)
    b4 = zeros((120, 4))
    b5 = zeros(120)
    for i in range(3):
        b2[i * 10: i * 10 + 10] = b9[i * 50: i * 50 + 10]
        b3[i * 10: i * 10 + 10] = b1[i * 50: i * 50 + 10]
        b4[i * 10: i * 10 + 40] = b9[i * 50: i * 50 + 40]
        b5[i * 10: i * 10 + 40] = b1[i * 50: i * 50 + 40]
    b6 = fonk3(b2, b4, b5, k=5)
    b7 = b6 / float(30)
    print(f"The total error rate is: {b7:.2%}")
def fonk2():
    b8 = loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    b9 = b8[:, 1:5]
    b1 = b8[:, 5].astype(int)
    return b9, b1
def fonk3(inX, dataset, b1, k):
    b10 = fonk4(inX, dataset)
    b11 = argsort(b10)
    b12 = {}
    for i in range(k):
        b13 = b1[b11[i]]
        b12[b13] = b12.get(b13, 0) + 1
    b14 = sorted(b12.items(), key=operator.itemgetter(1), reverse=True)
    return b14[0][0]
def fonk4(inX, dataset):
    b15 = tile(inX, (dataset.shape[0], 1)) - dataset
    b16 = b15 ** 2
    b17 = b16.sum(axis=1)
    b10 = sqrt(b17)
    return b10
if b18 = = '__main__':
    fonk1()