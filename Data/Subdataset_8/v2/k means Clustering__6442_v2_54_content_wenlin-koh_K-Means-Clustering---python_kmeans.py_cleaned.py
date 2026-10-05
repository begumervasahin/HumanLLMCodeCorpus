import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append([float(word) for word in line.split('\t')])
    return np.asarray(data)
def compute_error(dataset: np.array, centroids: np.array) -> float:
    total_error = 0.0
    for point in dataset:
        centroid_index = int(point[-1])
        total_error += np.linalg.norm(point[:-1] - centroids[centroid_index])
    return (1.0 / dataset.shape[0]) * total_error
def update_centroids(dataset: np.array, centroids: np.array) -> np.array:
    new_centroids = np.zeros(centroids.shape)
    cluster_counts = [0 for _ in range(centroids.shape[0])]
    for point in dataset:
        cluster_id = int(point[-1])
        new_centroids[cluster_id] += point[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(centroids.shape[0]):
        new_centroids[i] = new_centroids[i] / cluster_counts[i] if cluster_counts[i] != 0 else centroids[i]
    return new_centroids
def assign_clusters(dataset: np.array, centroids: np.array) -> np.array:
    for i in range(dataset.shape[0]):
        point = dataset[i][:-1]
        shortest_distance = float("inf")
        closest_cluster_id = 0
        for j, centroid in enumerate(centroids):
            distance = np.linalg.norm(point - centroid)
            if distance < shortest_distance:
                shortest_distance = distance
                dataset[i][-1] = closest_cluster_id
            closest_cluster_id += 1
    return dataset
