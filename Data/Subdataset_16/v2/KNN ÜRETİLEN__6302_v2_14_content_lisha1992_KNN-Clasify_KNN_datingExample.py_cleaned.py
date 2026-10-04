
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
def fonk1(unlabeled_sample, b12, b13, k):
    b1 = b12.shape[0]
    b2 = np.tile(unlabeled_sample, (b1, 1)) - b12
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = b13[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = sorted(b7.items(), key=itemgetter(1), reverse=True)
    return b9[0][0]
def fonk2(filename, num_features):
    with open(filename) as file:
        b10 = file.readlines()
    b11 = len(b10)
    b12 = np.zeros((b11, num_features))
    b13 = []
    for index, b14 in enumerate(b10):
        b14 = b14.strip()
        b15 = b14.split('\t')
        b12[index, :] = b15[:num_features]
        b13.append(int(b15[-1]))
    return b12, b13
def fonk3(data_matrix, b13):
    plt.figure()
    plt.scatter(data_matrix[:, 0], data_matrix[:, 1],
                b16 = 15.0 * np.array(b13),
                b17 = 15.0 * np.array(b13))
    plt.show()
def fonk4(b12):
    b18 = b12.min(0)
    b19 = b12.max(0)
    b20 = b19 - b18
    b21 = (b12 - b18) / b20
    return b21, b20, b18
def fonk5():
    a1 = 0.1
    b12, b13 = fonk2('datingTestSet2.txt', 3)
    b21, b20, b18 = fonk4(b12)
    b22 = int(b21.shape[0] * a1)
    a2 = 0.0
    for i in range(b22):
        b23 = fonk1(b21[i, :],
                                b21[b22:],
                                b13[b22:],
                                3)
        print(f'Result from KNN Classifier: {b23}, Actual class: {b13[i]}')
        if b23 != b13[i]:
            a2 += 1
    print(f'Total error rate: {a2 / b22:.2f}')
def fonk6():
    b24 = ['not at all', 'in small doses', 'in large doses']
    b25 = float(input('Percentage of time spent playing video games? '))
    b26 = float(input('Frequent flier miles earned per year? '))
    b27 = float(input('Liters of ice cream consumed per year? '))
    b12, b13 = fonk2('datingTestSet2.txt', 3)
    b21, b20, b18 = fonk4(b12)
    b28 = np.array([b25, b26, b27])
    b29 = (b28 - b18) / b20
    b23 = fonk1(b29, b21, b13, 3)
    print(f'You will probably like this person: {b24[b23 - 1]}')
if b30 = = '__main__':
    fonk6()