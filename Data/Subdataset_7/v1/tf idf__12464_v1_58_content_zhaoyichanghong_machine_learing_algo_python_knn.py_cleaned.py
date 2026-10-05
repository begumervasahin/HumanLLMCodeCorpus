import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
class class1:
    def fonk1(self, X, y, b13, b1 = euclidean_distances):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Training data
        y : shape (n_samples,)
            Target values
        b13 : Number of neighbors
        b1 : Distance algorithm, default is Euclidean b1
        '''
        self.b2 = X
        self.b3 = y
        self.b4 = b13
        self.b5 = b1
    def fonk2(self, x):
        b6 = self.b5(x.reshape(1, -1), self.b2)
        b7 = np.argpartition(b6, self.b4 - 1)[:self.b4]
        return np.argmax(np.bincount(self.b3[b7].astype(int)))
    def fonk3(self, X):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Predicting data
        Returns
        -------
        y : shape (n_samples,)
            Predicted class class2 per sample.
        '''
        return np.apply_along_axis(self.__predict, 1, X)
if b8 = = "__main__":
    b9 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b10 = np.array([0, 0, 1, 1])
    b11 = np.array([[1.5, 2.5], [3.5, 4.5]])
    b12 = class1()
    b12.fonk1(b9, b10, b13 = 2)
    b14 = b12.fonk3(b11)
    print("Predictions:", b14)