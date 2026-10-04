
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
def fonk1(unlabeled, dataset, b22, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabeled, (b1, 1)) - dataset
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = b22[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    a1 = 0
    b9 = None
    for key, value in b7.items():
        if value > a1:
            a1 = value
            b9 = key
    return b9
def fonk2(filename, num_features):
    with open(filename) as fr:
        b10 = fr.readlines()
    b11 = len(b10)
    b12 = np.zeros((b11, num_features))
    b13 = []
    for index, b14 in enumerate(b10):
        b14 = b14.strip()
        b15 = b14.split('\t')
        b12[index, :] = b15[:num_features]
        b13.append(int(b15[-1]))
    return b12, b13
def fonk3(b12, b22):
    b16 = plt.figure()
    b17 = b16.add_subplot(111)
    b17.scatter(b12[:, 0], b12[:, 1], 15.0 * np.array(b22), 15.0 * np.array(b22))
    plt.show()
def fonk4(dataset):
    b18 = dataset.min(0)
    b19 = dataset.max(0)
    b20 = b19 - b18
    b21 = (dataset - b18) / b20
    return b21, b20, b18
def fonk5():
    a2 = 0.1
    b12, b22 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_matrix, b20, b18 = fonk4(b12)
    b23 = int(norm_matrix.shape[0] * a2)
    a3 = 0.0
    for i in range(b23):
        b24 = fonk1(norm_matrix[i, :], norm_matrix[b23:], b22[b23:], 3)
        print(f'Result from KNN Classifier: {b24}, Actual class: {b22[i]}')
        if b24 != b22[i]:
            a3 += 1
    print(f'Total error a2: {a3 / b23:.2f}')
def fonk6():
    b25 = ['not at all', 'in small doses', 'in large doses']
    b26 = float(input('Percentage of time spent playing video games? '))
    b27 = float(input('Frequent flier miles earned per year? '))
    b28 = float(input('Liters of ice cream consumed per year? '))
    b12, b22 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_matrix, b20, b18 = fonk4(b12)
    b29 = np.array([b26, b27, b28])
    b30 = (b29 - b18) / b20
    b24 = fonk1(b30, norm_matrix, b22, 3)
    print(f'You will probably like this person: {b25[b24 - 1]}')
if b31 = = "__main__":
    fonk5()
    fonk6()