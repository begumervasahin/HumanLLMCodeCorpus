import numpy as np
import os
def fonk1(unlabeled, dataSet, labels, k):
    b1 = dataSet.shape[0]
    b2 = np.tile(unlabeled, (b1, 1)) - dataSet
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = b4 ** 0.5
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = labels[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    a1 = 0
    for key, value in b7.items():
        if value > a1:
            a1 = value
            b9 = key
    return b9
def fonk2(fileName):
    b10 = np.zeros((1, 1024))
    with open(fileName) as imgFile:
        for i in range(32):
            b11 = imgFile.readline()
            for j in range(32):
                b10[0, 32 * i + j] = int(b11[j])
    return b10
def fonk3():
    b12 = []
    b13 = os.listdir('/Users/ceciliaLee/Desktop/digits/trainingDigits')
    b14 = len(b13)
    b15 = np.zeros((b14, 1024))
    for i in range(b14):
        b16 = b13[i]
        b17 = b16.split('.')[0]
        b18 = int(b17.split('_')[0])
        b12.append(b18)
        b15[i, :] = fonk2('/Users/ceciliaLee/Desktop/digits/trainingDigits/%s' % b16)
    b19 = os.listdir('/Users/ceciliaLee/Desktop/digits/testDigits')
    b20 = len(b19)
    a2 = 0.0
    for i in range(b20):
        b16 = b19[i]
        b17 = b16.split('.')[0]
        b18 = int(b17.split('_')[0])
        b21 = fonk2('/Users/ceciliaLee/Desktop/digits/testDigits/%s' % b16)
        b22 = fonk1(b21, b15, b12, 3)
        print('Classified Result: %d, Actual Class: %d' % (b22, b18))
        if b22 != b18:
            a2 += 1
    print('\nTotal Incorrectly Classified Samples: %d' % a2)
    print('\nError Rate: %f' % (a2 / b20))
fonk3()