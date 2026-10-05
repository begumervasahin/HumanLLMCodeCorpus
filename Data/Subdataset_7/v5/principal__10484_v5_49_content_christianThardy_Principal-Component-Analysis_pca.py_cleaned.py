import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as SKPCA
from load_data import load_mnist
import timeit
b1 = load_mnist()
images, b2 = b1['data'], b1['target']
plt.figure(b3 = (4, 4))
plt.imshow(images[0].reshape(28, 28), b4 = 'gray')
plt.show()
def fonk1(b16):
    b5 = np.mean(b16, b15=0)
    b6 = np.b6(b16, b15=0)
    b7 = np.where(b6 == 0, 1., b6)
    b8 = (b16 - b5) / b7
    return b8, b5, b6
def fonk2(S):
    b11, b9 = np.linalg.eig(S)
    b10 = np.argsort(b11)[::-1]
    b11 = b11[b10]
    b9 = b9[:, b10]
    return b11, b9
def fonk3(B):
    return B @ np.linalg.inv(B.T @ B) @ B.T
def fonk4(b16, num_components):
    b8, mean, b6 = fonk1(b16)
    b12 = np.cov(b8, rowvar=False, bias=True)
    b11, b9 = fonk2(b12)
    b13 = fonk3(b9[:, :num_components])
    b14 = (b13 @ b8.T).T
    return b14
def fonk5(predict, actual):
    return np.square(predict - actual).sum(b15 = 1).mean()
a1 = 1000
b16 = (images.reshape(-1, 28 * 28)[:a1]) / 255.
b8, b5, b6 = fonk1(b16)
b17 = []
for num_component in range(1, 100):
    b14 = fonk4(b8, num_component)
    b18 = fonk5(b14, b8)
    b17.append((num_component, b18))
b17 = np.asarray(b17)
plt.plot(b17[:, 0], b17[:, 1])
plt.axhline(100, b19 = '--', color='r', linewidth=2)
plt.xlabel('Number of Components')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs Number of Principal Components')
plt.xticks(np.arange(1, 100, 5))
plt.show()
def fonk6(b16, n_components):
    N, b20 = b16.shape
    b21 = (b16 @ b16.T) / N
    b11, b9 = fonk2(b21)
    b22 = (b16.T @ b9)[:, :n_components]
    b23 = fonk3(b22)
    b14 = (b23 @ b16.T).T
    return b14
np.testing.assert_almost_equal(fonk4(b8, 2), fonk6(b8, 2))
def fonk7(f, b24 = 10):
    b25 = []
    for _ in range(b24):
        b26 = timeit.default_timer()
        f()
        b27 = timeit.default_timer()
        b25.append(b27 - b26)
    return np.mean(b25), np.b6(b25)
b28 = np.arange(4, 784, step=100)
b29 = []
b30 = []
for dataset_size in b28:
    b31 = b8[:dataset_size]
    b5, b32 = fonk7(lambda: b31.T @ b31)
    b29.append((dataset_size, b5, b32))
    b5, b32 = fonk7(lambda: b31 @ b31.T)
    b30.append((dataset_size, b5, b32))
b29 = np.asarray(b29)
b30 = np.asarray(b30)
plt.errorbar(b29[:, 0], b29[:, 1], b29[:, 2], b33 = '$b16^T b16$ (PCA)', linewidth=2)
plt.errorbar(b30[:, 0], b30[:, 1], b30[:, 2], b33 = '$b16 b16^T$ (PCA_high_dim)', linewidth=2)
plt.xlabel('Size of Dataset')
plt.ylabel('Running Time')
plt.legend()
plt.show()
b34 = []
b35 = []
for dataset_size in b28:
    b31 = b8[:dataset_size]
    b5, b32 = fonk7(lambda: fonk4(b31, 2), b24=10)
    b34.append((dataset_size, b5, b32))
    b5, b32 = fonk7(lambda: fonk6(b31, 2), b24=10)
    b35.append((dataset_size, b5, b32))
b34 = np.asarray(b34)
b35 = np.asarray(b35)
plt.errorbar(b34[:, 0], b34[:, 1], b34[:, 2], b33 = 'PCA', linewidth=2)
plt.errorbar(b35[:, 0], b35[:, 1], b35[:, 2], b33 = 'PCA_high_dim', linewidth=2)
plt.xlabel('Number of Datapoints')
plt.ylabel('Run Time')
plt.legend()
plt.show()
print("Time taken for PCA:", fonk7(lambda: fonk4(b8, 2)))
print("Time taken for PCA_high_dim:", fonk7(lambda: fonk6(b8, 2)))