import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append([float(value) for value in line.strip().split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.array, M: np.array) -> float:
    error = 0.0
    for x in X:
        error += np.linalg.norm(x[:-1] - M[int(x[-1])])
    return error / X.shape[0]
def calculate_mean(X: np.array, M: np.array) -> np.array:
    new_centroids = np.zeros(M.shape)
    counts = np.zeros(M.shape[0])
    for x in X:
        cluster_id = int(x[-1])
        new_centroids[cluster_id] += x[:-1]
        counts[cluster_id] += 1
    for i in range(M.shape[0]):
        if counts[i] > 0:
            new_centroids[i] /= counts[i]
    return new_centroids
def group_data(X: np.array, M: np.array) -> np.array:
    for i in range(X.shape[0]):
        point = X[i][:-1]
        shortest_distance = float("inf")
        cluster_id = 0
        for idx, centroid in enumerate(M):
            distance = np.linalg.norm(point - centroid)
            if distance < shortest_distance:
                shortest_distance = distance
                X[i][-1] = idx
    return X