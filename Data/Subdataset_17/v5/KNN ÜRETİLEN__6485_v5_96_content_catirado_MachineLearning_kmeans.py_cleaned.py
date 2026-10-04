import numpy as np
import math
MAX_ITERATIONS = 100
def run(data_set, k):
    iterations = 0
    centroids = get_random_centroids(data_set, k)
    old_centroids = np.zeros_like(centroids)
    while not has_converged(old_centroids, centroids, iterations):
        old_centroids = centroids.copy()
        iterations += 1
        clusters = assign_clusters(data_set, centroids)
        centroids = calculate_new_centroids(clusters, data_set, k)
    return centroids, clusters, iterations
def has_converged(old_centroids, centroids, iterations):
    return iterations > MAX_ITERATIONS or np.array_equal(old_centroids, centroids)
def get_random_centroids(data_set, k):
    indices = np.random.choice(len(data_set), k, replace=False)
    return data_set[indices]
def assign_clusters(data_set, centroids):
    clusters = [[] for _ in centroids]
    for point in data_set:
        closest_centroid_idx = np.argmin([euclidean_distance(point, centroid) for centroid in centroids])
        clusters[closest_centroid_idx].append(point)
    return clusters
def calculate_new_centroids(clusters, data_set, k):
    new_centroids = []
    for cluster in clusters:
        if cluster:
            new_centroids.append(np.mean(cluster, axis=0))
        else:
            new_centroids.append(data_set[np.random.randint(0, len(data_set))])
    return np.array(new_centroids)
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))
if __name__ == "__main__":
    data = np.array([
        [1.0, 2.0],
        [1.5, 1.8],
        [5.0, 8.0],
        [8.0, 8.0],
        [1.0, 0.6],
        [9.0, 11.0],
        [8.0, 2.0],
        [10.0, 2.0],
        [9.0, 3.0]
    ])
    k = 3
    centroids, clusters, iterations = run(data, k)
    print(f"Centroids:\n{centroids}")
    print(f"Iterations: {iterations}")