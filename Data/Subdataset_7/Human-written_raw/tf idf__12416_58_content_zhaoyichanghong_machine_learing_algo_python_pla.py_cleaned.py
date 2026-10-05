import numpy as np
import metrics
class class1:
    def fonk1(self, X, y):
        '''
        Parameters
        ----------
        X : shape (n_samples, b1)
            Training data
        y : shape (n_samples,)
            Target values, 1 or -1
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
            b3 = self.fonk2(X)
            if metrics.accuracy(y, b3) == 1:
                break
    def fonk2(self, X):
        '''
        Parameters
        ----------
        X : shape (n_samples, b1)
            Predicting data
        Returns
        -------
        y : shape (n_samples,)
            Predicted class class2 per sample, 1 or -1
        '''
        return np.sign(X.dot(self.b2) + self.a1)