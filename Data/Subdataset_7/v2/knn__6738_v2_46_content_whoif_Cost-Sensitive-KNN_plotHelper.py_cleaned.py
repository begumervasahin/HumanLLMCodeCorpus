import matplotlib.pyplot as plt
import numpy as np
def fonk1(b10, b11, b12, b13, b14, b15, b1 = True):
    b2 = plt.figure()
    b3 = b2.add_subplot(111)
    b4 = [b10, b12, b14]
    b5 = [b11, b13, b15]
    b6 = ['b', 'g', 'r']
    for dataset, b5, color in zip(b4, b5, b6):
        b7 = np.where(b5 == 1)[0]
        b8 = np.where(b5 == 0)[0]
        if b7.size > 0:
            b3.scatter(dataset[b7, 0], dataset[b7, 1], b9 = 'o', c=color)
        if b8.size > 0:
            b3.scatter(dataset[b8, 0], dataset[b8, 1], b9 = 'x', c=color)
    plt.show(b1 = b1)
b10 = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
b11 = np.array([1, 0, 1, 0, 1])
b12 = np.array([[2, 3], [4, 5]])
b13 = np.array([0, 0])
b14 = np.array([[1, 2], [3, 4], [5, 6]])
b15 = np.array([1, 1, 1])
fonk1(b10, b11, b12, b13, b14, b15)