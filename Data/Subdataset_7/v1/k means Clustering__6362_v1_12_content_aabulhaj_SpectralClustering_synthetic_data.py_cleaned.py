import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def fonk1():
    b1 = np.arange(0, 2 * np.pi, 0.03)
    b2 = np.shape(b1)[0]
    b3 = np.array([np.cos(b1) + 0.1 * np.random.randn(b2),
                        np.sin(b1) + 0.1 * np.random.randn(b2)]).T
    b4 = np.array([2 * np.cos(b1) + 0.1 * np.random.randn(b2),
                        2 * np.sin(b1) + 0.1 * np.random.randn(b2)]).T
    b5 = np.array([3 * np.cos(b1) + 0.1 * np.random.randn(b2),
                        3 * np.sin(b1) + 0.1 * np.random.randn(b2)]).T
    b6 = np.array([4 * np.cos(b1) + 0.1 * np.random.randn(b2),
                        4 * np.sin(b1) + 0.1 * np.random.randn(b2)]).T
    b7 = np.concatenate((b3, b4, b5, b6), axis=0)
    return b7
def fonk2():
    b8 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, b9 = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, b8=b8, shuffle=False, random_state=99)
    return X
b10 = fonk1()
b11 = fonk2()
plt.figure(b12 = (8, 8))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(b10[:, 0], b10[:, 1], b13 = 5)
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(b11[:, 0], b11[:, 1], b13 = 5)
plt.show()