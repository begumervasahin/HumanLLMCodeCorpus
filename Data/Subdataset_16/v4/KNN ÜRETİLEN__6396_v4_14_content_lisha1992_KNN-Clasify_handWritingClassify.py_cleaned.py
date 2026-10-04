
import numpy as np
import operator
from os import listdir
def fonk1(unlabel, dataset, b12, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabel, (b1, 1)) - dataset
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = b12[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    a1 = 0
    b9 = None
    for key, value in b7.items():
        if value > a1:
            a1 = value
            b9 = key
    return b9
def fonk2(b16):
    b10 = np.zeros((1, 1024))
    with open(b16) as img_file:
        for i in range(32):
            b11 = img_file.readline()
            for j in range(32):
                b10[0, 32 * i + j] = int(b11[j])
    return b10
def fonk3():
    b12 = []
    b13 = listdir('/Users/ceciliaLee/Desktop/digits/trainingDigits')
    b14 = len(b13)
    b15 = np.zeros((b14, 1024))
    for i in range(b14):
        b16 = b13[i]
        b17 = int(b16.split('_')[0])
        b12.append(b17)
        b15[i, :] = fonk2(f'/Users/ceciliaLee/Desktop/digits/trainingDigits/{b16}')
    b18 = listdir('/Users/ceciliaLee/Desktop/digits/testDigits')
    b19 = len(b18)
    a2 = 0.0
    for i in range(b19):
        b16 = b18[i]
        b17 = int(b16.split('_')[0])
        b20 = fonk2(f'/Users/ceciliaLee/Desktop/digits/testDigits/{b16}')
        b21 = fonk1(b20, b15, b12, 3)
        print(f'The classified result by KNN class1: {b21}, the actual class class1: {b17}')
        if b21 != b17:
            a2 += 1
    print(f'\nThe total number of incorrectly classified samples class1: {a2}')
    print(f'\nThe error rate class1: {a2 / b19:.2%}')
if b22 = = '__main__':
    fonk3()