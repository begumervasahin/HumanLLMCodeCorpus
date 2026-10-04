
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
def fonk1(unlabeled_sample, b9, b10, k):
    b1 = b9.shape[0]
    b2 = np.linalg.norm(np.tile(unlabeled_sample, (b1, 1)) - b9, axis=1)
    b3 = np.argsort(b2)
    b4 = {}
    for i in range(k):
        b5 = b10[b3[i]]
        b4[b5] = b4.get(b5, 0) + 1
    return max(b4.items(), b6 = itemgetter(1))[0]
def fonk2(filename, num_features):
    with open(filename) as file:
        b7 = file.readlines()
    b8 = len(b7)
    b9 = np.zeros((b8, num_features))
    b10 = []
    for index, b11 in enumerate(b7):
        b11 = b11.strip()
        b12 = b11.split('\t')
        b9[index, :] = b12[:num_features]
        b10.append(int(b12[-1]))
    return b9, b10
def fonk3(data_matrix, b10):
    plt.figure()
    plt.scatter(data_matrix[:, 0], data_matrix[:, 1],
                b13 = 15.0 * np.array(b10),
                b14 = 15.0 * np.array(b10))
    plt.show()
def fonk4(b9):
    b15 = b9.min(0)
    b16 = b9.max(0)
    b17 = b16 - b15
    b18 = (b9 - b15) / b17
    return b18, b17, b15
def fonk5():
    a1 = 0.1
    b9, b10 = fonk2('datingTestSet2.txt', 3)
    b18, b17, b15 = fonk4(b9)
    b19 = int(b18.shape[0] * a1)
    a2 = 0.0
    for i in range(b19):
        b20 = fonk1(b18[i, :],
                                b18[b19:],
                                b10[b19:],
                                3)
        print(f'Result from KNN Classifier: {b20}, Actual class: {b10[i]}')
        if b20 != b10[i]:
            a2 += 1
    print(f'Total error rate: {a2 / b19:.2f}')
def fonk6():
    b21 = ['not at all', 'in small doses', 'in large doses']
    b22 = float(input('Percentage of time spent playing video games? '))
    b23 = float(input('Frequent flier miles earned per year? '))
    b24 = float(input('Liters of ice cream consumed per year? '))
    b9, b10 = fonk2('datingTestSet2.txt', 3)
    b18, b17, b15 = fonk4(b9)
    b25 = np.array([b22, b23, b24])
    b26 = (b25 - b15) / b17
    b20 = fonk1(b26, b18, b10, 3)
    print(f'You will probably like this person: {b21[b20 - 1]}')
if b27 = = '__main__':
    fonk6()