import numpy as np
class KMeans:
    def __init__(self, k, data):
        self.k = k
        self.centers = self._initialize_centers(data)
    def _initialize_centers(self, data):
        minima, maxima = data.min(axis=0), data.max(axis=0)
        return np.random.rand(self.k, data.shape[1]) * (maxima - minima) + minima
    def _calculate_distances(self, data):
        distances = np.sqrt(((data[:, np.newaxis, :] - self.centers[np.newaxis, :, :]) ** 2).sum(axis=2))
        return distances
    def _update_clusters(self, data):
        distances = self._calculate_distances(data)
        closest_clusters = np.argmin(distances, axis=1)
        for i in range(self.k):
            points_in_cluster = data[closest_clusters == i]
            if len(points_in_cluster) > 0:
                self.centers[i] = np.mean(points_in_cluster, axis=0)
    def train(self, data, max_iterations=10):
        for _ in range(max_iterations):
            old_centers = self.centers.copy()
            self._update_clusters(data)
            if np.allclose(old_centers, self.centers, atol=1e-4):
                break
    def predict(self, data):
        distances = self._calculate_distances(data)
        return np.argmin(distances, axis=1)
if __name__ == "__main__":
    data = np.random.rand(100, 2)
    kmeans = KMeans(k=3, data=data)
    kmeans.train(data)
    clusters = kmeans.predict(data)
    print("Cluster centers:", kmeans.centers)
    print("Cluster assignments:", clusters)