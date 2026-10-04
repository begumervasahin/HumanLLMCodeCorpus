import numpy as np
class KMeans:
    def __init__(self, k, data):
        self.k = k
        self.data = data
        self.n_data, self.n_dim = data.shape
    def initialize_centers(self):
        minima = self.data.min(axis=0)
        maxima = self.data.max(axis=0)
        self.centres = np.random.rand(self.k, self.n_dim) * (maxima - minima) + minima
    def compute_distances(self, data, centers):
        return np.linalg.norm(data[:, np.newaxis] - centers, axis=2)
    def update_centers(self, cluster_assignments):
        for i in range(self.k):
            assigned_data = self.data[cluster_assignments == i]
            if assigned_data.size > 0:
                self.centres[i] = assigned_data.mean(axis=0)
    def train(self, max_iterations=100):
        self.initialize_centers()
        old_centres = np.zeros_like(self.centres)
        count = 0
        while np.any(np.abs(old_centres - self.centres) > 1e-5) and count < max_iterations:
            old_centres = self.centres.copy()
            count += 1
            distances = self.compute_distances(self.data, self.centres)
            cluster_assignments = np.argmin(distances, axis=1)
            self.update_centers(cluster_assignments)
        return self.centres
    def predict(self, new_data):
        distances = self.compute_distances(new_data, self.centres)
        cluster_assignments = np.argmin(distances, axis=1)
        return cluster_assignments
if __name__ == "__main__":
    data = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    k = 2
    kmeans = KMeans(k, data)
    centres = kmeans.train(max_iterations=100)
    print("Cluster centers:\n", centres)
    new_data = np.array([[0, 0], [4, 4], [10, 10]])
    clusters = kmeans.predict(new_data)
    print("Predicted clusters for new data:\n", clusters)