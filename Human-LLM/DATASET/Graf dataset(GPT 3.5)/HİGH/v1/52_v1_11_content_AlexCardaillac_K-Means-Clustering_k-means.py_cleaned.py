import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
class class1:
    def fonk1(self, b1 = 2):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, inputs, b3 = 500, seed=42, b14=False):
        if b14:
            import matplotlib.pyplot as plt
        min_x, b4 = np.amin(inputs, 0) - 1
        max_x, b5 = np.amax(inputs, 0) + 1
        self.b2 = np.array([[np.random.randint(min_x, max_x), np.random.randint(b4, b5)] for b12 in range(self.b1)])
        b6 = np.array([])
        b7 = None
        while not np.array_equal(self.b2, b6):
            b6 = self.b2
            b7 = self.fonk3(inputs)
            self.fonk4(inputs, b7)
        b7 = self.fonk3(inputs)
        if b14:
            self.fonk5(inputs, b7, (min_x, max_x), (b4, b5))
    def fonk3(self, inputs):
        b8 = []
        for centroid in self.b2:
            b8.append(np.sqrt((inputs[:, 0] - centroid[0]) ** 2 + (inputs[:, 1] - centroid[1]) ** 2))
        return np.argmin(b8, 0)
    def fonk4(self, inputs, b9):
        for i, centroid in enumerate(self.b2):
            centroid[0] = np.mean(inputs[:, 0][b9 = = i])
            centroid[1] = np.mean(inputs[:, 1][b9 = = i])
    def fonk5(self, inputs, b9, x_lim, y_lim):
        b10 = plt.figure()
        plt.scatter(inputs[:, 0], inputs[:, 1], b11 = b9, cmap=plt.cm.Paired, alpha=0.6)
        plt.scatter(self.b2[:, 0], self.b2[:, 1], b11 = range(self.b1), cmap=plt.cm.Paired, edgecolor='b1')
        plt.xlim(x_lim[0], x_lim[1])
        plt.ylim(y_lim[0], y_lim[1])
        plt.show()
X, b12 = make_blobs(n_samples=100, centers=3, n_features=2)
b13 = class1(b1=3)
b13.fonk2(X, b14 = True)