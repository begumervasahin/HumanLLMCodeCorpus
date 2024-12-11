import numpy as np
import timeit
import matplotlib.pyplot as plt
from load_data import load_mnist
from sklearn.decomposition import PCA as SKPCA
import pandas as pd
b1 = load_mnist()
images, b2 = b1['data'], b1['target']
def fonk1(b21):
    b3 = np.mean(b21, b13=0)
    b4 = np.b4(b21, b13=0)
    b5 = b4.copy()
    b5[b4 = = 0] = 1.
    b6 = (b21 - b3) / b5
    return b6, b3, b4
def fonk2(b21, num_components):
    b21, mean, b4 = fonk1(b21)
    b7 = np.cov(b21, rowvar=False, bias=True)
    b10, b8 = np.linalg.eig(b7)
    b9 = b10.argsort()[::-1]
    b10 = b10[b9]
    b8 = b8[:, b9]
    b11 = b8[:, :num_components]
    b12 = np.dot(b11.T, b21.T).T
    return b12
def fonk3(predict, actual):
    return np.square(predict - actual).sum(b13 = 1).mean()
def fonk4(f, b14 = 10):
    b15 = []
    for _ in range(b14):
        b16 = timeit.default_timer()
        f()
        b17 = timeit.default_timer()
        b15.append(b17 - b16)
    return np.mean(b15), np.b4(b15)
def fonk5(b21, n_components):
    N, b18 = b21.shape
    b19 = (b21 @ b21.T) / N
    b10, b8 = np.linalg.eig(b19)
    b9 = b10.argsort()[::-1]
    b10 = b10[b9]
    b8 = b8[:, b9]
    b20 = b8[:, :n_components]
    b11 = b20 @ np.linalg.inv(b20.T @ b20) @ b20.T
    b12 = b11 @ b21.T
    return b12.T
a1 = 1000
b21 = (images.reshape(-1, 28 * 28)[:a1]) / 255.
b6, b3, b4 = fonk1(b21)
np.testing.assert_almost_equal(fonk2(b6, 2), fonk5(b6, 2))
b22 = []
for num_component in range(1, 100):
    b23 = fonk2(b6, num_component)
    b24 = fonk3(b23, b6)
    b22.append((num_component, b24))
b22 = np.asarray(b22)
plt.plot(b22[:, 0], b22[:, 1])
plt.axhline(100, b25 = '--', color='r', linewidth=2)
plt.xlabel('num_components')
plt.ylabel('MSE')
plt.title('MSE vs number of principal components')
plt.show()
b26 = []
b27 = []
for datasetsize in np.arange(4, 784, b28 = 50):
    b29 = b6[:datasetsize]
    b3, b30 = fonk4(lambda: b29.T @ b29)
    b26.append((datasetsize, b3, b30))
    b3, b30 = fonk4(lambda: b29 @ b29.T)
    b27.append((datasetsize, b3, b30))
b26 = np.asarray(b26)
b27 = np.asarray(b27)
plt.errorbar(b26[:, 0], b26[:, 1], b26[:, 2], b31 = '$b21^T b21$ (PCA)', linewidth=2)
plt.errorbar(b27[:, 0], b27[:, 1], b27[:, 2], b31 = '$b21 b21^T$ (PCA_high_dim)', linewidth=2)
plt.xlabel('size of dataset')
plt.ylabel('running time')
plt.legend()
plt.show()
b32 = []
b33 = []
for datasetsize in np.arange(4, 784, b28 = 100):
    b29 = b6[:datasetsize]
    a2 = 2
    b3, b30 = fonk4(lambda: fonk2(b29, a2), b14=10)
    b32.append((datasetsize, b3, b30))
    b3, b30 = fonk4(lambda: fonk5(b29, a2), b14=10)
    b33.append((datasetsize, b3, b30))
b32 = np.asarray(b32)
b33 = np.asarray(b33)
plt.errorbar(b32[:, 0], b32[:, 1], b32[:, 2], b31 = 'PCA', linewidth=2)
plt.errorbar(b33[:, 0], b33[:, 1], b33[:, 2], b31 = 'PCA_high_dim', linewidth=2)
plt.xlabel('number of datapoints')
plt.ylabel('run time')
plt.legend()
plt.show()
print("Time taken for PCA:", fonk4(lambda: fonk2(b6, 2)))
print("Time taken for PCA_high_dim:", fonk4(lambda: fonk5(b6, 2)))