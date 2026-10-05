import numpy as np
import metrics
class class1:
    def fonk1(self, X, y):
        '''
        Train the Perceptron model.
        Parameters
        ----------
        X : array-like, shape (n_samples, b1)
            Training data.
        y : array-like, shape (n_samples,)
            Target values, where 1 or -1 indicate the class.
        '''
        n_samples, b1 = X.shape
        self.b2 = np.zeros(b1)
        self.a1 = 0
        while True:
            for i in range(n_samples):
                b3 = self.fonk2(X[i])
                if y[i] * b3 <= 0:
                    self.b2 += (y[i] * X[i]).reshape(self.b2.shape)
                    self.a1 += y[i]
            b4 = self.fonk2(X)
            if metrics.accuracy(y, b4) == 1:
                break
    def fonk2(self, X):
        '''
        Predict class class2 for samples.
        Parameters
        ----------
        X : array-like, shape (n_samples, b1)
            Predicting data.
        Returns
        -------
        y : array-like, shape (n_samples,)
            Predicted class class3 per sample, where 1 or -1 indicate the class.
        '''
        return np.sign(X.dot(self.b2) + self.a1)