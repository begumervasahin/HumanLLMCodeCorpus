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
    return (iterations > MAX_ITERATIONS) or np.array_equal(old_centroids, centroids)
def get_random_centroids(data_set, centroids, k):
    for _ in range(k):
        centroids.append(data_set[np.random.randint(0, len(data_set), size=1)])
    return centroids
def get_clusters(data_set, centroids, k):
    clusters = [[] for _ in range(k)]
    for x in data_set:
        best = centroids.index(min(centroids, key=lambda c: euclidean_distance(x, c)))
        clusters[best] += [x]
    return clusters
def calculate_new_centroids(clusters, data_set, k):
    new_centroids = [[] for _ in range(k)]
    for i, cluster in enumerate(clusters):
        if not cluster:
            new_centroids[i] = data_set[np.random.randint(0, len(data_set), size=1)]
        else:
            new_centroids[i] = np.mean(cluster, axis=0).tolist()
    return new_centroids
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y)**2))
data_set = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
k = 2
centroids, clusters, iterations = run(data_set, k)
print("Centroids:")
print(centroids)
print("Clusters:")
print(clusters)
print("Number of iterations:", iterations)