import csv
import random
import copy
import numpy as np
import sys
def main():
    if len(sys.argv) != 4:
        print("Usage: python kmeans.py <input_file> <k_clusters> <output_file>")
        sys.exit(1)
    inputFile = sys.argv[1]
    k = int(sys.argv[2])
    outputFile = sys.argv[3]
    with open(inputFile, 'r') as file:
        csv_reader = csv.reader(file)
        data = np.array([row for row in csv_reader if row])
    X, y = data[:, :-1].astype(float), data[:, -1]
    X = min_max_norm(X)
    clusters, centroids = k_means(X, k)
    sse = calculate_sse(X, k, centroids, clusters)
    print(f"SSE is {sse:.2f}")
    clusters = list(map(int, clusters))
    with open(outputFile, 'w') as file:
        for cluster_id in clusters:
            file.write(str(cluster_id) + '\n')
        file.write(f"SSE is {sse:.2f}")
def min_max_norm(X):
    normalized_data = []
    for column in X.T:
        col_min = column.min()
        col_max = column.max()
        normalized_column = (column - col_min) / (col_max - col_min)
        normalized_data.append(normalized_column)
    return np.array(normalized_data).T
def calculate_difference(centroids, old_centroids):
    total_difference = 0
    for i in range(len(centroids)):
        total_difference += np.linalg.norm(centroids[i] - old_centroids[i], 2)
    return total_difference
def k_means(X, k):
    centroids = []
    index_set = set()
    for _ in range(k):
        index = random.randint(0, len(X) - 1)
        while index in index_set:
            index = random.randint(0, len(X) - 1)
        centroids.append(X[index])
        index_set.add(index)
    centroids = np.array(centroids)
    old_centroids = np.zeros(centroids.shape)
    difference = calculate_difference(centroids, old_centroids)
    cluster_assignments = np.zeros(len(X))
    while difference != 0:
        for i in range(len(X)):
            distances = []
            for centroid in centroids:
                distances.append(np.linalg.norm(X[i] - centroid, 2))
            cluster_index = np.argmin(distances)
            cluster_assignments[i] = cluster_index
        old_centroids = copy.deepcopy(centroids)
        for i in range(k):
            if len(X[cluster_assignments == i]) > 0:
                centroids[i] = np.mean(X[cluster_assignments == i], axis=0)
        difference = calculate_difference(centroids, old_centroids)
    return cluster_assignments, centroids
def calculate_sse(X, k, centroids, clusters):
    sse = 0
    for i in range(k):
        for j in X[clusters == i]:
            sse += np.linalg.norm(j - centroids[i], 2) ** 2
    return sse
if __name__ == '__main__':
    main()