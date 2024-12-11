import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class class1:
    def fonk1(self, b1 = 2):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, inputs, b3 = 500, seed=42, b15=False):
        min_x, b4 = np.min(inputs, b9=0) - 1
        max_x, b5 = np.max(inputs, b9=0) + 1
        self.b2 = np.array([[np.random.randint(min_x, max_x), np.random.randint(b4, b5)] for b13 in range(self.b1)])
        b6 = np.array([])
        b7 = None
        while not np.array_equal(self.b2, b6):
            b6 = self.b2
            b7 = self.fonk3(inputs)
            self.fonk4(inputs, b7)
        b7 = self.fonk3(inputs)
        if b15:
            self.fonk5(inputs, b7, (min_x, max_x), (b4, b5))
    def fonk3(self, inputs):
        b8 = []
        for centroid in self.b2:
            b8.append(np.sqrt((inputs.T[0] - centroid[0]) ** 2 + (inputs.T[1] - centroid[1]) ** 2))
        return np.argmin(b8, b9 = 0)
    def fonk4(self, inputs, b10):
        for i, centroid in enumerate(self.b2):
            centroid[0] = np.mean(inputs.T[0][b10 = = i])
            centroid[1] = np.mean(inputs.T[1][b10 = = i])
    def fonk5(self, inputs, b10, x_lim, y_lim):
        b11 = plt.figure()
        plt.scatter(inputs.T[0], inputs.T[1], b12 = b10, cmap=plt.cm.Paired, alpha=0.6)
        plt.scatter(self.b2.T[0], self.b2.T[1], b12 = range(self.b1), cmap=plt.cm.Paired, edgecolor='b1')
        plt.xlim(x_lim[0], x_lim[1])
        plt.ylim(y_lim[0], y_lim[1])
        plt.show()
X, b13 = make_blobs(n_samples=100, centers=3, n_features=2)
b14 = class1(b1=3)
b14.fonk2(X, b15 = True)