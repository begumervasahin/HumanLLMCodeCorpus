import numpy as np
from sklearn.metrics import accuracy_score
class class1:
    def fonk1(self, b6, b7):
        '''
        Fit the Perceptron Learning Algorithm to the training data.
        Parameters
        ----------
        b6 : numpy.ndarray
            Training data of shape (n_samples, b1).
        b7 : numpy.ndarray
            Target values of shape (n_samples,).
        '''
        n_samples, b1 = b6.shape
        self.b2 = np.zeros(b1)
        self.a1 = 0
        while True:
            for i in range(n_samples):
                b3 = self.fonk2(b6[i])
                if b7[i] * b3 <= 0:
                    self.b2 += (b7[i] * b6[i]).reshape(self.b2.shape)
                    self.a1 += b7[i]
            b4 = self.fonk2(b6)
            if accuracy_score(b7, b4) == 1:
                break
    def fonk2(self, X):
        '''
        Predict class class2 for input data.
        Parameters
        ----------
        X : numpy.ndarray
            Input data of shape (n_samples, b1).
        Returns
        -------
        numpy.ndarray
            Predicted class class3 of shape (n_samples,).
        '''
        return np.sign(X.dot(self.b2) + self.a1)
if b5 = = "__main__":
    b6 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b7 = np.array([1, 1, -1, -1])
    b8 = class1()
    b8.fonk1(b6, b7)
    b9 = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    b4 = b8.fonk2(b9)
    print("Predictions:", b4)