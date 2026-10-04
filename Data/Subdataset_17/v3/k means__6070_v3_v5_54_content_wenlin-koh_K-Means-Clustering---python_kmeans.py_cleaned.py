import numpy as np
def load_data(filename: str) -> np.array:
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append([float(value) for value in line.split('\t')] + [0])
    return np.asarray(data)
def compute_error(X: np.array, centroids: np.array) -> float:
    total_error = 0.0
    for point in X:
        cluster_id = int(point[-1])
        total_error += np.linalg.norm(point[:-1] - centroids[cluster_id])
    return total_error / X.shape[0]
def calculate_new_centroids(X: np.array, centroids: np.array) -> np.array:
    new_centroids = np.zeros(centroids.shape)
    cluster_counts = np.zeros(centroids.shape[0], dtype=int)
    for point in X:
        cluster_id = int(point[-1])
        new_centroids[cluster_id] += point[:-1]
        cluster_counts[cluster_id] += 1
    for i in range(centroids.shape[0]):
        if cluster_counts[i] > 0:
            new_centroids[i] /= cluster_counts[i]
    return new_centroids
def assign_clusters(X: np.array, centroids: np.array) -> np.array:
    for point in X:
        distances = np.linalg.norm(point[:-1] - centroids, axis=1)
        point[-1] = np.argmin(distances)
    return X
def kmeans_clustering(filename: str, num_clusters: int, max_iterations: int = 100) -> (np.array, float):
    X = load_data(filename)
    initial_centroids_idx = np.random.choice(X.shape[0], num_clusters, replace=False)
    centroids = X[initial_centroids_idx, :-1]
    for iteration in range(max_iterations):
        X = assign_clusters(X, centroids)
        new_centroids = calculate_new_centroids(X, centroids)
        if np.allclose(centroids, new_centroids):
            print(f"Converged after {iteration} iterations.")
            break
        centroids = new_centroids
    error = compute_error(X, centroids)
    return centroids, error
if __name__ == "__main__":
    filename = "data.txt"
    num_clusters = 3
    centroids, error = kmeans_clustering(filename, num_clusters)
    print("Final centroids:")
    print(centroids)
    print("Final error:")
    print(error)