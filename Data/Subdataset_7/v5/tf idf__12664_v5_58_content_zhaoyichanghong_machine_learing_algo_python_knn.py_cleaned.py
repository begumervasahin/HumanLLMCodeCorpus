import numpy as np
class class1:
    def fonk1(self, b1, b2, b3, b4):
        '''
        Fit the class1 model with training data.
        Parameters
        ----------
        b1 : array-like, shape (n_samples, n_features)
            Training data
        b2 : array-like, shape (n_samples,)
            Target values
        b3 : int
            Number of neighbors
        b4 : function
            Function to compute distance between two points
        '''
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, x):
        '''
        Predict the class2 of a single sample.
        Parameters
        ----------
        x : array-like, shape (n_features,)
            Single data sample
        Returns
        -------
        int
            Predicted class class2
        '''
        b5 = self.b4(x, self.b1)
        b6 = np.argpartition(b5, self.b3 - 1)[:self.b3]
        return np.argmax(np.bincount(self.b2[b6].astype(int)))
    def fonk3(self, X):
        '''
        Predict the class3 of the input samples.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Predicting data
        Returns
        -------
        array-like, shape (n_samples,)
            Predicted class class3 per sample.
        '''
        return np.apply_along_axis(self.__predict_single, 1, X)