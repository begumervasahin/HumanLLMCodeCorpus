import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append([float(value) for value in line.strip().split('\t')] + [0])
    return np.asarray(data)
def compute_error(data: np.array, centroids: np.array) -> float:
    total_error = 0.0
    for point in data:
        centroid_idx = int(point[-1])
        total_error += np.linalg.norm(point[:-1] - centroids[centroid_idx])
    return total_error / data.shape[0]
def calculate_mean(data: np.array, centroids: np.array) -> np.array:
    new_centroids = np.zeros_like(centroids)
    counts = np.zeros(centroids.shape[0])
    for point in data:
        cluster_id = int(point[-1])
        new_centroids[cluster_id] += point[:-1]
        counts[cluster_id] += 1
    for i in range(centroids.shape[0]):
        if counts[i] > 0:
            new_centroids[i] /= counts[i]
    return new_centroids
def group_data(data: np.array, centroids: np.array) -> np.array:
    for i in range(data.shape[0]):
        point = data[i][:-1]
        distances = np.linalg.norm(point - centroids, axis=1)
        data[i][-1] = np.argmin(distances)
    return data