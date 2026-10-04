import numpy as np
import operator
a1 = 1
a2 = 2
b1 = a1 + a2
print(b1)
b2 = np.array([6, 7, 8])
b3 = b2.shape[0]
print(b3)
b4 = np.sum([[0, 1, 2], [2, 1, 3]])
print(b4)
b5 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
print(b5)
b6 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
print(b6)
b7 = b6.argsort()
print(b7)
b8 = {"A": 6, "B": 1, "C": 0, "D": 2}
b9 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
print(b9)
b10 = np.array([[5, 8], [1, 2]])
def fonk1(matrix):
    rows, b11 = matrix.shape
    b12 = np.zeros((1, rows * b11))
    for i in range(rows):
        for j in range(b11):
            b12[0, b11 * i + j] = int(matrix[i, j])
    return b12
b13 = fonk1(b10)
print(b13)
b14 = np.zeros((1, 4))
print(b14[0, 1])
