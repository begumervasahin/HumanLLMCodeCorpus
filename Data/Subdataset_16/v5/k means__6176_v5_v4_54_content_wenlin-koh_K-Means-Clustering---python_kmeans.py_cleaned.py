import numpy as np
def fonk1(filename: str) -> np.array:
    b1 = []
    with open(filename, "r") as file:
        b2 = file.readlines()
        for line in b2:
            b1.append([float(value) for value in line.strip().split('\t')] + [0])
    return np.asarray(b1)
def fonk2(b1: np.array, centroids: np.array) -> float:
    a1 = 0.0
    for b7 in b1:
        b3 = int(b7[-1])
        a1 += np.linalg.norm(b7[:-1] - centroids[b3])
    return a1 / b1.shape[0]
def fonk3(b1: np.array, centroids: np.array) -> np.array:
    b4 = np.zeros_like(centroids)
    b5 = np.zeros(centroids.shape[0])
    for b7 in b1:
        b6 = int(b7[-1])
        b4[b6] += b7[:-1]
        b5[b6] += 1
    for i in range(centroids.shape[0]):
        if b5[i] > 0:
            b4[i] /= b5[i]
    return b4
def fonk4(b1: np.array, centroids: np.array) -> np.array:
    for i in range(b1.shape[0]):
        b7 = b1[i][:-1]
        b8 = np.linalg.norm(b7 - centroids, axis=1)
        b1[i][-1] = np.argmin(b8)
    return b1