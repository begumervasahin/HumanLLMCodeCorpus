import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
class class1:
    def fonk1(self, b2, b3, b4, b1 = euclidean_distances):
        '''
        Fit the K Nearest Neighbors model with the given training data.
        Parameters
        ----------
        b2 : array-like, shape (n_samples, n_features)
            The training samples.
        b3 : array-like, shape (n_samples,)
            The target labels corresponding to the training data.
        b4 : int
            Number of neighbors to consider for classification.
        b1 : function, optional
            The distance metric to use. Default is Euclidean distance.
        '''
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
    def fonk2(self, sample):
        '''
        Predict the label for a single sample.
        Parameters
        ----------
        sample : array-like, shape (n_features,)
            The sample for which to predict the label.
        Returns
        -------
        label : int
            The predicted label for the sample.
        '''
        b5 = self.b1(sample.reshape(1, -1), self.b2)
        b6 = np.argpartition(b5, self.b4 - 1)[:self.b4]
        return np.argmax(np.bincount(self.b3[b6].astype(int)))
    def fonk3(self, b8):
        '''
        Predict the labels for a set of test samples.
        Parameters
        ----------
        b8 : array-like, shape (n_samples, n_features)
            The test samples for which to predict the labels.
        Returns
        -------
        predicted_labels : array-like, shape (n_samples,)
            The predicted labels for the test samples.
        '''
        return np.apply_along_axis(self.__predict_single_sample, 1, b8)
if b7 = = "__main__":
    b2 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b3 = np.array([0, 0, 1, 1])
    b8 = np.array([[1.5, 2.5], [3.5, 4.5]])
    b9 = class1()
    b9.fonk1(b2, b3, b4 = 2)
    b10 = b9.fonk3(b8)
    print("Predictions:", b10)