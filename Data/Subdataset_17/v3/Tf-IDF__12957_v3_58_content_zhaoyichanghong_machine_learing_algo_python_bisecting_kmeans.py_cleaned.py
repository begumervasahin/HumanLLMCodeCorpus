import numpy as np
from sklearn.cluster import KMeans
class BisectingKMeans:
    def fit(self, X, n_clusters):
        n_samples = X.shape[0]
        clusters = [np.arange(n_samples)]
        while len(clusters) < n_clusters:
            sse = [self._calculate_sse(X, cluster) for cluster in clusters]
            index_to_split = np.argmax(sse)
            data_to_split = X[clusters[index_to_split]]
            new_clusters = self._split_cluster(data_to_split, clusters[index_to_split])
            clusters[index_to_split] = new_clusters[0]
            clusters.append(new_clusters[1])
        y = self._assign_labels(n_samples, clusters)
        return y
    def _calculate_sse(self, X, cluster):
        return np.var(X[cluster])
    def _split_cluster(self, data_to_split, indices_to_split):
        kmeans = KMeans(n_clusters=2, random_state=0)
        labels = kmeans.fit_predict(data_to_split)
        new_clusters = [indices_to_split[labels == i] for i in range(2)]
        return new_clusters
    def _assign_labels(self, n_samples, clusters):
        y = np.zeros(n_samples, dtype=int)
        for i, cluster in enumerate(clusters):
            y[cluster] = i
        return y
if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.rand(100, 2)
    bkm = BisectingKMeans()
    n_clusters = 3
    labels = bkm.fit(X, n_clusters)
    print("Cluster labels:", labels)