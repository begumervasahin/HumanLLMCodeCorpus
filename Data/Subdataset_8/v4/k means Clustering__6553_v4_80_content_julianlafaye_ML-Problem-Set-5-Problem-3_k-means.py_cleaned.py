import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize_centroids(dataset, k):
    n = np.shape(dataset)[1]
    centroids = np.zeros((k, n))
    for i in range(n):
        min_val = min(dataset[:, i])
        range_val = float(max(dataset[:, i]) - min_val)
        centroids[:, i] = min_val + range_val * np.random.rand(k)
    return centroids
def kmeans(dataset, k):
    m = np.shape(dataset)[0]
    cluster_assignments = np.zeros((m, 2))
    centroids = initialize_centroids(dataset, k)
    original_centroids = centroids.copy()
    changed = True
    num_iterations = 0
    while changed:
        changed = False
        for i in range(m):
            min_dist = np.inf
            min_index = -1
            for j in range(k):
                distance = metric.euclidean(centroids[j, :], dataset[i, :])
                if distance < min_dist:
                    min_dist = distance
                    min_index = j
            if cluster_assignments[i, 0] != min_index:
                changed = True
            cluster_assignments[i, :] = min_index, min_dist ** 2
        for cent in range(k):
            points = dataset[np.nonzero(cluster_assignments[:, 0] == cent)[0]]
            centroids[cent, :] = np.mean(points, axis=0)
        num_iterations += 1
    return centroids, cluster_assignments, num_iterations, original_centroids
print('k Means Clustering Algorithm in Python')
filename = 'kmeans_data.csv'
dataset = np.genfromtxt(filename, delimiter=',')
plt.scatter(dataset[:, 0], dataset[:, 1])
plt.show()
num_centroids = int(input("Number of Centroids: "))
k = num_centroids
centroids, cluster_assignments, num_iterations, original_centroids = kmeans(dataset, k)
print('Number of iterations:', num_iterations)
print('\nFinal centroids:\n', centroids)
print('\nOriginal centroids:\n', original_centroids)
clustered_data = np.concatenate((dataset, cluster_assignments), axis=1)
plt.scatter(clustered_data[:, 0], clustered_data[:, 1], c=clustered_data[:, 2])
plt.show()