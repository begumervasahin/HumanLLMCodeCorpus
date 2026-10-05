
import numpy as np
import operator
import matplotlib.pyplot as plt
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
def fonk2(filename, dim):
    b10 = np.zeros((len(open(filename).readlines()), dim))
    b11 = []
    with open(filename) as file:
        a2 = 0
        for b12 in file:
            b12 = b12.strip()
            b13 = b12.split('\t')
            b10[a2, :] = b13[:dim]
            b11.append(int(b13[-1]))
            a2 += 1
    return b10, b11
def fonk3(b10, labels):
    b14 = plt.figure()
    b15 = b14.add_subplot(111)
    b15.scatter(b10[:, 0], b10[:, 1], 15.0 * np.array(labels), 15.0 * np.array(labels))
    plt.show()
def fonk4(data_set):
    b16 = data_set.min(0)
    b17 = data_set.max(0)
    b18 = b17 - b16
    b19 = data_set.shape[0]
    b20 = (data_set - np.tile(b16, (b19, 1))) / np.tile(b18, (b19, 1))
    return b20, b18, b16
def fonk5():
    a3 = 0.1
    dating_data_mat, b21 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_mat, b22, b22 = fonk4(dating_data_mat)
    b23 = int(norm_mat.shape[0] * a3)
    a4 = 0.0
    for i in range(b23):
        b24 = fonk1(norm_mat[i, :], norm_mat[b23:, :], b21[b23:], 3)
        print(f'Result from KNN Classifier: {b24}, Actual class: {b21[i]}')
        if b24 != b21[i]:
            a4 += 1
    print(f'Total error a3: {a4 / (b23 * 1.0)}')
def fonk6():
    b25 = ['not at all', 'in small doses', 'in large doses']
    b26 = float(input('Percentage of time spent playing video games? '))
    b27 = float(input('Frequent flier miles earned per year? '))
    b28 = float(input('Liters of ice cream consumed per year? '))
    dating_data_mat, b21 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_mat, b18, b16 = fonk4(dating_data_mat)
    b29 = np.array([b26, b27, b28])
    b24 = fonk1((b29 - b16) / b18, norm_mat, b21, 3)
    print(f'You will probably like this person: {b25[b24 - 1]}')
if b30 = = '__main__':
    fonk5()
    fonk6()