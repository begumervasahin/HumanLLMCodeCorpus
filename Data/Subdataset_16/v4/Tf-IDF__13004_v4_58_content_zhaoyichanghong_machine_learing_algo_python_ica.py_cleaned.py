import numpy as np
import scipy.special
import pca
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, X, epochs, optimizer):
        n_samples, b2 = X.shape
        b3 = pca.PCA(b2, whiten=True)
        b4 = b3.fonk2(X)
        self.b1 = np.random.rand(b2, b2)
        for epoch in range(epochs):
            b5 = np.zeros_like(self.b1)
            for x in b4:
                b6 = 1 - 2 * scipy.special.expit(self.b1.dot(x.T))
                b7 = np.linalg.inv(self.b1.T)
                b5 += b6[:, None] * x + b7
            b5 /= n_samples
            self.b1 += optimizer.optimize([b5])[0]
        b8 = b4.dot(self.b1)
        return b8