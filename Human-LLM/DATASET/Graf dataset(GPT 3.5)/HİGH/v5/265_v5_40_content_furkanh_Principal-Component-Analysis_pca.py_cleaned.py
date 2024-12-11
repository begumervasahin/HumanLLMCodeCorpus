import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
    def fonk2(self, X):
        if self.b1 is None or self.b1 > X.shape[0]:
            self.b1 = X.shape[0]
        self.b2 = np.b2(X, axis=0)
        b3 = X - self.b2
        b4 = np.matmul(b3.T, b3) / (X.shape[0] - 1)
        b7, b5 = np.linalg.eig(b4)
        b6 = b7.argsort()[::-1]
        b5 = b5[:, b6]
        b7 = b7[b6][::-1]
        self.b7 = np.real(b7)
        self.b5 = np.real(b5)
        b8 = np.sum(self.b7)
        a1 = 0
        self.b9 = []
        for i in range(self.b7.shape[0]):
            a1 += self.b7[i]
            self.b9.append(a1 / b8)
    def fonk3(self, X):
        b3 = X - self.b2
        b10 = np.matmul(b3, self.b5)[:, :self.b1]
        return b10