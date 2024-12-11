import numpy as np
def fonk1(unlabeled_data, dataset, labels, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabeled_data, (b1, 1)) - dataset
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
def fonk2(filename, b26):
    b10 = np.loadtxt(filename)
    return b10[:, :b26], b10[:, -1].astype(int)
def fonk3(dataset):
    b11 = dataset.min(0)
    b12 = dataset.max(0)
    b13 = b12 - b11
    b14 = (dataset - b11) / b13
    return b14, b13, b11
def fonk4(filename, b26, b15 = 0.1, k=3):
    dating_data, b16 = fonk2(filename, b26)
    norm_data, b17, b17 = fonk3(dating_data)
    b18 = int(norm_data.shape[0] * b15)
    a2 = 0.0
    for i in range(b18):
        b19 = fonk1(norm_data[i, :], norm_data[b18:, :], b16[b18:], k)
        print(f"Result from KNN Classifier class1: {b19}, the actual class class1: {b16[i]}")
        if b19 != b16[i]:
            a2 += 1
    print(f"The total error b15 class1: {a2 / (b18 * 1.0)}")
def fonk5(filename, b26):
    b20 = ['not at all', 'in small doses', 'in large doses']
    b21 = float(input('Percentage of time spent playing video games? '))
    b22 = float(input('Frequent flier miles earned per year? '))
    b23 = float(input('Liters of ice cream consumed per year? '))
    dating_data, b16 = fonk2(filename, b26)
    norm_data, b13, b11 = fonk3(dating_data)
    b24 = np.array([b21, b22, b23])
    b19 = fonk1((b24 - b11) / b13, norm_data, b16, 3)
    print(f'You will probably like this person: {b20[b19 - 1]}')
if b25 = = '__main__':
    fonk4('datingTestSet2.txt', b26 = 3)
    fonk5('datingTestSet2.txt', b26 = 3)