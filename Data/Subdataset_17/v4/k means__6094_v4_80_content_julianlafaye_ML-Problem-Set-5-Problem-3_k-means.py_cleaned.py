import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as metric
def initialize(dataset, k):
    n_features = np.shape(dataset)[1]
    centroids = np.mat(np.zeros((k, n_features)))
    for i in range(n_features):
        min_val = min(dataset[:, i])
        range_val = float(max(dataset[:, i]) - min_val)
        centroids[:, i] = min_val + range_val * np.random.rand(k, 1)
    return centroids
def cluster(dataset, k):
    n_samples = np.shape(dataset)[0]
    cluster_class = np.mat(np.zeros((n_samples, 2)))
    centroids = initialize(dataset, k)
    centroids_origin = centroids.copy()
    changed = True
    n_iter = 0
    while changed:
        changed = False
        for i in range(n_samples):
            min_dist = np.inf
            min_index = -1
            for j in range(k):
                distance = metric.euclidean(centroids[j, :], dataset[i, :])
                if distance < min_dist:
                    min_dist = distance
                    min_index = j
            if cluster_class[i, 0] != min_index:
                changed = True
            cluster_class[i, :] = min_index, min_dist ** 2
        for cent in range(k):
            points = dataset[np.nonzero(cluster_class[:, 0].A == cent)[0]]
            centroids[cent, :] = np.mean(points, axis=0)
        n_iter += 1
        print(f"Iteration {n_iter}")
    return centroids, cluster_class, n_iter, centroids_origin
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
    centroids, cluster_classes, n, origin_centroids = cluster(dataset, k)
    print('Number of iterations:', n)
    print('\nFinal centroids:\n', centroids)
    print('\nOriginal centroids:\n', origin_centroids)
    newSet = np.concatenate((dataset, cluster_classes), axis=1)
    plt.scatter(newSet[:, 0], newSet[:, 1], c=newSet[:, 2])
    plt.title('Clustered Data')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
if __name__ == "__main__":
    main()