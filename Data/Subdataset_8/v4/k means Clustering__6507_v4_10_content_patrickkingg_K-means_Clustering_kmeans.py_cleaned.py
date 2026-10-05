import numpy as np
from csv import reader
from random import randint
from copy import deepcopy
import sys
def read_data(input_file):
    with open(input_file, 'r') as file:
        csv_reader = reader(file)
        data = np.array([row for row in csv_reader if row], dtype=float)
    return data
def min_max_normalize(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
def initialize_centroids(X, k):
    indices = np.random.choice(len(X), size=k, replace=False)
    return X[indices]
def assign_clusters(X, centroids):
    distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
    return np.argmin(distances, axis=0)
def update_centroids(X, assignments, k):
    centroids = np.array([X[assignments == i].mean(axis=0) for i in range(k)])
    return centroids
def calculate_sse(X, assignments, centroids):
    sse = sum(np.linalg.norm(X[assignments == i] - centroids[i], axis=1)**2 for i in range(len(centroids)))
    return sse
def k_means(X, k):
    centroids = initialize_centroids(X, k)
    for iteration in range(100):
        assignments = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, assignments, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return assignments, centroids
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <inputfile.csv> <k> <outputfile.txt>")
        sys.exit(1)
    input_file, k, output_file = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    data = read_data(input_file)
    X = min_max_normalize(data[:, :-1])
    assignments, centroids = k_means(X, k)
    sse = calculate_sse(X, assignments, centroids)
    print(f"SSE is {sse:.2f}")
    with open(output_file, 'w') as f:
        for cluster_id in assignments:
            f.write(f"{cluster_id}\n")
        f.write(f"SSE is {sse:.2f}")
if __name__ == "__main__":
    main()