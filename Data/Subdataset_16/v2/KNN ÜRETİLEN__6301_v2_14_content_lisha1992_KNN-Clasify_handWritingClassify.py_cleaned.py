
import numpy as np
from os import listdir
def fonk1(unlabeled_sample, dataset, b12, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabeled_sample, (b1, 1)) - dataset
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = b12[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = sorted(b7.items(), key=lambda item: item[1], reverse=True)
    return b9[0][0]
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
    b13 = listdir('digits/trainingDigits')
    b14 = len(b13)
    b15 = np.zeros((b14, 1024))
    for i, file_name in enumerate(b13):
        b16 = int(file_name.split('_')[0])
        b12.append(b16)
        b15[i, :] = fonk2(f'digits/trainingDigits/{file_name}')
    b17 = listdir('digits/testDigits')
    b18 = len(b17)
    a1 = 0.0
    for file_name in b17:
        b16 = int(file_name.split('_')[0])
        b19 = fonk2(f'digits/testDigits/{file_name}')
        b20 = fonk1(b19, b15, b12, 3)
        print(f'The KNN classified result class1: {b20}, the actual class class1: {b16}')
        if b20 != b16:
            a1 += 1
    print(f'\nThe total number of incorrectly classified samples class1: {a1}')
    print(f'The error rate class1: {a1 / b18:.6f}')
if b21 = = '__main__':
    fonk3()