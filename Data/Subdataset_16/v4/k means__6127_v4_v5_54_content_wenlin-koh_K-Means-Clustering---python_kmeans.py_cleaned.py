import numpy as np
def fonk1(filename: str) -> np.ndarray:
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            b1.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(b1)
def fonk2(X: np.ndarray, M: np.ndarray) -> float:
    a1 = 0.0
    for x in X:
        b2 = int(x[-1])
        a1 += np.linalg.norm(x[:-1] - M[b2])
    return a1 / X.shape[0]
def fonk3(X: np.ndarray, M: np.ndarray) -> np.ndarray:
    b3 = np.zeros(M.shape)
    b4 = np.zeros(M.shape[0])
    for x in X:
        b2 = int(x[-1])
        b3[b2] += x[:-1]
        b4[b2] += 1
    for i in range(M.shape[0]):
        if b4[i] > 0:
            b3[i] /= b4[i]
    return b3
def fonk4(X: np.ndarray, M: np.ndarray) -> np.ndarray:
    for i in range(X.shape[0]):
        b5 = X[i][:-1]
        b6 = float("inf")
        a2 = -1
        for idx, centroid in enumerate(M):
            b7 = np.linalg.norm(b5 - centroid)
            if b7 < b6:
                b6 = b7
                a2 = idx
        X[i][-1] = a2
    return X