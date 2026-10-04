import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
np.random.seed(0)
X, b1 = make_circles(n_samples=400, factor=0.3, noise=0.05)
b2 = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
b3 = b2.fit_transform(X)
b4 = b2.inverse_transform(b3)
b5 = PCA()
b6 = b5.fit_transform(X)
def fonk1(ax, X, b1):
    ax.set_title("Original space")
    b7 = b1 == 0
    b8 = b1 == 1
    ax.plot(X[b7, 0], X[b7, 1], "ro")
    ax.plot(X[b8, 0], X[b8, 1], "bo")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    X1, b9 = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-1.5, 1.5, 50))
    b10 = np.array([X1.ravel(), b9.ravel()]).T
    b11 = b2.transform(b10)[:, 0].reshape(X1.shape)
    ax.contour(X1, b9, b11, b12 = 'grey', linewidths=1, origin='lower')
def fonk2(ax, b6, b1):
    ax.set_title("Projection by PCA")
    b7 = b1 == 0
    b8 = b1 == 1
    ax.plot(b6[b7, 0], b6[b7, 1], "ro")
    ax.plot(b6[b8, 0], b6[b8, 1], "bo")
    ax.set_xlabel("1st principal component")
    ax.set_ylabel("2nd component")
def fonk3(ax, b3, b1):
    ax.set_title("Projection by KPCA")
    b7 = b1 == 0
    b8 = b1 == 1
    ax.plot(b3[b7, 0], b3[b7, 1], "ro")
    ax.plot(b3[b8, 0], b3[b8, 1], "bo")
    ax.set_xlabel("1st principal component in space induced by $\phi$")
    ax.set_ylabel("2nd component")
def fonk4(ax, b4, b1):
    ax.set_title("Original space after inverse transform")
    b7 = b1 == 0
    b8 = b1 == 1
    ax.plot(b4[b7, 0], b4[b7, 1], "ro")
    ax.plot(b4[b8, 0], b4[b8, 1], "bo")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
fig, b13 = plt.subplots(2, 2, figsize=(12, 12), subplot_kw={'aspect': 'equal'})
fonk1(b13[0, 0], X, b1)
fonk2(b13[0, 1], b6, b1)
fonk3(b13[1, 0], b3, b1)
fonk4(b13[1, 1], b4, b1)
plt.subplots_adjust(0.02, 0.10, 0.98, 0.94, 0.04, 0.35)
plt.show()