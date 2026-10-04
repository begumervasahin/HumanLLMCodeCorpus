import numpy as np
import operator
a1 = 1
a2 = 2
b1 = a1 + a2
print(b5"Sum of a1 and a2: {b1}")
a2 = np.array([6, 7, 8])
b1 = a2.shape[0]
print(b5"Shape of array a2: {b1}")
a1 = np.sum([[0, 1, 2], [2, 1, 3]])
print(b5"Sum of all elements: {a1}")
a1 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(b5"Sum along axis 0: {a1}")
a1 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(b5"Sum along axis 1: {a1}")
b2 = a1.argsort()
print(b5"Indices of sorted array a1: {b2}")
b3 = {"A": 6, "B": 1, "C": 0, "D": 2}
b4 = sorted(b3.items(), key=operator.itemgetter(1), reverse=True)
print(b5"Dictionary sorted by value: {b4}")
b5 = np.array([[5, 8], [1, 2]])
def fonk1(array):
    b6 = np.zeros((1, 4))
    for i in range(2):
        for j in range(2):
            b6[0, 2*i + j] = int(array[i, j])
    return b6
b6 = fonk1(b5)
print(b5"Converted vector: {b6[0, 1]}")