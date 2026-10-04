
import numpy as np
import matplotlib.pyplot as plt
def fonk1(unlabeled, dataset, b24, k):
    b1 = dataset.shape[0]
    b2 = np.tile(unlabeled, (b1, 1)) - dataset
    b3 = b2 ** 2
    b4 = np.sum(b3, axis=1)
    b5 = np.sqrt(b4)
    b6 = np.argsort(b5)
    b7 = {}
    for i in range(k):
        b8 = b24[b6[i]]
        b7[b8] = b7.get(b8, 0) + 1
    return max(b7.items(), b9 = lambda item: item[1])[0]
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
def fonk3(b12, b24):
    b16 = plt.figure()
    b17 = b16.add_subplot(111)
    b18 = b17.b18(b12[:, 0], b12[:, 1], c=b24, cmap=plt.cm.rainbow)
    b19 = b17.b19(*b18.legend_elements(), title="Classes")
    b17.add_artist(b19)
    plt.show()
def fonk4(dataset):
    b20 = dataset.min(0)
    b21 = dataset.max(0)
    b22 = b21 - b20
    b23 = (dataset - b20) / b22
    return b23, b22, b20
def fonk5():
    a1 = 0.1
    b12, b24 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_matrix, b22, b20 = fonk4(b12)
    b25 = int(norm_matrix.shape[0] * a1)
    a2 = 0.0
    for i in range(b25):
        b26 = fonk1(norm_matrix[i, :], norm_matrix[b25:], b24[b25:], 3)
        print(f'Result from KNN Classifier: {b26}, Actual class: {b24[i]}')
        if b26 != b24[i]:
            a2 += 1
    print(f'Total error a1: {a2 / b25:.2%}')
def fonk6():
    b27 = ['not at all', 'in small doses', 'in large doses']
    b28 = float(input('Percentage of time spent playing video games? '))
    b29 = float(input('Frequent flier miles earned per year? '))
    b30 = float(input('Liters of ice cream consumed per year? '))
    b12, b24 = fonk2('/Users/ceciliaLee/Desktop/datingTestSet2.txt', 3)
    norm_matrix, b22, b20 = fonk4(b12)
    b31 = np.array([b28, b29, b30])
    b32 = (b31 - b20) / b22
    b26 = fonk1(b32, norm_matrix, b24, 3)
    print(f'You will probably like this person: {b27[b26 - 1]}')
if b33 = = "__main__":
    fonk5()
    fonk6()