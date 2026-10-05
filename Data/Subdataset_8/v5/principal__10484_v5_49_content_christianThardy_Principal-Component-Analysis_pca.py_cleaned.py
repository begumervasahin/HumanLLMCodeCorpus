import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as SKPCA
from load_data import load_mnist
import timeit
MNIST = load_mnist()
images, labels = MNIST['data'], MNIST['target']
plt.figure(figsize=(4, 4))
plt.imshow(images[0].reshape(28, 28), cmap='gray')
plt.show()
def normalize(X):
    mu = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std_filled = np.where(std == 0, 1., std)
    X_normalized = (X - mu) / std_filled
    return X_normalized, mu, std
def compute_eigen(S):
    eigen_values, eigen_vectors = np.linalg.eig(S)
    sorted_indices = np.argsort(eigen_values)[::-1]
    eigen_values = eigen_values[sorted_indices]
    eigen_vectors = eigen_vectors[:, sorted_indices]
    return eigen_values, eigen_vectors
def projection_matrix(B):
    return B @ np.linalg.inv(B.T @ B) @ B.T
def PCA(X, num_components):
    X_normalized, mean, std = normalize(X)
    covariance_matrix = np.cov(X_normalized, rowvar=False, bias=True)
    eigen_values, eigen_vectors = compute_eigen(covariance_matrix)
    projection_matrix_ = projection_matrix(eigen_vectors[:, :num_components])
    X_reconstructed = (projection_matrix_ @ X_normalized.T).T
    return X_reconstructed
def mean_squared_error(predict, actual):
    return np.square(predict - actual).sum(axis=1).mean()
NUM_DATAPOINTS = 1000
X = (images.reshape(-1, 28 * 28)[:NUM_DATAPOINTS]) / 255.
X_normalized, mu, std = normalize(X)
loss = []
for num_component in range(1, 100):
    X_reconstructed = PCA(X_normalized, num_component)
    error = mean_squared_error(X_reconstructed, X_normalized)
    loss.append((num_component, error))
loss = np.asarray(loss)
plt.plot(loss[:, 0], loss[:, 1])
plt.axhline(100, linestyle='--', color='r', linewidth=2)
plt.xlabel('Number of Components')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs Number of Principal Components')
plt.xticks(np.arange(1, 100, 5))
plt.show()
def PCA_high_dim(X, n_components):
    N, D = X.shape
    M = (X @ X.T) / N
    eigen_values, eigen_vectors = compute_eigen(M)
    U = (X.T @ eigen_vectors)[:, :n_components]
    P = projection_matrix(U)
    X_reconstructed = (P @ X.T).T
    return X_reconstructed
np.testing.assert_almost_equal(PCA(X_normalized, 2), PCA_high_dim(X_normalized, 2))
def timing(f, repeat=10):
    times = []
    for _ in range(repeat):
        start = timeit.default_timer()
        f()
        stop = timeit.default_timer()
        times.append(stop - start)
    return np.mean(times), np.std(times)
sizes = np.arange(4, 784, step=100)
times_mm0 = []
times_mm1 = []
for dataset_size in sizes:
    XX = X_normalized[:dataset_size]
    mu, sigma = timing(lambda: XX.T @ XX)
    times_mm0.append((dataset_size, mu, sigma))
    mu, sigma = timing(lambda: XX @ XX.T)
    times_mm1.append((dataset_size, mu, sigma))
times_mm0 = np.asarray(times_mm0)
times_mm1 = np.asarray(times_mm1)
plt.errorbar(times_mm0[:, 0], times_mm0[:, 1], times_mm0[:, 2], label='$X^T X$ (PCA)', linewidth=2)
plt.errorbar(times_mm1[:, 0], times_mm1[:, 1], times_mm1[:, 2], label='$X X^T$ (PCA_high_dim)', linewidth=2)
plt.xlabel('Size of Dataset')
plt.ylabel('Running Time')
plt.legend()
plt.show()
times0 = []
times1 = []
for dataset_size in sizes:
    XX = X_normalized[:dataset_size]
    mu, sigma = timing(lambda: PCA(XX, 2), repeat=10)
    times0.append((dataset_size, mu, sigma))
    mu, sigma = timing(lambda: PCA_high_dim(XX, 2), repeat=10)
    times1.append((dataset_size, mu, sigma))
times0 = np.asarray(times0)
times1 = np.asarray(times1)
plt.errorbar(times0[:, 0], times0[:, 1], times0[:, 2], label='PCA', linewidth=2)
plt.errorbar(times1[:, 0], times1[:, 1], times1[:, 2], label='PCA_high_dim', linewidth=2)
plt.xlabel('Number of Datapoints')
plt.ylabel('Run Time')
plt.legend()
plt.show()
print("Time taken for PCA:", timing(lambda: PCA(X_normalized, 2)))
print("Time taken for PCA_high_dim:", timing(lambda: PCA_high_dim(X_normalized, 2)))