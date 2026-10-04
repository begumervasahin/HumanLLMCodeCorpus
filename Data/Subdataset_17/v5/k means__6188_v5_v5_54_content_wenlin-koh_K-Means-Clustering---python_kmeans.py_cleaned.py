import numpy as np
def load_data(filename: str) -> np.ndarray:
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.ndarray, centroids: np.ndarray) -> float:
    total_error = 0.0
    for point in X:
        cluster_id = int(point[-1])
        total_error += np.linalg.norm(point[:-1] - centroids[cluster_id])
    return total_error / X.shape[0]
def calculate_new_centroids(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    new_centroids = np.zeros(centroids.shape)
    cluster_counts = np.zeros(centroids.shape[0])
    for point in X:
        cluster_id = int(point[-1])
        new_centroids[cluster_id] += point[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(centroids.shape[0]):
        if cluster_counts[i] > 0:
            new_centroids[i] /= cluster_counts[i]
    return new_centroids
def assign_clusters(X: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    for i, point in enumerate(X):
        shortest_distance = float("inf")
        closest_cluster = -1
        for cluster_id, centroid in enumerate(centroids):
            distance = np.linalg.norm(point[:-1] - centroid)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_cluster = cluster_id
        X[i][-1] = closest_cluster
    return X