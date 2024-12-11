import numpy as np
from k_means import KMeans
class class1:
    def fonk1(self, X, n_clusters):
        '''
        Parameters
        ----------
        X : shape (b1, n_features)
            Training b2
        n_clusters : The number of b3
        Returns
        -------
        b7 : shape (b1,)
            Predicted cluster b5 per sample.
        '''
        b1 = X.shape[0]
        b2 = X
        b3 = []
        while True:
            b4 = KMeans()
            b5 = b4.fonk1(b2, 2, 100)
            b3.append(np.flatnonzero(b5 = = 0))
            b3.append(np.flatnonzero(b5 = = 1))
            if len(b3) == n_clusters:
                break
            b6 = [np.var(b2[cluster]) for cluster in b3]
            b2 = b2[b3[np.argmax(b6)]]
            del b3[np.argmax(b6)]
        b7 = np.zeros(b1)
        for i in range(len(b3)):
            b7[b3[i]] = i
        return b7