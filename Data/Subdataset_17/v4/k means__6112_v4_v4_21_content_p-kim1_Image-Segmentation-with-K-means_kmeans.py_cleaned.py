import numpy as np
class KMeans:
    def __init__(self, k, data):
        self.k = k
        self.n_data = data.shape[0]
        self.n_dim = data.shape[1]
        self.centres = None
    def train(self, data, max_iterations=10):
        minima = data.min(axis=0)
        maxima = data.max(axis=0)
        self.centres = np.random.rand(self.k, self.n_dim) * (maxima - minima) + minima
        old_centres = np.zeros((self.k, self.n_dim))
        count = 0
        while not np.allclose(self.centres, old_centres) and count < max_iterations:
            old_centres = self.centres.copy()
            count += 1
            distances = np.linalg.norm(data[:, np.newaxis] - self.centres, axis=2)
            cluster_labels = np.argmin(distances, axis=1)
            for i in range(self.k):
                points_in_cluster = data[cluster_labels == i]
                if points_in_cluster.size > 0:
                    self.centres[i] = points_in_cluster.mean(axis=0)
        return self.centres
    def predict(self, data):
        distances = np.linalg.norm(data[:, np.newaxis] - self.centres, axis=2)
        cluster_labels = np.argmin(distances, axis=1)
        return cluster_labels