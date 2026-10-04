import numpy as np
def load_data(filename: str) -> np.ndarray:
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.ndarray, M: np.ndarray) -> float:
    total_error = 0.0
    for x in X:
        cluster_id = int(x[-1])
        total_error += np.linalg.norm(x[:-1] - M[cluster_id])
    return total_error / X.shape[0]
def calculate_mean(X: np.ndarray, M: np.ndarray) -> np.ndarray:
    new_centroids = np.zeros(M.shape)
    cluster_counts = np.zeros(M.shape[0])
    for x in X:
        cluster_id = int(x[-1])
        new_centroids[cluster_id] += x[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(M.shape[0]):
        if cluster_counts[i] > 0:
            new_centroids[i] /= cluster_counts[i]
    return new_centroids
def group_data(X: np.ndarray, M: np.ndarray) -> np.ndarray:
    for i in range(X.shape[0]):
        point = X[i][:-1]
        shortest_distance = float("inf")
        closest_cluster = -1
        for idx, centroid in enumerate(M):
            distance = np.linalg.norm(point - centroid)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_cluster = idx
        X[i][-1] = closest_cluster
    return X