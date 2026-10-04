import numpy as np
import operator
a1 = 1
a2 = 2
b1 = a1 + a2
print(b1)
a2 = np.array([6, 7, 8])
b1 = a2.shape[0]
print(b1)
a1 = np.sum([[0, 1, 2], [2, 1, 3]])
print(a1)
a1 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(a1)
a1 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(a1)
b2 = a1.argsort()
print(b2)
b3 = {"A": 6, "B": 1, "C": 0, "D": 2}
b4 = sorted(b3.items(), key=operator.itemgetter(1), reverse=True)
print(b4)
b5 = np.array([[5, 8], [1, 2]])
def fonk1(matrix):
    rows, b6 = matrix.shape
    b7 = np.zeros((1, rows * b6))
    for i in range(rows):
        for j in range(b6):
            b7[0, b6 * i + j] = int(matrix[i, j])
    return b7
b7 = np.zeros((1, 4))
print(b7[0, 1])
