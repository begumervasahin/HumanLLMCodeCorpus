import numpy as np
class KMeans:
    def fit(self, X, n_clusters, max_iter):
        pass
class BisectingKMeans:
    def fit(self, X, n_clusters):
        '''
        Fit Bisecting K-Means clustering algorithm.
        Parameters
        ----------
        X : numpy.ndarray
            Training data of shape (n_samples, n_features).
        n_clusters : int
            The desired number of clusters.
        Returns
        -------
        y : numpy.ndarray
            Predicted cluster label per sample of shape (n_samples,).
        '''
        n_samples = X.shape[0]
        data = X
        clusters = []
        while True:
            model = KMeans()
            label = model.fit(data, 2, 100)
            clusters.append(np.flatnonzero(label == 0))
            clusters.append(np.flatnonzero(label == 1))
            if len(clusters) == n_clusters:
                break
            sse = [np.var(data[cluster]) for cluster in clusters]
            data = data[clusters[np.argmax(sse)]]
            del clusters[np.argmax(sse)]
        y = np.zeros(n_samples)
        for i in range(len(clusters)):
            y[clusters[i]] = i
        return y
if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    bisecting_kmeans = BisectingKMeans()
    labels = bisecting_kmeans.fit(X, 3)
    print("Cluster labels:", labels)