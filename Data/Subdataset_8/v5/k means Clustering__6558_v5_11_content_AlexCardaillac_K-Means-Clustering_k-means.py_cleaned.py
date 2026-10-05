import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class KMeans:
    def __init__(self, num_clusters=2):
        self.num_clusters = num_clusters
        self.centroids = []
    def train(self, data, max_iterations=500, seed=42, display=False):
        min_x, min_y = np.min(data, axis=0) - 1
        max_x, max_y = np.max(data, axis=0) + 1
        self.centroids = np.array([[np.random.randint(min_x, max_x), np.random.randint(min_y, max_y)] for _ in range(self.num_clusters)])
        prev_centroids = np.array([])
        closest_clusters = None
        for _ in range(max_iterations):
            prev_centroids = np.copy(self.centroids)
            closest_clusters = self.assign_closest_clusters(data)
            self.update_centroids(data, closest_clusters)
            if np.array_equal(self.centroids, prev_centroids):
                break
        closest_clusters = self.assign_closest_clusters(data)
        if display:
            self.display_clusters(data, closest_clusters, (min_x, max_x), (min_y, max_y))
    def assign_closest_clusters(self, data):
        distances = np.array([np.sqrt(np.sum((data - centroid) ** 2, axis=1)) for centroid in self.centroids])
        return np.argmin(distances, axis=0)
    def update_centroids(self, data, cluster_assignments):
        for i in range(self.num_clusters):
            cluster_points = data[cluster_assignments == i]
            if len(cluster_points) > 0:
                self.centroids[i] = np.mean(cluster_points, axis=0)
    def display_clusters(self, data, cluster_assignments, x_lim, y_lim):
        plt.figure()
        plt.scatter(data[:, 0], data[:, 1], c=cluster_assignments, cmap=plt.cm.Paired, alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c=range(self.num_clusters), cmap=plt.cm.Paired, edgecolor='k')
        plt.xlim(x_lim[0], x_lim[1])
        plt.ylim(y_lim[0], y_lim[1])
        plt.show()
data, _ = make_blobs(n_samples=100, centers=3, n_features=2)
clusterer = KMeans(num_clusters=3)
clusterer.train(data, display=True)