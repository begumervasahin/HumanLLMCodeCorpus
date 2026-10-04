import numpy as np
import k_means
class BisectingKMeans:
    def fit(self, X, n_clusters):
        n_samples = X.shape[0]
        initial_cluster = np.arange(n_samples)
        clusters = [initial_cluster]
        while len(clusters) < n_clusters:
            sse = [self._calculate_sse(X[cluster]) for cluster in clusters]
            idx_to_split = np.argmax(sse)
            data_to_split = X[clusters[idx_to_split]]
            labels = self._bisect_cluster(data_to_split)
            new_clusters = [clusters[idx_to_split][labels == i] for i in range(2)]
            clusters.pop(idx_to_split)
            clusters.extend(new_clusters)
        y = self._assign_labels(clusters, n_samples)
        return y
    def _calculate_sse(self, cluster_data):
        return np.var(cluster_data) * cluster_data.shape[0]
    def _bisect_cluster(self, data):
        model = k_means.KMeans()
        labels = model.fit(data, n_clusters=2, max_iter=100)
        return labels
    def _assign_labels(self, clusters, n_samples):
        y = np.zeros(n_samples, dtype=int)
        for cluster_idx, cluster in enumerate(clusters):
            y[cluster] = cluster_idx
        return y