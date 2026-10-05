import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append([float(word) for word in line.split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.array, M: np.array) -> float:
    total_error = 0.0
    for x in X:
        cluster_id = int(x[-1])
        total_error += np.linalg.norm(x[:-1] - M[cluster_id])
    return (1.0 / X.shape[0]) * total_error
def calculate_mean(X: np.array, M: np.array) -> np.array:
    new_centroids = np.zeros(M.shape)
    cluster_counts = [0 for _ in range(M.shape[0])]
    for x in X:
        cluster_id = int(x[-1])
        new_centroids[cluster_id] += x[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(M.shape[0]):
        if cluster_counts[i] != 0:
            new_centroids[i] /= cluster_counts[i]
    return new_centroids
def group_data(X: np.array, M: np.array) -> np.array:
    for i in range(X.shape[0]):
        point = X[i][:-1]
        shortest_distance = float("inf")
        closest_cluster = 0
        for idx, centroid in enumerate(M):
            distance = np.linalg.norm(point - centroid)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_cluster = idx
        X[i][-1] = closest_cluster
    return X