import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize_centroids(dataset, k):
    num_features = dataset.shape[1]
    centroids = np.zeros((k, num_features))
    for i in range(num_features):
        min_val = dataset[:, i].min()
        range_val = float(dataset[:, i].max() - min_val)
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
            min_distance = float('inf')
            closest_centroid = -1
            for j in range(k):
                distance = metric.euclidean(centroids[j, :], dataset[i, :])
                if distance < min_distance:
                    min_distance = distance
                    closest_centroid = j
            if cluster_assignments[i, 0] != closest_centroid:
                changed = True
            cluster_assignments[i, :] = closest_centroid, min_distance ** 2
        for cent in range(k):
            points_assigned_to_centroid = dataset[np.where(cluster_assignments[:, 0] == cent)[0]]
            if len(points_assigned_to_centroid) > 0:
                centroids[cent, :] = np.mean(points_assigned_to_centroid, axis=0)
        iterations += 1
        print(f'Iteration {iterations}')
    return centroids, cluster_assignments, iterations, initial_centroids
def main():
    print('k-Means Clustering Algorithm in Python')
    filename = 'kmeans_data.csv'
    dataset = np.genfromtxt(filename, delimiter=',')
    plt.scatter(dataset[:, 0], dataset[:, 1])
    plt.title('Dataset')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
    k = int(input("Number of Centroids: "))
    centroids, cluster_assignments, iterations, initial_centroids = kmeans_clustering(dataset, k)
    print('Number of iterations:', iterations)
    print('\nFinal centroids:\n', centroids)
    print('\nInitial centroids:\n', initial_centroids)
    plt.scatter(dataset[:, 0], dataset[:, 1], c=cluster_assignments[:, 0])
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')
    plt.title('Clustered Data with Centroids')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
if __name__ == "__main__":
    main()