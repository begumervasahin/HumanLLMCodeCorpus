import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize_centroids(dataset, k):
    num_features = dataset.shape[1]
    centroids = np.zeros((k, num_features))
    for i in range(num_features):
        min_val = np.min(dataset[:, i])
        range_val = np.max(dataset[:, i]) - min_val
        centroids[:, i] = min_val + range_val * np.random.rand(k)
    return centroids
def kmeans_clustering(dataset, k):
    num_samples = dataset.shape[0]
    cluster_assignments = np.zeros((num_samples, 2))
    centroids = initialize_centroids(dataset, k)
    initial_centroids = centroids.copy()
    changed = True
    iterations = 0
    while changed:
        changed = False
        for i in range(num_samples):
            distances = [metric.euclidean(dataset[i, :], centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            if cluster_assignments[i, 0] != closest_centroid:
                changed = True
            cluster_assignments[i, :] = closest_centroid, distances[closest_centroid] ** 2
        for cent in range(k):
            points_assigned_to_centroid = dataset[cluster_assignments[:, 0] == cent]
            if points_assigned_to_centroid.size > 0:
                centroids[cent, :] = np.mean(points_assigned_to_centroid, axis=0)
        iterations += 1
        print(f'Iteration {iterations}')
    return centroids, cluster_assignments, iterations, initial_centroids
def plot_dataset(dataset):
    plt.scatter(dataset[:, 0], dataset[:, 1])
    plt.title('Dataset')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def plot_clusters(dataset, centroids, cluster_assignments):
    plt.scatter(dataset[:, 0], dataset[:, 1], c=cluster_assignments[:, 0])
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')
    plt.title('Clustered Data with Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
def main():
    print('k-Means Clustering Algorithm in Python')
    filename = 'kmeans_data.csv'
    dataset = np.genfromtxt(filename, delimiter=',')
    plot_dataset(dataset)
    k = int(input("Number of Centroids: "))
    centroids, cluster_assignments, iterations, initial_centroids = kmeans_clustering(dataset, k)
    print('Number of iterations:', iterations)
    print('\nFinal centroids:\n', centroids)
    print('\nInitial centroids:\n', initial_centroids)
    plot_clusters(dataset, centroids, cluster_assignments)
if __name__ == "__main__":
    main()