import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class class1:
    def fonk1(self, b1 = 2, b2=500, seed=42):
        self.b1 = b1
        self.b2 = b2
        np.random.seed(seed)
        self.b3 = []
    def fonk2(self, inputs, b4 = False):
        self.fonk3(inputs)
        for b13 in range(self.b2):
            b5 = self.fonk4(inputs)
            b6 = self.fonk5(inputs, b5)
            if np.all(b6 = = self.b3):
                break
            self.b3 = b6
        if b4:
            self.fonk6(inputs, b5)
    def fonk3(self, inputs):
        min_x, b7 = np.min(inputs, b10=0) - 1
        max_x, b8 = np.max(inputs, b10=0) + 1
        self.b3 = np.array([[np.random.uniform(min_x, max_x), np.random.uniform(b7, b8)] for b13 in range(self.b1)])
    def fonk4(self, inputs):
        b9 = np.sqrt(((inputs - self.b3[:, np.newaxis])**2).sum(b10=2))
        return np.argmin(b9, b10 = 0)
    def fonk5(self, inputs, b5):
        return np.array([inputs[b5 = = b1].mean(b10=0) for b1 in range(self.b1)])
    def fonk6(self, inputs, b5):
        plt.figure(b11 = (8, 6))
        plt.scatter(inputs[:, 0], inputs[:, 1], b12 = b5, cmap='viridis', alpha=0.5)
        plt.scatter(self.b3[:, 0], self.b3[:, 1], b12 = 'red', s=100, marker='X')
        plt.title('class1 Clustering')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.show()
X, b13 = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)
b14 = class1(b1=3)
b14.fonk2(X, b4 = True)