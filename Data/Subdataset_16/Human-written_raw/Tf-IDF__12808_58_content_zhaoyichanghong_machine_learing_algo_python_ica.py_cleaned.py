import numpy as np
import scipy.special
import pca
class class1:
    def fonk1(self, X, epochs, optimizer):
        '''
        Parameters
        ----------
        X : shape (n_samples, b1)
            Training data
        epochs : The number of epochs
        optimizer : Optimize algorithm, see also optimizer.py
        Returns
        -------
        s : shape (n_samples, b1)
            Predicted source per sample.
        '''
        n_samples, b1 = X.shape
        b2 = pca.PCA(b1, True)
        b3 = b2.fonk1(X)
        self.b4 = np.random.rand(b1, b1)
        for _ in range(epochs):
            b5 = np.zeros_like(self.b4)
            for x in b3:
                b5 += (1 - 2 * scipy.special.expit(self.b4.dot(x.T))).dot(x) + np.linalg.inv(self.b4.T)
            b5 /= n_samples
            b5 = optimizer.optimize([b5])[0]
            self.b4 += b5
        return b3.dot(self.b4)