import numpy as np
from sklearn.datasets import make_blobs
def fonk1():
    b1 = np.arange(0, 2 * np.pi, 0.03)
    b2 = np.shape(b1)
    b2 = b2[0]
    b3 = np.matrix([np.cos(b1) + 0.1 * np.random.randn(b2),
                         np.sin(b1) + 0.1 * np.random.randn(b2)])
    b4 = np.matrix([2 * np.cos(b1) + 0.1 * np.random.randn(b2),
                         2 * np.sin(b1) + 0.1 * np.random.randn(b2)])
    b5 = np.matrix([3 * np.cos(b1) + 0.1 * np.random.randn(b2),
                         3 * np.sin(b1) + 0.1 * np.random.randn(b2)])
    b6 = np.matrix([4 * np.cos(b1) + 0.1 * np.random.randn(b2),
                         4 * np.sin(b1) + 0.1 * np.random.randn(b2)])
    b7 = np.concatenate((b3, b4, b5, b6), axis=1)
    return np.array(b7.T)
def fonk2():
    b8 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, b9 = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, b8=b8, shuffle=False, random_state=99)
    return X