import numpy as np
class class1:
    def fonk1(self, X, y, n_neighbors, distance):
        '''
        Parameters
        ----------
        X : shape (n_samples, n_features)
            Training data
        y : shape (n_samples, n_classes)
            Target values
        n_neighbors : Number of neighbors
        distance : Distance algorithm, see also distance.py
        '''
        self.b1 = X
        self.b2 = y
        self.b3 = n_neighbors
        self.b4 = distance
    def fonk2(self, x):
        b5 = self.b4(x, self.b1)
        b6 = np.argpartition(b5, self.b3 - 1)[:self.b3]
        return np.argmax(np.bincount(self.b2[b6].astype(int)))
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