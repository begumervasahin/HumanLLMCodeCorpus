import numpy as np
import operator
a1 = 1
a2 = 2
b1 = a1 + a2
print(f"Sum of a1 and a2: {b1}")
b2 = np.array([6, 7, 8])
b3 = b2.shape[0]
print(f"Shape of array a2: {b3}")
b4 = np.sum([[0, 1, 2], [2, 1, 3]])
print(f"Sum of all elements: {b4}")
b5 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(f"Sum along axis 0: {b5}")
b6 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(f"Sum along axis 1: {b6}")
b7 = b6.argsort()
print(f"Indices of sorted array along axis 1: {b7}")
b8 = {"A": 6, "B": 1, "C": 0, "D": 2}
b9 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
print(f"Dictionary sorted by value: {b9}")
b10 = np.array([[5, 8], [1, 2]])
def fonk1(array):
    b11 = array.shape[0] * array.shape[1]
    b12 = np.zeros((1, b11))
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            b12[0, array.shape[1]*i + j] = array[i, j]
    return b12
b13 = fonk1(b10)
print(f"Converted vector: {b13[0, 1]}")