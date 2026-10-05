import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
class class1:
    def fonk1(self, b1 = 5, b2=euclidean_distances):
        '''
        Initialize the K Nearest Neighbors classifier.
        Parameters
        ----------
        b1 : int, optional
            Number of neighbors to consider for classification. Default is 5.
        b2 : function, optional
            The distance metric to use. Default is Euclidean distance.
        '''
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, b3, b4):
        '''
        Fit the K Nearest Neighbors model with the given training data.
        Parameters
        ----------
        b3 : array-like, shape (n_samples, n_features)
            The training samples.
        b4 : array-like, shape (n_samples,)
            The target labels corresponding to the training data.
        '''
        self.b3 = b3
        self.b4 = b4
    def fonk3(self, b10):
        '''
        Predict the labels for a set of test samples.
        Parameters
        ----------
        b10 : array-like, shape (n_samples, n_features)
            The test samples for which to predict the labels.
        Returns
        -------
        predicted_labels : array-like, shape (n_samples,)
            The predicted labels for the test samples.
        '''
        b5 = []
        for sample in b10:
            b6 = self.b2(sample.reshape(1, -1), self.b3)
            b7 = np.argpartition(b6, self.b1 - 1)[:self.b1]
            b8 = np.argmax(np.bincount(self.b4[b7].astype(int)))
            b5.append(b8)
        return np.array(b5)
if b9 = = "__main__":
    b3 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b4 = np.array([0, 0, 1, 1])
    b10 = np.array([[1.5, 2.5], [3.5, 4.5]])
    b11 = class1(b1=2)
    b11.fonk2(b3, b4)
    b5 = b11.fonk3(b10)
    print("Predictions:", b5)