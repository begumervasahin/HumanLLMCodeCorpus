import numpy as np
class KMeans:
    def __init__(self, k, data):
        self.nData = np.shape(data)[0]
        self.nDim = np.shape(data)[1]
        self.k = k
    def kmeans_train(self, data, max_iterations=10):
        minima = data.min(axis=0)
        maxima = data.max(axis=0)
        self.centres = np.random.rand(self.k, self.nDim) * (maxima - minima) + minima
        old_centres = np.random.rand(self.k, self.nDim) * (maxima - minima) + minima
        iteration_count = 0
        while np.sum(np.sum(old_centres - self.centres)) != 0 and iteration_count < max_iterations:
            old_centres = self.centres.copy()
            iteration_count += 1
            distances = np.ones((self.k, self.nData)) * np.sum((data - self.centres[0, :]) ** 2, axis=1)
            for j in range(1, self.k):
                distances[j, :] = np.sum((data - self.centres[j, :]) ** 2, axis=1)
            cluster = np.argmin(distances, axis=0)
            for j in range(self.k):
                this_cluster = (cluster == j)
                if np.sum(this_cluster) > 0:
                    self.centres[j, :] = np.sum(data[this_cluster, :], axis=0) / np.sum(this_cluster)
        return self.centres
    def kmeans_fwd(self, data):
        n_data = np.shape(data)[0]
        distances = np.ones((self.k, n_data)) * np.sum((data - self.centres[0, :]) ** 2, axis=1)
        for j in range(1, self.k):
            distances[j, :] = np.sum((data - self.centres[j, :]) ** 2, axis=1)
        cluster = np.argmin(distances, axis=0)
        return cluster
if __name__ == "__main__":
    np.random.seed(42)
    data = np.random.rand(100, 2)
    kmeans = KMeans(k=3, data=data)
    centers = kmeans.kmeans_train(data)
    print("Final cluster centers:")
    print(centers)
    new_data = np.random.rand(10, 2)
    clusters = kmeans.kmeans_fwd(new_data)
    print("Clusters for new data:")
    print(clusters)