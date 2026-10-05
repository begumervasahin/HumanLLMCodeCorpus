import numpy as np
import timeit
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA as SKPCA
from load_data import load_mnist
MNIST = load_mnist()
images, labels = MNIST['data'], MNIST['target']
plt.figure(figsize=(4, 4))
plt.imshow(images[0].reshape(28, 28), cmap='gray')
plt.show()
def normalize(X):
    mu = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std_filled = np.where(std == 0, 1., std)
    Xbar = (X - mu) / std_filled
    return Xbar, mu, std
def eig(S):
    eigen_values, eigen_vectors = np.linalg.eig(S)
    idx_sorted = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[idx_sorted]
    eigen_vectors = eigen_vectors[:, idx_sorted]
    return eigen_values, eigen_vectors
def projection_matrix(B):
    return B @ np.linalg.inv(B.T @ B) @ B.T
def PCA(X, num_components):
    X_normalized, mean, std = normalize(X)
    covariance_matrix = np.cov(X_normalized, rowvar=False, bias=True)
    eigen_values, eigen_vectors = eig(covariance_matrix)
    projection_matrix_ = projection_matrix(eigen_vectors[:, :num_components])
    X_reconstructed = (projection_matrix_ @ X_normalized.T).T
    return X_reconstructed
def mse(predict, actual):
    return np.square(predict - actual).sum(axis=1).mean()
NUM_DATAPOINTS = 1000
X = (images.reshape(-1, 28 * 28)[:NUM_DATAPOINTS]) / 255.
X_normalized, mu, std = normalize(X)
loss = []
for num_component in range(1, 100):
    X_reconstructed = PCA(X_normalized, num_component)
    error = mse(X_reconstructed, X_normalized)
    loss.append((num_component, error))
loss = np.asarray(loss)
plt.plot(loss[:, 0], loss[:, 1])
plt.axhline(100, linestyle='--', color='r', linewidth=2)
plt.xlabel('num_components')
plt.ylabel('MSE')
plt.title('MSE vs number of principal components')
plt.xticks(np.arange(1, 100, 5))
plt.show()
def PCA_high_dim(X, n_components):
    N, D = X.shape
    M = (X @ X.T) / N
    eigen_values, eigen_vectors = eig(M)
    U = (X.T @ eigen_vectors)[:, :n_components]
    P = projection_matrix(U)
    X_reconstructed = (P @ X.T).T
    return X_reconstructed
np.testing.assert_almost_equal(PCA(X_normalized, 2), PCA_high_dim(X_normalized, 2))
def time(f, repeat=10):
    times = []
    for _ in range(repeat):
        start = timeit.default_timer()
        f()
        stop = timeit.default_timer()
        times.append(stop - start)
    return np.mean(times), np.std(times)
times_mm0 = []
times_mm1 = []
for datasetsize in np.arange(4, 784, step=100):
    XX = X_normalized[:datasetsize]
    mu, sigma = time(lambda: XX.T @ XX)
    times_mm0.append((datasetsize, mu, sigma))
    mu, sigma = time(lambda: XX @ XX.T)
    times_mm1.append((datasetsize, mu, sigma))
times_mm0 = np.asarray(times_mm0)
times_mm1 = np.asarray(times_mm1)
plt.errorbar(times_mm0[:, 0], times_mm0[:, 1], times_mm0[:, 2], label='$X^T X$ (PCA)', linewidth=2)
plt.errorbar(times_mm1[:, 0], times_mm1[:, 1], times_mm1[:, 2], label='$X X^T$ (PCA_high_dim)', linewidth=2)
plt.xlabel('size of dataset')
plt.ylabel('running time')
plt.legend()
plt.show()
times0 = []
times1 = []
for datasetsize in np.arange(4, 784, step=100):
    XX = X_normalized[:datasetsize]
    mu, sigma = time(lambda: PCA(XX, 2), repeat=10)
    times0.append((datasetsize, mu, sigma))
    mu, sigma = time(lambda: PCA_high_dim(XX, 2), repeat=10)
    times1.append((datasetsize, mu, sigma))
times0 = np.asarray(times0)
times1 = np.asarray(times1)
plt.errorbar(times0[:, 0], times0[:, 1], times0[:, 2], label='PCA', linewidth=2)
plt.errorbar(times1[:, 0], times1[:, 1], times1[:, 2], label='PCA_high_dim', linewidth=2)
plt.xlabel('number of datapoints')
plt.ylabel('run time')
plt.legend()
plt.show()
print("Time taken for PCA:", time(lambda: PCA(X_normalized, 2)))
print("Time taken for PCA_high_dim:", time(lambda: PCA_high_dim(X_normalized, 2)))