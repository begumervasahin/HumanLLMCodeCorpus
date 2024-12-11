import matplotlib.pyplot as plt
import numpy as np
def fonk1(b9, b10, b11, b12, b13, b14, b1 = True):
    fig, b2 = plt.subplots()
    b3 = [(b9, b10), (b11, b12), (b13, b14)]
    b4 = ['b', 'g', 'r']
    b5 = ['o', 'x']
    for dataset, labels, color in zip(b3, b4):
        b6 = np.where(labels == 1)[0]
        b7 = np.where(labels == 0)[0]
        if b6.size > 0:
            b2.scatter(dataset[b6, 0], dataset[b6, 1], b8 = 'o', c=color)
        if b7.size > 0:
            b2.scatter(dataset[b7, 0], dataset[b7, 1], b8 = 'x', c=color)
    plt.show(b1 = b1)
b9 = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
b10 = np.array([1, 0, 1, 0, 1])
b11 = np.array([[2, 3], [4, 5]])
b12 = np.array([0, 0])
b13 = np.array([[1, 2], [3, 4], [5, 6]])
b14 = np.array([1, 1, 1])
fonk1(b9, b10, b11, b12, b13, b14)