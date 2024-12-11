import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def fonk1():
    b1 = np.arange(0, 2 * np.pi, 0.03)
    b2 = len(b1)
    a1 = 0.1
    b3 = fonk2(b1, a1)
    b4 = fonk2(b1, a1, b8=2)
    b5 = fonk2(b1, a1, b8=3)
    b6 = fonk2(b1, a1, b8=4)
    return np.concatenate((b3, b4, b5, b6), b7 = 0)
def fonk2(b1, a1, b8 = 1):
    b9 = b8 * np.cos(b1) + a1 * np.random.randn(len(b1))
    b10 = b8 * np.sin(b1) + a1 * np.random.randn(len(b1))
    return np.column_stack((b9, b10))
def fonk3():
    b11 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, b12 = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, b11=b11, shuffle=False, random_state=99)
    return X
b13 = fonk1()
b14 = fonk3()
plt.figure(b15 = (12, 6))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(b13[:, 0], b13[:, 1], b16 = 5)
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(b14[:, 0], b14[:, 1], b16 = 5)
plt.tight_layout()
plt.show()