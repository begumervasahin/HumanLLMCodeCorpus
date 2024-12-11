import numpy as np
import operator
import os
def fonk1(unlabeled_data, data_set, labels, k):
    b1 = data_set.shape[0]
    b2 = np.tile(unlabeled_data, (b1, 1)) - data_set
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
def fonk2(file_name):
    b10 = np.zeros((1, 1024))
    with open(file_name) as img_file:
        for i in range(32):
            b11 = img_file.readline()
            for j in range(32):
                b10[0, 32 * i + j] = int(b11[j])
    return b10
def fonk3():
    b12 = []
    b13 = os.listdir('digits/trainingDigits')
    b14 = len(b13)
    b15 = np.zeros((b14, 1024))
    for i in range(b14):
        b16 = b13[i]
        b17 = b16.split('.')[0]
        b18 = int(b17.split('_')[0])
        b12.append(b18)
        b15[i, :] = fonk2('digits/trainingDigits/' + b16)
    b19 = os.listdir('digits/testDigits')
    b20 = len(b19)
    a2 = 0.0
    for i in range(b20):
        b16 = b19[i]
        b17 = b16.split('.')[0]
        b18 = int(b17.split('_')[0])
        b21 = fonk2('digits/testDigits/' + b16)
        b22 = fonk1(b21, b15, b12, 3)
        print('The classified result by KNN class1: %d, the actual class class1: %d' % (b22, b18))
        if b22 != b18:
            a2 += 1
    print('\nThe total number of incorrectly classified samples class1: %d' % a2)
    print('\nThe error rate class1: %f' % (a2 / (b20 * 0.1)))
fonk3()