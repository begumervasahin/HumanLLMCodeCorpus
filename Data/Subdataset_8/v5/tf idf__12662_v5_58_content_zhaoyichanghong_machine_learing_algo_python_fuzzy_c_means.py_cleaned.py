import numpy as np
import distance
class FCM:
    def fit(self, X, n_clusters, m, epochs):
        '''
        Parameters
        ----------
        X : numpy.ndarray
            Training data of shape (n_samples, n_features)
        n_clusters : int
            The number of clusters
        m : float
            Weighted index number
        epochs : int
            The number of epochs
        Returns
        -------
        y : numpy.ndarray
            Predicted cluster label per sample of shape (n_samples,)
        '''
        n_samples, n_features = X.shape
        membership_weights = np.zeros((n_samples, n_clusters))
        cluster_centers = X[np.random.choice(n_samples, n_clusters)]
        for _ in range(epochs):
            distances = np.apply_along_axis(distance.euclidean_distance, 1, cluster_centers, X).T + 1e-8
            for i in range(n_clusters):
                membership_weights[:, i] = 1 / np.sum((distances[:, i].reshape((-1, 1)) / distances) ** (2 / (m - 1)), axis=1)
            for i in range(n_clusters):
                cluster_centers[i] = np.sum(membership_weights[:, i].reshape(-1, 1) ** m * X, axis=0) / np.sum(membership_weights[:, i] ** m)
        return np.argmax(membership_weights, axis=1)