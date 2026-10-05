import numpy as np
from scipy.spatial import distance
class class1:
    def fonk1(self, b8, a1):
        '''
        Parameters
        ----------
        b8 : shape (b1, n_features)
            Training data
        a1 : The number of b2
        Returns
        -------
        b6 : shape (b1,)
            Predicted cluster label per sample.
        '''
        b1 = b8.shape[0]
        b2 = [[i] for i in range(b1)]
        for j in reversed(range(a1, b1)):
            b3 = np.array([np.mean(b8[cluster], axis=0).ravel() for cluster in b2])
            b4 = distance.squareform(distance.pdist(b3))
            np.fill_diagonal(b4, np.inf)
            b5 = np.unravel_index(np.argmin(b4), b4.shape)
            b2[b5[0]].extend(b2[b5[1]])
            del b2[b5[1]]
        b6 = np.zeros(b1)
        for i in range(len(b2)):
            b6[b2[i]] = i
        return b6
if b7 = = "__main__":
    b8 = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    b9 = class1()
    a1 = 2
    b10 = b9.fonk1(b8, a1)
    print("Predicted labels:", b10)