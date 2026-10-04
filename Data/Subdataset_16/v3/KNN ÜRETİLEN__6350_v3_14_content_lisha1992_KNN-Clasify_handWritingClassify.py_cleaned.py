
import numpy as np
from os import listdir
def fonk1(unlabeled_sample, dataset, b10, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabeled_sample, (b1, 1)) - dataset
    b3 = np.sqrt(np.sum(b2 ** 2, axis=1))
    b4 = np.argsort(b3)
    b5 = {}
    for i in range(k):
        b6 = b10[b4[i]]
        b5[b6] = b5.get(b6, 0) + 1
    b7 = sorted(b5.items(), key=lambda item: item[1], reverse=True)
    return b7[0][0]
def fonk2(file_name):
    b8 = np.zeros((1, 1024))
    with open(file_name) as img_file:
        for i in range(32):
            b9 = img_file.readline()
            for j in range(32):
                b8[0, 32 * i + j] = int(b9[j])
    return b8
def fonk3(directory):
    b10 = []
    b11 = listdir(directory)
    b1 = len(b11)
    b12 = np.zeros((b1, 1024))
    for i, file_name in enumerate(b11):
        b13 = int(file_name.split('_')[0])
        b10.append(b13)
        b12[i, :] = fonk2(f'{directory}/{file_name}')
    return b12, b10
def fonk4():
    training_matrix, b14 = fonk3('digits/trainingDigits')
    test_matrix, b15 = fonk3('digits/testDigits')
    b16 = len(b15)
    a1 = 0.0
    for i in range(b16):
        b17 = fonk1(test_matrix[i], training_matrix, b14, k=3)
        b18 = b15[i]
        print(f'The KNN classified result class1: {b17}, the actual class class1: {b18}')
        if b17 != b18:
            a1 += 1
    print(f'\nThe total number of incorrectly classified samples class1: {a1}')
    print(f'The error rate class1: {a1 / b16:.6f}')
if b19 = = '__main__':
    fonk4()