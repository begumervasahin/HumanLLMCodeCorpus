import numpy as np
import os
def fonk1(unlabeled_data, data_set, labels, k):
    b1 = np.sqrt(np.sum((data_set - unlabeled_data) ** 2, axis=1))
    b2 = np.argsort(b1)
    b3 = {}
    for i in range(k):
        b4 = labels[b2[i]]
        b3[b4] = b3.get(b4, 0) + 1
    b5 = max(b3.items(), key=lambda x: x[1])[0]
    return b5
def fonk2(file_name):
    b6 = np.zeros((1, 1024))
    with open(file_name) as img_file:
        for i in range(32):
            b7 = img_file.readline()
            for j in range(32):
                b6[0, 32 * i + j] = int(b7[j])
    return b6
def fonk3():
    b8 = os.listdir('digits/trainingDigits')
    b9 = len(b8)
    b10 = np.zeros((b9, 1024))
    b11 = []
    for i, file_name_str in enumerate(b8):
        b12 = file_name_str.split('.')[0]
        b13 = int(b12.split('_')[0])
        b11.append(b13)
        b10[i, :] = fonk2('digits/trainingDigits/' + file_name_str)
    b14 = os.listdir('digits/testDigits')
    b15 = len(b14)
    a1 = 0.0
    for file_name_str in b14:
        b12 = file_name_str.split('.')[0]
        b13 = int(b12.split('_')[0])
        b16 = fonk2('digits/testDigits/' + file_name_str)
        b17 = fonk1(b16, b10, b11, 3)
        print(f'The classified result by KNN class1: {b17}, the actual class class1: {b13}')
        if b17 != b13:
            a1 += 1
    print(f'\nThe total number of incorrectly classified samples class1: {a1}')
    print(f'\nThe error rate class1: {a1 / b15:.4f}')
fonk3()