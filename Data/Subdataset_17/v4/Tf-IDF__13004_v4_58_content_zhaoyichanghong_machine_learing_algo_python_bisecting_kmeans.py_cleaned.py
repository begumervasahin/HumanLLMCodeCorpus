import numpy as np
import k_means
class BisectingKMeans:
    def fit(self, X, n_clusters):
        n_samples = X.shape[0]
        clusters = [np.arange(n_samples)]
        while len(clusters) < n_clusters:
            sse = [np.var(X[cluster]) for cluster in clusters]
            idx_to_split = np.argmax(sse)
            data_to_split = X[clusters[idx_to_split]]
            model = k_means.KMeans()
            labels = model.fit(data_to_split, n_clusters=2, max_iter=100)
            new_clusters = [clusters[idx_to_split][labels == i] for i in range(2)]
            clusters.pop(idx_to_split)
            clusters.extend(new_clusters)
        y = np.zeros(n_samples, dtype=int)
        for cluster_idx, cluster in enumerate(clusters):
            y[cluster] = cluster_idx
        return y