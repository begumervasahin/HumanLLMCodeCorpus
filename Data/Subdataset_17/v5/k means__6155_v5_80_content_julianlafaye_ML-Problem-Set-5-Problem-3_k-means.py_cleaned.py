import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize_centroids(dataset, k):
    n_features = dataset.shape[1]
    centroids = np.zeros((k, n_features))
    for i in range(n_features):
        feature_min = np.min(dataset[:, i])
        feature_range = np.ptp(dataset[:, i])
        centroids[:, i] = feature_min + feature_range * np.random.rand(k)
    return np.matrix(centroids)
def assign_clusters(dataset, centroids):
    n_samples = dataset.shape[0]
    cluster_info = np.zeros((n_samples, 2))
    for i in range(n_samples):
        min_dist = np.inf
        for j in range(centroids.shape[0]):
            dist = metric.euclidean(centroids[j, :], dataset[i, :])
            if dist < min_dist:
                min_dist = dist
                cluster_info[i, :] = j, min_dist ** 2
    return np.matrix(cluster_info)
def update_centroids(dataset, cluster_info, k):
    centroids = np.zeros((k, dataset.shape[1]))
    for cent in range(k):
        points = dataset[np.where(cluster_info[:, 0].A == cent)[0]]
        centroids[cent, :] = np.mean(points, axis=0) if points.size else centroids[cent, :]
    return np.matrix(centroids)
def kmeans_clustering(dataset, k):
    centroids = initialize_centroids(dataset, k)
    initial_centroids = centroids.copy()
    cluster_info = np.matrix(np.zeros((dataset.shape[0], 2)))
    changed = True
    iterations = 0
    while changed:
        iterations += 1
        cluster_info = assign_clusters(dataset, centroids)
        new_centroids = update_centroids(dataset, cluster_info, k)
        if np.allclose(centroids, new_centroids):
            changed = False
        centroids = new_centroids
        print(f"Iteration {iterations}")
    return centroids, cluster_info, iterations, initial_centroids
def plot_data(dataset, title, xlabel, ylabel):
    plt.scatter(dataset[:, 0], dataset[:, 1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
def main():
    print('k-Means Clustering Algorithm in Python')
    filename = 'kmeans_data.csv'
    dataset = np.genfromtxt(filename, delimiter=',')
    plot_data(dataset, 'Dataset', 'Feature 1', 'Feature 2')
    k = int(input("Number of Centroids: "))
    centroids, cluster_info, iterations, initial_centroids = kmeans_clustering(dataset, k)
    print('Number of iterations:', iterations)
    print('\nFinal centroids:\n', centroids)
    print('\nInitial centroids:\n', initial_centroids)
    clustered_dataset = np.hstack((dataset, cluster_info))
    plt.scatter(clustered_dataset[:, 0], clustered_dataset[:, 1], c=clustered_dataset[:, 2])
    plt.title('Clustered Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
if __name__ == "__main__":
    main()