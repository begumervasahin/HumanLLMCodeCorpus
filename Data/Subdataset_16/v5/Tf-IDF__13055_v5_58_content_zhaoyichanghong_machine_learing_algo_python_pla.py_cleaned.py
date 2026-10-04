import numpy as np
import metrics
class class1:
    def fonk1(self):
        self.b1 = None
        self.a1 = 0
    def fonk2(self, X, y):
        n_samples, b2 = X.shape
        self.b1 = np.zeros(b2)
        self.a1 = 0
        while True:
            b3 = False
            for i in range(n_samples):
                b4 = self.fonk4(X[i])
                if y[i] * b4 <= 0:
                    self.b1 += y[i] * X[i]
                    self.a1 += y[i]
                    b3 = True
            if not b3:
                break
    def fonk3(self, X):
        return np.sign(X.dot(self.b1) + self.a1)
    def fonk4(self, x):
        return np.sign(np.dot(x, self.b1) + self.a1)