import numpy as np
import operator
def fonk1():
    features, b1 = fonk2()
    test_features, b5, train_features, b2 = fonk3(features, b1)
    b3 = fonk4(test_features, train_features, b2, k=5)
    print(f"The total error rate is: {b3:.2%}")
def fonk2():
    b4 = np.loadtxt(open("./Iris.csv", "rb"), delimiter=",", skiprows=1)
    return b4[:, 1:5], b4[:, 5].astype(int)
def fonk3(features, b1):
    test_features, b5 = np.zeros((30, 4)), np.zeros(30)
    train_features, b2 = np.zeros((120, 4)), np.zeros(120)
    for i in range(3):
        test_features[i * 10: i * 10 + 10] = features[i * 50: i * 50 + 10]
        b5[i * 10: i * 10 + 10] = b1[i * 50: i * 50 + 10]
        train_features[i * 10: i * 10 + 40] = features[i * 50: i * 50 + 40]
        b2[i * 10: i * 10 + 40] = b1[i * 50: i * 50 + 40]
    return test_features, b5, train_features, b2
def fonk4(test_features, train_features, b2, k):
    a1 = 0
    for i in range(len(test_features)):
        b6 = fonk5(test_features[i], train_features, b2, k)
        if b6 != b5[i]:
            a1 += 1
    return a1 / len(test_features)
def fonk5(inX, dataset, b1, k):
    b7 = fonk6(inX, dataset)
    b8 = np.argsort(b7)
    b9 = {}
    for i in range(k):
        b10 = b1[b8[i]]
        b9[b10] = b9.get(b10, 0) + 1
    b11 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
    return b11[0][0]
def fonk6(inX, dataset):
    b12 = np.tile(inX, (dataset.shape[0], 1)) - dataset
    b13 = b12 ** 2
    b14 = b13.sum(axis=1)
    b7 = np.sqrt(b14)
    return b7
if b15 = = '__main__':
    fonk1()