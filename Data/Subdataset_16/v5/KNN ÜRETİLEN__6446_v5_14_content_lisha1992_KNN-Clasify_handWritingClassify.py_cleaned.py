import numpy as np
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
def fonk2(filename):
    b10 = np.zeros((1, 1024))
    with open(filename) as img_file:
        for i in range(32):
            b11 = img_file.readline()
            for j in range(32):
                b10[0, 32 * i + j] = int(b11[j])
    return b10
def fonk3():
    b12 = []
    b13 = '/Users/ceciliaLee/Desktop/digits/trainingDigits'
    b14 = '/Users/ceciliaLee/Desktop/digits/testDigits'
    b15 = listdir(b13)
    b16 = len(b15)
    b17 = np.zeros((b16, 1024))
    for i, filename in enumerate(b15):
        b18 = int(filename.split('_')[0])
        b12.append(b18)
        b17[i, :] = fonk2(f'{b13}/{filename}')
    b19 = listdir(b14)
    b20 = len(b19)
    a2 = 0.0
    for i, filename in enumerate(b19):
        b18 = int(filename.split('_')[0])
        b21 = fonk2(f'{b14}/{filename}')
        b22 = fonk1(b21, b17, b12, 3)
        print(f'The classified result by KNN class1: {b22}, the actual class class1: {b18}')
        if b22 != b18:
            a2 += 1
    print(f'\nThe total number of incorrectly classified samples class1: {a2}')
    print(f'The error rate class1: {a2 / b20:.2%}')
if b23 = = '__main__':
    fonk3()