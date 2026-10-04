import math
import numpy as np
def fonk1(filename: str) -> np.array:
    b1 = []
    with open(filename, "r") as file:
        b2 = file.readlines()
        for line in b2:
            b1.append([float(word) for word in line.split('\t')] + [0])
    return np.asarray(b1)
def fonk2(X: np.array, M: np.array) -> float:
    a1 = 0.0
    for x in X:
        a1 += np.linalg.norm(x[:-1] - M[int(x[-1])])
    return (1.0 / X.shape[0]) * a1
def fonk3(X: np.array, M: np.array) -> np.array:
    b3 = np.zeros(M.shape)
    b4 = [0 for _ in range(M.shape[0])]
    for x in X:
        b5 = int(x[-1])
        b3[b5] += x[:-1]
        b4[b5] += 1
    for i in range(M.shape[0]):
        b3[i] /= b4[i] if b4[i] != 0 else 1
    return b3
def fonk4(X: np.array, M: np.array) -> np.array:
    for i in range(X.shape[0]):
        b6 = np.asarray([n for n in X[i][:-1]])
        b7 = float("inf")
        b5 = 0
        for idx, centroid in enumerate(M):
            b8 = np.linalg.norm(b6 - centroid)
            if b8 < b7:
                b7 = b8
                X[i][-1] = b5
            b5 += 1
    return X