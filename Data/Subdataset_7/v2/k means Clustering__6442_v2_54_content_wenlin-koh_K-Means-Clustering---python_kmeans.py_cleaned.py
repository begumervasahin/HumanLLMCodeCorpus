import numpy as np
def fonk1(filename: str) -> np.array:
    b1 = []
    with open(filename, "r") as file:
        for line in file.readlines():
            b1.append([float(word) for word in line.split('\t')])
    return np.asarray(b1)
def fonk2(dataset: np.array, centroids: np.array) -> float:
    a1 = 0.0
    for b6 in dataset:
        b2 = int(b6[-1])
        a1 += np.linalg.norm(b6[:-1] - centroids[b2])
    return (1.0 / dataset.shape[0]) * a1
def fonk3(dataset: np.array, centroids: np.array) -> np.array:
    b3 = np.zeros(centroids.shape)
    b4 = [0 for _ in range(centroids.shape[0])]
    for b6 in dataset:
        b5 = int(b6[-1])
        b3[b5] += b6[:-1]
        b4[b5] += 1
    for i in range(centroids.shape[0]):
        b3[i] = b3[i] / b4[i] if b4[i] != 0 else centroids[i]
    return b3
def fonk4(dataset: np.array, centroids: np.array) -> np.array:
    for i in range(dataset.shape[0]):
        b6 = dataset[i][:-1]
        b7 = float("inf")
        a2 = 0
        for j, centroid in enumerate(centroids):
            b8 = np.linalg.norm(b6 - centroid)
            if b8 < b7:
                b7 = b8
                dataset[i][-1] = a2
            a2 += 1
    return dataset
