import numpy as np
from sklearn.datasets import make_blobs
def fonk1(b1 = 209):
    b2 = np.linspace(0, 2 * np.pi, b1)
    b3 = fonk2(b2, 1)
    b4 = fonk2(b2, 2)
    b5 = fonk2(b2, 3)
    b6 = fonk2(b2, 4)
    b7 = np.concatenate((b3, b4, b5, b6), axis=1)
    return b7.T
def fonk2(b2, radius):
    return np.array([
        radius * np.cos(b2) + 0.1 * np.random.randn(len(b2)),
        radius * np.sin(b2) + 0.1 * np.random.randn(len(b2))
    ])
def fonk3(b8 = 3000, num_features=2, cluster_std=1.0, random_state=99):
    b9 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, b10 = make_blobs(n_samples=b8, n_features=num_features, cluster_std=cluster_std, b9=b9, shuffle=False, random_state=random_state)
    return X