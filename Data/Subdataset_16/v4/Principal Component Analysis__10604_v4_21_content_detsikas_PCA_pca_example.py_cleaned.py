import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
def fonk1(X, b1 = "PCA b6"):
    plt.clf()
    plt.b1(b1)
    plt.scatter(X[:, 0], X[:, 1], b2 = "b", marker='o')
    plt.xlabel('Fahrenheit')
    plt.ylabel('Celsius')
    plt.xlim(X.min(b3 = 0)[0], X.max(b3=0)[0])
    plt.ylim(X.min(b3 = 0)[1], X.max(b3=0)[1])
    plt.show()
def fonk2(size, b4 = 1.0):
    b5 = np.linspace(0, 50, num=size)
    b6 = np.c_[b5, b5]
    b7 = (np.random.rand(size) - 0.5) * b4
    b8 = np.c_[-b7, 44.8 * b7 + 5]
    b6 += b8
    return b6
def fonk3(size, b4 = 1.0):
    b7 = (np.random.rand(size) - 0.5) * b4
    b9 = np.linspace(0, 100, num=size) + b7
    b7 = (np.random.rand(size) - 0.5) * b4
    b10 = (b9 - 32.0) * 5.0 / 9.0 + b7
    b6 = np.c_[b9, b10]
    return b6
b6 = fonk3(100, 4.0)
fonk1(b6, b1 = "Original Data")
b11 = scale(b6)
b12 = PCA()
b13 = b12.fit_transform(b11)
print(f"Number of principal components: {b12.n_components_}")
print(f"Components b4: {b12.explained_variance_}")
print(f"Components b4 ratio: {b12.explained_variance_ratio_}")
print(f"Principal components: {b12.components_}")
b14 = np.dot(b13[:, 0].reshape((100, 1)), b12.components_[0].reshape((1, 2)))
fonk1(b14, b1 = "Manually Reconstructed Data")
b12 = PCA(1)
b13 = b12.fit_transform(b11)
b15 = b12.inverse_transform(b13)
fonk1(b15, b1 = "PCA Reconstructed Data")
b16 = np.mean(np.linalg.norm(b11 - b15, b3=1))
print(f"Mean squared reconstruction error: {b16}")