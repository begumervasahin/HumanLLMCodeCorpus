import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def fonk1():
    b1 = np.arange(0, 2 * np.pi, 0.03)
    b2 = len(b1)
    def fonk2(radius):
        return np.array([radius * np.cos(b1) + 0.1 * np.random.randn(b2),
                         radius * np.sin(b1) + 0.1 * np.random.randn(b2)]).T
    b3 = fonk2(1)
    b4 = fonk2(2)
    b5 = fonk2(3)
    b6 = fonk2(4)
    b7 = np.concatenate((b3, b4, b5, b6), axis=0)
    return b7
def fonk3():
    b8 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    b12, b9 = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, b8=b8, shuffle=False, random_state=99)
    return b12
def fonk4(b7, b12):
    plt.figure(b10 = (16, 8))
    plt.subplot(1, 2, 1)
    plt.title('Circles')
    plt.scatter(b7[:, 0], b7[:, 1], b11 = 5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.subplot(1, 2, 2)
    plt.title('Blobs')
    plt.scatter(b12[:, 0], b12[:, 1], b11 = 5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.tight_layout()
    plt.show()
b7 = fonk1()
b12 = fonk3()
fonk4(b7, b12)