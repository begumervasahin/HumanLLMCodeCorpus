import numpy as np
def fonk1(unlabeled_data, dataset, labels, k):
    b1 = np.sqrt(np.sum((np.tile(unlabeled_data, (dataset.shape[0], 1)) - dataset) ** 2, axis=1))
    b2 = np.argsort(b1)
    b3 = {}
    for i in range(k):
        b4 = labels[b2[i]]
        b3[b4] = b3.get(b4, 0) + 1
    b5 = max(b3, key=b3.get)
    return b5
def fonk2(filename, b22):
    b6 = np.loadtxt(filename)
    return b6[:, :b22], b6[:, -1].astype(int)
def fonk3(dataset):
    b7 = dataset.min(0)
    b8 = dataset.max(0)
    b9 = b8 - b7
    b10 = (dataset - b7) / b9
    return b10, b9, b7
def fonk4(filename, b22, b11 = 0.1, k=3):
    dating_data, b12 = fonk2(filename, b22)
    norm_data, b13, b13 = fonk3(dating_data)
    b14 = int(norm_data.shape[0] * b11)
    a1 = 0.0
    for i in range(b14):
        b15 = fonk1(norm_data[i], norm_data[b14:], b12[b14:], k)
        print(f"Result from KNN Classifier class1: {b15}, the actual class class1: {b12[i]}")
        if b15 != b12[i]:
            a1 += 1
    print(f"The total error b11 class1: {a1 / b14}")
def fonk5(filename, b22):
    b16 = ['not at all', 'in small doses', 'in large doses']
    b17 = float(input('Percentage of time spent playing video games? '))
    b18 = float(input('Frequent flier miles earned per year? '))
    b19 = float(input('Liters of ice cream consumed per year? '))
    dating_data, b12 = fonk2(filename, b22)
    norm_data, b9, b7 = fonk3(dating_data)
    b20 = np.array([b17, b18, b19])
    b15 = fonk1((b20 - b7) / b9, norm_data, b12, 3)
    print(f'You will probably like this person: {b16[b15 - 1]}')
if b21 = = '__main__':
    fonk4('datingTestSet2.txt', b22 = 3)
    fonk5('datingTestSet2.txt', b22 = 3)