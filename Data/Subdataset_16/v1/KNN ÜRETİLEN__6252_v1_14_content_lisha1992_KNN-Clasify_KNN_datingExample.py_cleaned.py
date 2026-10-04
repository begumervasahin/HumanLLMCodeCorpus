
import numpy as np
import operator
import matplotlib.pyplot as plt
def fonk1(unLabel, dataSet, labels, k):
    b1 = dataSet.shape[0]
    b2 = np.tile(unLabel, (b1, 1)) - dataSet
    b3 = b2**2
    b4 = np.sum(b3, axis=1)
    b5 = b4**0.5
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = labels[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    a1 = 0
    a2 = -1
    for key, value in b7.items():
        if value > a1:
            a1 = value
            a2 = key
    return a2
def fonk2(filename, dim2):
    with open(filename) as fr:
        b9 = fr.readlines()
    b10 = len(b9)
    b11 = np.zeros((b10, dim2))
    b12 = []
    a3 = 0
    for b13 in b9:
        b13 = b13.strip()
        b14 = b13.split('\t')
        b11[a3, :] = b14[0:dim2]
        b12.append(int(b14[-1]))
        a3 += 1
    return b11, b12
def fonk3(datingDataMat, b22):
    b15 = plt.figure()
    b16 = b15.add_subplot(111)
    b16.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * np.array(b22), 15.0 * np.array(b22))
    plt.show()
def fonk4(dataSet):
    b17 = dataSet.min(0)
    b18 = dataSet.max(0)
    b19 = b18 - b17
    b20 = dataSet.shape[0]
    b21 = (dataSet - np.tile(b17, (b20, 1))) / np.tile(b19, (b20, 1))
    return b21, b19, b17
def fonk5():
    a4 = 0.1
    datingDataMat, b22 = fonk2('datingTestSet2.txt', 3)
    normMat, b19, b17 = fonk4(datingDataMat)
    b23 = int(normMat.shape[0] * a4)
    a5 = 0.0
    for i in range(b23):
        b24 = fonk1(normMat[i, :], normMat[b23:normMat.shape[0], :], b22[b23:normMat.shape[0]], 3)
        print(f'Result from KNN Classifier class1: {b24}, the actual class class1: {b22[i]}')
        if b24 != b22[i]:
            a5 += 1
    print(f'The total error a4 class1: {a5 / b23:.2f}')
def fonk6():
    b25 = ['not at all', 'in small doses', 'in large doses']
    b26 = float(input('Percentage of time spent playing video games? '))
    b27 = float(input('Frequent flier miles earned per year? '))
    b28 = float(input('Liters of ice cream consumed per year? '))
    datingDataMat, b22 = fonk2('datingTestSet2.txt', 3)
    normMat, b19, b17 = fonk4(datingDataMat)
    b29 = np.array([b26, b27, b28])
    b24 = fonk1((b29 - b17) / b19, normMat, b22, 3)
    print(f'You will probably like this person: {b25[b24 - 1]}')
if b30 = = '__main__':
    fonk6()