import numpy as np
import math
MAX_ITERATIONS = 100
def kmeans_clustering(data_set, k):
    iterations = 0
    centroids = get_random_centroids(data_set, k)
    old_centroids = [[] for _ in range(k)]
    while not has_converged(old_centroids, centroids, iterations):
        old_centroids = centroids
        iterations += 1
        clusters = assign_clusters(data_set, centroids)
        centroids = calculate_new_centroids(clusters, data_set, k)
    return centroids, clusters, iterations
def has_converged(old_centroids, centroids, iterations):
    return iterations > MAX_ITERATIONS or old_centroids == centroids
def get_random_centroids(data_set, k):
    return [data_set[np.random.randint(0, len(data_set))].tolist() for _ in range(k)]
def assign_clusters(data_set, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for data_point in data_set:
        closest_centroid_index = np.argmin([euclidean_distance(data_point, centroid) for centroid in centroids])
        clusters[closest_centroid_index].append(data_point)
    return clusters
def calculate_new_centroids(clusters, data_set, k):
    new_centroids = []
    for cluster in clusters:
        if not cluster:
            new_centroids.append(get_random_centroids(data_set, 1)[0])
        else:
            new_centroids.append(np.mean(cluster, axis=0).tolist())
    return new_centroids
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
if __name__ == "__main__":
    data_set = np.array([
        [1.0, 2.0], [1.5, 1.8], [5.0, 8.0],
        [8.0, 8.0], [1.0, 0.6], [9.0, 11.0],
        [8.0, 2.0], [10.0, 2.0], [9.0, 3.0]
    ])
    k = 3
    centroids, clusters, iterations = kmeans_clustering(data_set, k)
    print("Centroids:")
    print(centroids)
    print("\nClusters:")
    for cluster in clusters:
        print(cluster)
    print("\nIterations:")
    print(iterations)