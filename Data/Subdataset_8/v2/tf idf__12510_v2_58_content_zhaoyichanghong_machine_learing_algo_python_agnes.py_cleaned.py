import numpy as np
from scipy.spatial import distance
class Agnes:
    def fit(self, X, n_clusters):
        '''
        Agglomerative Nesting (AGNES) clustering algorithm.
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input data.
        n_clusters : int
            The number of clusters to form.
        Returns
        -------
        labels : array-like of shape (n_samples,)
            Predicted cluster labels for each sample.
        '''
        n_samples = X.shape[0]
        clusters = [[i] for i in range(n_samples)]
        for j in reversed(range(n_clusters, n_samples)):
            cluster_centers = np.array([np.mean(X[cluster], axis=0).ravel() for cluster in clusters])
            distances = distance.squareform(distance.pdist(cluster_centers))
            np.fill_diagonal(distances, np.inf)
            nearest_cluster_indices = np.unravel_index(np.argmin(distances), distances.shape)
            clusters[nearest_cluster_indices[0]].extend(clusters[nearest_cluster_indices[1]])
            del clusters[nearest_cluster_indices[1]]
        labels = np.zeros(n_samples)
        for i, cluster in enumerate(clusters):
            labels[cluster] = i
        return labels
if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    agnes = Agnes()
    n_clusters = 2
    predicted_labels = agnes.fit(X, n_clusters)
    print("Predicted labels:", predicted_labels)