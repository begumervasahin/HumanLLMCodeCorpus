import numpy as np
from sklearn.cluster import KMeans
class class1:
    def fonk1(self, b12, a1):
        '''
        Parameters
        ----------
        b12 : ndarray of shape (b1, n_features)
            Training b2.
        a1 : int
            The number of b3 to form.
        Returns
        -------
        b10 : ndarray of shape (b1,)
            Predicted cluster b8 per sample.
        '''
        b1 = b12.shape[0]
        b2 = b12
        b3 = [np.arange(b1)]
        while len(b3) < a1:
            b4 = [np.var(b2[cluster]) for cluster in b3]
            b5 = np.argmax(b4)
            b6 = b2[b3[b5]]
            b7 = KMeans(a1=2, random_state=0)
            b8 = b7.fit_predict(b6)
            b9 = [b3[b5][b8 == i] for i in range(2)]
            b3[b5] = b9[0]
            b3.append(b9[1])
        b10 = np.zeros(b1, dtype=int)
        for i, cluster in enumerate(b3):
            b10[cluster] = i
        return b10
if b11 = = "__main__":
    np.random.seed(42)
    b12 = np.random.rand(100, 2)
    b13 = class1()
    a1 = 3
    b14 = b13.fonk1(b12, a1)
    print("Cluster b14:", b14)