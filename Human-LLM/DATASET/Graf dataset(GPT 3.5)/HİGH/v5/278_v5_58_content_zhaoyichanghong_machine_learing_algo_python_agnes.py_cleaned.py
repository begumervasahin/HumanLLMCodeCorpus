import numpy as np
import distance
class class1:
    def fonk1(self, X, n_clusters):
        '''
        Parameters
        ----------
        X : numpy.ndarray
            Training data with shape (b1, n_features)
        n_clusters : int
            The number of b2
        Returns
        -------
        b6 : numpy.ndarray
            Predicted cluster label per sample with shape (b1,)
        '''
        b1 = X.shape[0]
        b2 = [[i] for i in range(b1)]
        for j in reversed(range(n_clusters, b1)):
            b3 = np.array([np.mean(X[cluster], axis=0).ravel() for cluster in b2])
            b4 = np.apply_along_axis(distance.euclidean_distance, 1, b3, b3)
            b5 = np.unravel_index(np.argmin(b4 + np.diag(np.full(j + 1, np.inf))), b4.shape)
            b2[b5[0]].extend(b2[b5[1]])
            del b2[b5[1]]
        b6 = np.zeros(b1)
        for i, cluster in enumerate(b2):
            b6[cluster] = i
        return b6