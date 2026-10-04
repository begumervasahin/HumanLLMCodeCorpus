import numpy as np
import math
MAX_ITERATIONS = 100
def run(data_set, k):
    iterations = 0
    centroids = []
    old_centroids = [[] for _ in range(k)]
    centroids = get_random_centroids(data_set, centroids, k)
    while not has_converged(old_centroids, centroids, iterations):
        old_centroids = centroids
        iterations += 1
        clusters = get_clusters(data_set, centroids, k)
        centroids = calculate_new_centroids(clusters, data_set, k)
    return centroids, clusters, iterations
def has_converged(old_centroids, centroids, iterations):
    return (iterations > MAX_ITERATIONS) or old_centroids == centroids
def get_random_centroids(data_set, centroids, k):
    for _ in range(k):
        centroids.append(data_set[np.random.randint(0, len(data_set))].tolist())
    return centroids
def get_clusters(data_set, centroids, k):
    clusters = [[] for _ in range(k)]
    for x in data_set:
        best = centroids.index(min(centroids, key=lambda c: euclidean_distance(x, c)))
        clusters[best].append(x)
    return clusters
def calculate_new_centroids(clusters, data_set, k):
    new_centroids = [[] for _ in range(k)]
    for i, cluster in enumerate(clusters):
        if not cluster:
            new_centroids[i] = data_set[np.random.randint(0, len(data_set))].tolist()
        else:
            new_centroids[i] = np.mean(cluster, axis=0).tolist()
    return new_centroids
def euclidean_distance(x, y):
    return math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))
if __name__ == "__main__":
    data_set = np.array([
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ])
    k = 3
    centroids, clusters, iterations = run(data_set, k)
    print("Centroids:")
    print(centroids)
    print("\nClusters:")
    for cluster in clusters:
        print(cluster)
    print("\nIterations:")
    print(iterations)