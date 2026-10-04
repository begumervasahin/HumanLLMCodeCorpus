
import numpy as np
import operator
from os import listdir
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
def fonk2(fileName):
    b9 = np.zeros((1, 1024))
    with open(fileName) as imgFile:
        for i in range(32):
            b10 = imgFile.readline()
            for j in range(32):
                b9[0, 32 * i + j] = int(b10[j])
    return b9
def fonk3():
    b11 = []
    b12 = listdir('digits/trainingDigits')
    b13 = len(b12)
    b14 = np.zeros((b13, 1024))
    for i in range(b13):
        b15 = b12[i]
        b16 = b15.split('.')[0]
        b17 = int(b16.split('_')[0])
        b11.append(b17)
        b14[i, :] = fonk2('digits/trainingDigits/%s' % b15)
    b18 = listdir('digits/testDigits')
    b19 = len(b18)
    a3 = 0.0
    for i in range(b19):
        b15 = b18[i]
        b16 = b15.split('.')[0]
        b17 = int(b16.split('_')[0])
        b20 = fonk2('digits/testDigits/%s' % b15)
        b21 = fonk1(b20, b14, b11, 3)
        print('The classified result by KNN class1: %d, the actual class class1: %d' % (b21, b17))
        if b21 != b17:
            a3 += 1
    print('\nThe total number of incorrectly classified samples class1: %d' % a3)
    print('\nThe error rate class1: %f' % (a3 / float(b19)))
if b22 = = '__main__':
    fonk3()