import numpy as np
def fonk1(filename: str) -> np.array:
    b1 = []
    with open(filename, "r") as file:
        for line in file.readlines():
            b1.append([float(word) for word in line.split('\t')] + [0])
    return np.asarray(b1)
def fonk2(X: np.array, M: np.array) -> float:
    a1 = 0.0
    for x in X:
        b2 = int(x[-1])
        a1 += np.linalg.norm(x[:-1] - M[b2])
    return (1.0 / X.shape[0]) * a1
def fonk3(X: np.array, M: np.array) -> np.array:
    b3 = np.zeros(M.shape)
    b4 = [0 for _ in range(M.shape[0])]
    for x in X:
        b2 = int(x[-1])
        b3[b2] += x[:-1]
        b4[b2] += 1
    for i in range(M.shape[0]):
        if b4[i] != 0:
            b3[i] /= b4[i]
    return b3
def fonk4(X: np.array, M: np.array) -> np.array:
    for i in range(X.shape[0]):
        b5 = X[i][:-1]
        b6 = float("inf")
        a2 = 0
        for idx, centroid in enumerate(M):
            b7 = np.linalg.norm(b5 - centroid)
            if b7 < b6:
                b6 = b7
                a2 = idx
        X[i][-1] = a2
    return X