import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize_centroids(dataset, k):
    num_features = np.shape(dataset)[1]
    centroids = np.zeros((k, num_features))
    for i in range(num_features):
        min_val = min(dataset[:, i])
        range_val = float(max(dataset[:, i]) - min_val)
        centroids[:, i] = min_val + range_val * np.random.rand(k)
    return centroids
def k_means(dataset, k):
    num_data_points = np.shape(dataset)[0]
    cluster_assignments = np.zeros((num_data_points, 2))
    centroids = initialize_centroids(dataset, k)
    original_centroids = centroids.copy()
    converged = False
    num_iterations = 0
    while not converged:
        converged = True
        for i in range(num_data_points):
            min_distance = np.inf
            min_index = -1
            for j in range(k):
                distance = metric.euclidean(centroids[j, :], dataset[i, :])
                if distance < min_distance:
                    min_distance = distance
                    min_index = j
            if cluster_assignments[i, 0] != min_index:
                converged = False
            cluster_assignments[i, :] = min_index, min_distance ** 2
        for cent in range(k):
            points_in_cluster = dataset[np.nonzero(cluster_assignments[:, 0] == cent)[0]]
            centroids[cent, :] = np.mean(points_in_cluster, axis=0)
        num_iterations += 1
    return centroids, cluster_assignments, num_iterations, original_centroids
print('k Means Clustering Algorithm in Python')
filename = 'kmeans_data.csv'
dataset = np.genfromtxt(filename, delimiter=',')
plt.scatter(dataset[:, 0], dataset[:, 1])
plt.title('Input Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
num_centroids = int(input("Number of Centroids: "))
final_centroids, cluster_assignments, num_iterations, original_centroids = k_means(dataset, num_centroids)
print('Number of iterations:', num_iterations)
print('\nFinal centroids:\n', final_centroids)
print('\nOriginal centroids:\n', original_centroids)
clustered_dataset = np.concatenate((dataset, cluster_assignments), axis=1)
plt.scatter(clustered_dataset[:, 0], clustered_dataset[:, 1], c=clustered_dataset[:, 2])
plt.title('Clustered Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()