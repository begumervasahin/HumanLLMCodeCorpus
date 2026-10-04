import numpy as np
import scipy.special
import pca
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, X, epochs, optimizer):
        b7, b2 = X.shape
        b3 = self.fonk3(X, b2)
        self.b1 = self.fonk4(b2)
        for _ in range(epochs):
            b4 = self.fonk5(b3)
            self.b1 += optimizer.optimize([b4])[0]
        b5 = self.fonk6(b3)
        return b5
    def fonk3(self, X, b2):
        b6 = pca.PCA(b2, whiten=True)
        return b6.fonk2(X)
    def fonk4(self, b2):
        return np.random.rand(b2, b2)
    def fonk5(self, b3):
        b7 = b3.shape[0]
        b4 = np.zeros_like(self.b1)
        for x in b3:
            b8 = 1 - 2 * scipy.special.expit(self.b1.dot(x.T))
            b9 = np.linalg.inv(self.b1.T)
            b4 += b8[:, None] * x + b9
        return b4 / b7
    def fonk6(self, b3):
        return b3.dot(self.b1)