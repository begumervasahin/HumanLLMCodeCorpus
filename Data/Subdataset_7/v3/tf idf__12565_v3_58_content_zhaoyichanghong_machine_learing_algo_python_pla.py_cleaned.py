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
                    self.fonk3(b6[i], b7[i])
            b4 = self.fonk4(b6)
            if self.fonk5(b7, b4):
                break
    def fonk2(self, sample):
        '''
        Predict class class2 for a single input sample.
        Parameters
        ----------
        sample : numpy.ndarray
            Input sample of shape (b1,).
        Returns
        -------
        int
            Predicted class class3, 1 or -1.
        '''
        return np.sign(np.dot(sample, self.b2) + self.a1)
    def fonk3(self, sample, target):
        '''
        Update b2 and a1 based on misclassified sample.
        Parameters
        ----------
        sample : numpy.ndarray
            Input sample of shape (b1,).
        target : int
            Target class class4 for the sample, 1 or -1.
        '''
        self.b2 += target * sample
        self.a1 += target
    def fonk4(self, X):
        '''
        Predict class class5 for input data.
        Parameters
        ----------
        X : numpy.ndarray
            Input data of shape (n_samples, b1).
        Returns
        -------
        numpy.ndarray
            Predicted class class6 of shape (n_samples,).
        '''
        return np.sign(np.dot(X, self.b2) + self.a1)
    def fonk5(self, y_true, y_pred):
        '''
        Check if the model has converged based on accuracy.
        Parameters
        ----------
        y_true : numpy.ndarray
            True class class7 of shape (n_samples,).
        y_pred : numpy.ndarray
            Predicted class class8 of shape (n_samples,).
        Returns
        -------
        bool
            True if accuracy is 100%, False otherwise.
        '''
        return accuracy_score(y_true, y_pred) == 1
if b5 = = "__main__":
    b6 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b7 = np.array([1, 1, -1, -1])
    b8 = class1()
    b8.fonk1(b6, b7)
    b9 = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
    b4 = b8.fonk4(b9)
    print("Predictions:", b4)