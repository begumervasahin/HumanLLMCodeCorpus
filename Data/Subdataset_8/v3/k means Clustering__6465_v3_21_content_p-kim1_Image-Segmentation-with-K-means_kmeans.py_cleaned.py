import numpy as np
class KMeans:
    def __init__(self, num_clusters, data):
        self.num_clusters = num_clusters
        self.num_data_points, self.dimensionality = np.shape(data)
        self.data = data
    def _initialize_centroids(self):
        min_values = np.min(self.data, axis=0)
        max_values = np.max(self.data, axis=0)
        return np.random.rand(self.num_clusters, self.dimensionality) * (max_values - min_values) + min_values
    def _assign_data_to_clusters(self, centroids):
        distances = np.sum((self.data[:, np.newaxis] - centroids) ** 2, axis=2)
        return np.argmin(distances, axis=1)
    def _update_centroids(self, cluster_assignments):
        centroids = np.zeros((self.num_clusters, self.dimensionality))
        for cluster_index in range(self.num_clusters):
            cluster_data_points = self.data[cluster_assignments == cluster_index]
            if len(cluster_data_points) > 0:
                centroids[cluster_index] = np.mean(cluster_data_points, axis=0)
        return centroids
    def train(self, max_iterations=10):
        centroids = self._initialize_centroids()
        prev_centroids = np.zeros_like(centroids)
        iteration_count = 0
        while not np.array_equal(centroids, prev_centroids) and iteration_count < max_iterations:
            prev_centroids = centroids.copy()
            cluster_assignments = self._assign_data_to_clusters(centroids)
            centroids = self._update_centroids(cluster_assignments)
            iteration_count += 1
        return centroids, cluster_assignments
    def predict(self, new_data, centroids):
        distances = np.sum((new_data[:, np.newaxis] - centroids) ** 2, axis=2)
        return np.argmin(distances, axis=1)
if __name__ == "__main__":
    np.random.seed(42)
    data = np.random.rand(100, 2)
    kmeans = KMeans(num_clusters=3, data=data)
    trained_centroids, cluster_assignments = kmeans.train()
    print("Final cluster centers:")
    print(trained_centroids)
    new_data = np.random.rand(10, 2)
    predicted_clusters = kmeans.predict(new_data, trained_centroids)
    print("Clusters for new data:")
    print(predicted_clusters)