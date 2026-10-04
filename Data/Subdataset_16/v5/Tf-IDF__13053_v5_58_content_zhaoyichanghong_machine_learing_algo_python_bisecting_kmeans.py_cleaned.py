import numpy as np
import k_means
class class1:
    def fonk1(self, X, n_clusters):
        b1 = X.shape[0]
        b2 = np.arange(b1)
        b3 = [b2]
        while len(b3) < n_clusters:
            b4 = [self.fonk2(X[cluster]) for cluster in b3]
            b5 = np.argmax(b4)
            b6 = X[b3[b5]]
            b7 = self.fonk3(b6)
            b8 = [b3[b5][b7 == i] for i in range(2)]
            b3.pop(b5)
            b3.extend(b8)
        b9 = self.fonk4(b3, b1)
        return b9
    def fonk2(self, cluster_data):
        return np.var(cluster_data) * cluster_data.shape[0]
    def fonk3(self, data):
        b10 = k_means.KMeans()
        b7 = b10.fonk1(data, n_clusters=2, max_iter=100)
        return b7
    def fonk4(self, b3, b1):
        b9 = np.zeros(b1, dtype=int)
        for cluster_idx, cluster in enumerate(b3):
            b9[cluster] = cluster_idx
        return b9