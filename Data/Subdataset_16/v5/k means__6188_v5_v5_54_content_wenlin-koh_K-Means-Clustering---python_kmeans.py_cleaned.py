import numpy as np
def fonk1(filename: str) -> np.ndarray:
    b1 = []
    with open(filename, "r") as file:
        for line in file:
            b1.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(b1)
def fonk2(X: np.ndarray, centroids: np.ndarray) -> float:
    a1 = 0.0
    for point in X:
        b2 = int(point[-1])
        a1 += np.linalg.norm(point[:-1] - centroids[b2])
    return a1 / X.shape[0]
def fonk3(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    b3 = np.zeros(centroids.shape)
    b4 = np.zeros(centroids.shape[0])
    for point in X:
        b2 = int(point[-1])
        b3[b2] += point[:-1]
        b4[b2] += 1
    for i in range(centroids.shape[0]):
        if b4[i] > 0:
            b3[i] /= b4[i]
    return b3
def fonk4(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    for i, point in enumerate(X):
        b5 = float("inf")
        a2 = -1
        for b2, centroid in enumerate(centroids):
            b6 = np.linalg.norm(point[:-1] - centroid)
            if b6 < b5:
                b5 = b6
                a2 = b2
        X[i][-1] = a2
    return X