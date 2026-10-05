import numpy as np
from scipy.spatial import distance
class FuzzyCMeans:
    def fit(self, data, n_clusters, fuzziness, max_iter):
        '''
        Fit the Fuzzy C-Means clustering model to the data.
        Parameters
        ----------
        data : numpy.ndarray
            Input data of shape (n_samples, n_features).
        n_clusters : int
            The number of clusters to form.
        fuzziness : float
            The fuzziness parameter (m) controlling the degree of fuzziness.
        max_iter : int
            Maximum number of iterations for the algorithm.
        Returns
        -------
        cluster_labels : numpy.ndarray
            Predicted cluster labels for each sample.
        '''
        n_samples, n_features = data.shape
        membership_weights = np.zeros((n_samples, n_clusters))
        cluster_centers = data[np.random.choice(n_samples, n_clusters)]
        for _ in range(max_iter):
            distances = distance.cdist(cluster_centers, data, metric='euclidean').T + 1e-8
            for i in range(n_clusters):
                membership_weights[:, i] = 1 / np.sum((distances[:, i].reshape((-1, 1)) / distances) ** (2 / (fuzziness - 1)), axis=1)
            for i in range(n_clusters):
                cluster_centers[i] = np.sum((membership_weights[:, i].reshape(-1, 1) ** fuzziness) * data, axis=0) / np.sum(membership_weights[:, i] ** fuzziness)
        cluster_labels = np.argmax(membership_weights, axis=1)
        return cluster_labels
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(100, 2)
    fcm = FuzzyCMeans()
    cluster_labels = fcm.fit(data, n_clusters=3, fuzziness=2, max_iter=10)
    print(cluster_labels)