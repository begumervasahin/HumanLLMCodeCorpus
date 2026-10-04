import numpy as np
import k_means
class class1:
    def fonk1(self, X, n_clusters):
        b1 = X.shape[0]
        b2 = [np.arange(b1)]
        while len(b2) < n_clusters:
            b3 = [np.var(X[cluster]) for cluster in b2]
            b4 = np.argmax(b3)
            b5 = X[b2[b4]]
            b6 = k_means.KMeans()
            b7 = b6.fonk1(b5, n_clusters=2, max_iter=100)
            b8 = [b2[b4][b7 == i] for i in range(2)]
            b2.pop(b4)
            b2.extend(b8)
        b9 = np.zeros(b1, dtype=int)
        for cluster_idx, cluster in enumerate(b2):
            b9[cluster] = cluster_idx
        return b9