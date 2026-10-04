import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
from sys import argv
def main():
    input_file = argv[1]
    k = int(argv[2])
    output_file = argv[3]
    data = read_csv(input_file)
    X, y = data[:, :-1], data[:, -1]
    X = normalize(X)
    clusters, centroids = k_means(X, k)
    sse = calculate_sse(X, clusters, centroids)
    print(f"SSE is {sse:.2f}")
    write_output(output_file, clusters, sse)
def read_csv(file_path):
    with open(file_path) as file:
        return np.array([row for row in reader(file) if row])
def normalize(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
def initialize_centroids(X, k):
    indices = set()
    centroids = []
    while len(centroids) < k:
        index = randint(0, len(X) - 1)
        if index not in indices:
            centroids.append(X[index])
            indices.add(index)
    return np.array(centroids)
def assign_clusters(X, centroids):
    clusters = np.zeros(len(X))
    for i, point in enumerate(X):
        distances = np.linalg.norm(point - centroids, axis=1)
        clusters[i] = np.argmin(distances)
    return clusters
def update_centroids(X, clusters, k):
    new_centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        points = X[clusters == i]
        if len(points) > 0:
            new_centroids[i] = points.mean(axis=0)
    return new_centroids
def k_means(X, k):
    centroids = initialize_centroids(X, k)
    old_centroids = np.zeros_like(centroids)
    clusters = np.zeros(len(X))
    while np.linalg.norm(centroids - old_centroids, axis=1).sum() != 0:
        clusters = assign_clusters(X, centroids)
        old_centroids = deepcopy(centroids)
        centroids = update_centroids(X, clusters, k)
    return clusters, centroids
def calculate_sse(X, clusters, centroids):
    sse = 0.0
    for i, centroid in enumerate(centroids):
        points = X[clusters == i]
        sse += np.sum((points - centroid) ** 2)
    return sse
def write_output(file_path, clusters, sse):
    with open(file_path, 'w') as file:
        for cluster in clusters:
            file.write(f"{int(cluster)}\n")
        file.write(f"SSE is {sse:.2f}")
if __name__ == '__main__':
    main()