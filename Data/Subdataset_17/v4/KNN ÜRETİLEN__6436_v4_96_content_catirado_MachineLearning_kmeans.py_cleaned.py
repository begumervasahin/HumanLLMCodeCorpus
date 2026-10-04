import numpy as np
import math
MAX_ITERATIONS = 100
def run(data_set, k):
    iterations = 0
    centroids = []
    old_centroids = [[] for _ in range(k)]
    centroids = get_random_centroids(data_set, k)
    while not has_converged(old_centroids, centroids, iterations):
        old_centroids = centroids
        iterations += 1
        clusters = get_clusters(data_set, centroids, k)
        centroids = calculate_new_centroids(clusters, data_set, k)
    return centroids, clusters, iterations
def has_converged(old_centroids, centroids, iterations):
    return (iterations > MAX_ITERATIONS) or old_centroids == centroids
def get_random_centroids(data_set, k):
    return [data_set[np.random.randint(0, len(data_set))] for _ in range(k)]
def get_clusters(data_set, centroids, k):
    clusters = [[] for _ in range(k)]
    for x in data_set:
        closest_centroid = min(range(len(centroids)), key=lambda c: euclidean_distance(x, centroids[c]))
        clusters[closest_centroid].append(x)
    return clusters
def calculate_new_centroids(clusters, data_set, k):
    new_centroids = []
    for cluster in clusters:
        if not cluster:
            new_centroids.append(data_set[np.random.randint(0, len(data_set))])
        else:
            new_centroids.append(np.mean(cluster, axis=0).tolist())
    return new_centroids
def euclidean_distance(x, y):
    return math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))