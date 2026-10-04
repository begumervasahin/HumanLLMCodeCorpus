import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append([float(value) for value in line.strip().split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.array, centroids: np.array) -> float:
    total_error = 0.0
    for x in X:
        cluster_id = int(x[-1])
        total_error += np.linalg.norm(x[:-1] - centroids[cluster_id])
    return total_error / X.shape[0]
def calculate_mean(X: np.array, centroids: np.array) -> np.array:
    new_centroids = np.zeros(centroids.shape)
    cluster_counts = np.zeros(centroids.shape[0])
    for x in X:
        cluster_id = int(x[-1])
        new_centroids[cluster_id] += x[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(centroids.shape[0]):
        if cluster_counts[i] != 0:
            new_centroids[i] /= cluster_counts[i]
        else:
            new_centroids[i] = centroids[i]
    return new_centroids
def group_data(X: np.array, centroids: np.array) -> np.array:
    for x in X:
        distances = np.linalg.norm(x[:-1] - centroids, axis=1)
        nearest_cluster_id = np.argmin(distances)
        x[-1] = nearest_cluster_id
    return X
def k_means_clustering(filename: str, k: int, iterations: int) -> tuple:
    data = load_data(filename)
    initial_indices = np.random.choice(data.shape[0], k, replace=False)
    centroids = data[initial_indices, :-1]
    for _ in range(iterations):
        data = group_data(data, centroids)
        centroids = calculate_mean(data, centroids)
    final_error = compute_error(data, centroids)
    print(f"Final clustering error: {final_error}")
    return data, centroids
if __name__ == "__main__":
    FILENAME = "data.txt"
    K = 3
    ITERATIONS = 100
    clustered_data, centroids = k_means_clustering(FILENAME, K, ITERATIONS)
    print("Clustered Data:\n", clustered_data)
    print("Centroids:\n", centroids)