import numpy as np
class KMeans:
    def __init__(self, k, data):
        self.nData = np.shape(data)[0]
        self.nDim = np.shape(data)[1]
        self.k = k
    def kmeans_train(self, data, maxIterations=10):
        minima = data.min(axis=0)
        maxima = data.max(axis=0)
        self.centres = np.random.rand(self.k, self.nDim) * (maxima - minima) + minima
        oldCentres = np.random.rand(self.k, self.nDim) * (maxima - minima) + minima
        count = 0
        while np.sum(np.sum(oldCentres - self.centres)) != 0 and count < maxIterations:
            oldCentres = self.centres.copy()
            count += 1
            distances = np.ones((self.k, self.nData)) * np.sum((data - self.centres[0, :]) ** 2, axis=1)
            for j in range(1, self.k):
                distances[j, :] = np.sum((data - self.centres[j, :]) ** 2, axis=1)
            cluster = np.argmin(distances, axis=0)
            for j in range(self.k):
                thisCluster = (cluster == j)
                if np.sum(thisCluster) > 0:
                    self.centres[j, :] = np.sum(data[thisCluster, :], axis=0) / np.sum(thisCluster)
        return self.centres
    def kmeans_fwd(self, data):
        nData = np.shape(data)[0]
        distances = np.ones((self.k, nData)) * np.sum((data - self.centres[0, :]) ** 2, axis=1)
        for j in range(1, self.k):
            distances[j, :] = np.sum((data - self.centres[j, :]) ** 2, axis=1)
        cluster = np.argmin(distances, axis=0)
        return cluster
if __name__ == "__main__":
    np.random.seed(42)
    data = np.random.rand(100, 2)
    kmeans = KMeans(k=3, data=data)
    centers = kmeans.kmeans_train(data)
    print("Final centers:")
    print(centers)
    new_data = np.random.rand(10, 2)
    clusters = kmeans.kmeans_fwd(new_data)
    print("Clusters for new data:")
    print(clusters)