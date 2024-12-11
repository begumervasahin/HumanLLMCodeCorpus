import numpy as np
import distance
class class1:
    def fonk1(self, X, n_clusters, m, epochs):
        '''
        Parameters
        ----------
        X : shape (n_samples, b1)
            Training data
        n_clusters : The number of clusters
        m : weighted index number
        epochs : The number of epochs
        Returns
        -------
        y : shape (n_samples,)
            Predicted cluster label per sample.
        '''
        n_samples, b1 = X.shape
        b2 = np.zeros((n_samples, n_clusters))
        b3 = X[np.random.choice(n_samples, n_clusters)]
        for _ in range(epochs):
            b4 = np.apply_along_axis(distance.euclidean_distance, 1, b3, X).T + 1e-8
            for i in range(n_clusters):
                b2[:, i] = 1 / np.sum((b4[:, i].reshape((-1, 1)) / b4) ** (2 / (m - 1)), b5 = 1)
            for i in range(n_clusters):
                b3[i] = np.sum(b2[:, i].reshape(-1, 1) ** m * X, b5 = 0) / np.sum(b2[:, i] ** m)
        return np.argmax(b2, b5 = 1)