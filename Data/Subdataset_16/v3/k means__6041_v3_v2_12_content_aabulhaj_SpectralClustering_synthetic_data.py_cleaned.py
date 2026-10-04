
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def fonk1(b1 = 210, noise_level=0.1):
    b2 = np.linspace(0, 2 * np.pi, b1)
    b3 = [1, 2, 3, 4]
    b4 = []
    for r in b3:
        b5 = r * np.cos(b2) + noise_level * np.random.randn(b1)
        b6 = r * np.sin(b2) + noise_level * np.random.randn(b1)
        b4.append(np.vstack((b5, b6)).T)
    return np.vstack(b4)
def fonk2(b7 = 3000, cluster_std=1.0, random_state=99):
    b8 = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, b9 = make_blobs(n_samples=b7, n_features=2, cluster_std=cluster_std, b8=b8, random_state=random_state)
    return X
b10 = fonk1()
b11 = fonk2()
plt.figure(b12 = (16, 8))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(b10[:, 0], b10[:, 1], b13 = 5, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(b11[:, 0], b11[:, 1], b13 = 5, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()