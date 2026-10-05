import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class KMeans:
    def __init__(self, k=2, max_iteration=500, seed=42):
        self.k = k
        self.max_iteration = max_iteration
        np.random.seed(seed)
        self.centroids = []
    def train(self, inputs, display=False):
        min_x, min_y = np.amin(inputs, axis=0) - 1
        max_x, max_y = np.amax(inputs, axis=0) + 1
        self.centroids = np.array([
            [np.random.uniform(min_x, max_x), np.random.uniform(min_y, max_y)]
            for _ in range(self.k)
        ])
        for _ in range(self.max_iteration):
            cluster_assignments = self._assign_clusters(inputs)
            new_centroids = self._calculate_new_centroids(inputs, cluster_assignments)
            if np.all(new_centroids == self.centroids):
                break
            self.centroids = new_centroids
        if display:
            self._display_plot(inputs, cluster_assignments)
    def _assign_clusters(self, inputs):
        distances = np.sqrt(((inputs - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
    def _calculate_new_centroids(self, inputs, cluster_assignments):
        return np.array([
            inputs[cluster_assignments == k].mean(axis=0)
            for k in range(self.k)
        ])
    def _display_plot(self, inputs, cluster_assignments):
        plt.figure(figsize=(8, 6))
        plt.scatter(inputs[:, 0], inputs[:, 1], c=cluster_assignments, cmap='viridis', alpha=0.5)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red', s=100, marker='X')
        plt.title('KMeans Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.show()
X, _ = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
clusterer = KMeans(k=3)
clusterer.train(X, display=True)