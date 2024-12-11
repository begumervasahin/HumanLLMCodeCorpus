import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class class1:
    def fonk1(self, b1 = 2):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, data, b3 = 500, seed=42, b14=False):
        min_x, b4 = np.min(data, b9=0) - 1
        max_x, b5 = np.max(data, b9=0) + 1
        self.b2 = np.array([[np.random.randint(min_x, max_x), np.random.randint(b4, b5)] for b12 in range(self.b1)])
        b6 = np.array([])
        b7 = None
        for b12 in range(b3):
            b6 = np.copy(self.b2)
            b7 = self.fonk3(data)
            self.fonk4(data, b7)
            if np.array_equal(self.b2, b6):
                break
        b7 = self.fonk3(data)
        if b14:
            self.fonk5(data, b7, (min_x, max_x), (b4, b5))
    def fonk3(self, data):
        b8 = np.array([np.sqrt(np.sum((data - centroid) ** 2, b9=1)) for centroid in self.b2])
        return np.argmin(b8, b9 = 0)
    def fonk4(self, data, cluster_assignments):
        for i in range(self.b1):
            b10 = data[cluster_assignments == i]
            if len(b10) > 0:
                self.b2[i] = np.mean(b10, b9 = 0)
    def fonk5(self, data, cluster_assignments, x_lim, y_lim):
        plt.figure()
        plt.scatter(data[:, 0], data[:, 1], b11 = cluster_assignments, cmap=plt.cm.Paired, alpha=0.6)
        plt.scatter(self.b2[:, 0], self.b2[:, 1], b11 = range(self.b1), cmap=plt.cm.Paired, edgecolor='k')
        plt.xlim(x_lim[0], x_lim[1])
        plt.ylim(y_lim[0], y_lim[1])
        plt.show()
data, b12 = make_blobs(n_samples=100, centers=3, n_features=2)
b13 = class1(b1=3)
b13.fonk2(data, b14 = True)