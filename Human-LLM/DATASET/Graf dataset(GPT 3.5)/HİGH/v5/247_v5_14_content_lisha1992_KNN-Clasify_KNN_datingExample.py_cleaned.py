import numpy as np
import matplotlib.pyplot as plt
def fonk1(unlabeled_data, data_set, labels, k):
    b1 = data_set.shape[0]
    b2 = np.tile(unlabeled_data, (b1, 1)) - data_set
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = labels[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    a1 = 0
    b9 = None
    for key, value in b7.items():
        if value > a1:
            a1 = value
            b9 = key
    return b9
def fonk2(filename, dim):
    b10 = np.loadtxt(filename, delimiter='\t', usecols=range(dim))
    b11 = np.loadtxt(filename, delimiter='\t', usecols=dim, dtype=int)
    return b10, b11
def fonk3(b10, labels):
    plt.scatter(b10[:, 0], b10[:, 1], b12 = 15.0 * np.array(labels), c=15.0 * np.array(labels))
    plt.show()
def fonk4(data_set):
    b13 = np.min(data_set, axis=0)
    b14 = np.max(data_set, axis=0)
    b15 = b14 - b13
    b16 = (data_set - b13) / b15
    return b16, b15, b13
def fonk5():
    a2 = 0.1
    dating_data_mat, b17 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_mat, b18, b18 = fonk4(dating_data_mat)
    b19 = int(norm_mat.shape[0] * a2)
    a3 = 0
    for i in range(b19):
        b20 = fonk1(norm_mat[i, :], norm_mat[b19:, :], b17[b19:], 3)
        print(f'Result from KNN Classifier: {b20}, Actual class: {b17[i]}')
        if b20 != b17[i]:
            a3 += 1
    b21 = a3 / b19
    print(f'Total error a2: {b21:.2%}')
def fonk6():
    b22 = ['not at all', 'in small doses', 'in large doses']
    b23 = float(input('Percentage of time spent playing video games? '))
    b24 = float(input('Frequent flier miles earned per year? '))
    b25 = float(input('Liters of ice cream consumed per year? '))
    dating_data_mat, b17 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_mat, b15, b13 = fonk4(dating_data_mat)
    b26 = np.array([b23, b24, b25])
    b27 = (b26 - b13) / b15
    b20 = fonk1(b27, norm_mat, b17, 3)
    print(f'You will probably like this person: {b22[b20 - 1]}')
if b28 = = '__main__':
    fonk5()
    fonk6()