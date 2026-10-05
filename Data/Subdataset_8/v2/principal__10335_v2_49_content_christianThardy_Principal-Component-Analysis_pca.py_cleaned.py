import numpy as np
import timeit
import matplotlib.pyplot as plt
from load_data import load_mnist
MNIST = load_mnist()
images, labels = MNIST['data'], MNIST['target']
def normalize(X):
    mu = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    std_filled = std.copy()
    std_filled[std == 0] = 1.
    X_normalized = (X - mu) / std_filled
    return X_normalized, mu, std
def PCA(X, num_components):
    X_normalized, mean, std = normalize(X)
    covariance_matrix = np.cov(X_normalized, rowvar=False, bias=True)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    projection_matrix = sorted_eigenvectors[:, :num_components]
    X_reconstructed = np.dot(projection_matrix.T, X_normalized.T).T
    return X_reconstructed
def compute_mse(predict, actual):
    return np.square(predict - actual).sum(axis=1).mean()
def measure_time(f, repeat=10):
    times = []
    for _ in range(repeat):
        start_time = timeit.default_timer()
        f()
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    mean_time = np.mean(times)
    std_time = np.std(times)
    return mean_time, std_time
def PCA_high_dim(X, n_components):
    N, D = X.shape
    covariance_matrix = (X @ X.T) / N
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    U = sorted_eigenvectors[:, :n_components]
    projection_matrix = U @ np.linalg.inv(U.T @ U) @ U.T
    X_reconstructed = projection_matrix @ X.T
    return X_reconstructed.T
NUM_DATAPOINTS = 1000
X = (images.reshape(-1, 28 * 28)[:NUM_DATAPOINTS]) / 255.
X_normalized, mean, std = normalize(X)
np.testing.assert_almost_equal(PCA(X_normalized, 2), PCA_high_dim(X_normalized, 2))
mse_values = []
for num_component in range(1, 100):
    reconstructed_data = PCA(X_normalized, num_component)
    mse_value = compute_mse(reconstructed_data, X_normalized)
    mse_values.append((num_component, mse_value))
mse_values = np.asarray(mse_values)
plt.plot(mse_values[:, 0], mse_values[:, 1])
plt.axhline(100, linestyle='--', color='r', linewidth=2)
plt.xlabel('Number of Components')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs Number of Principal Components')
plt.show()
time_data = {'Size of Dataset': [], 'Mean Time': [], 'Std Time': []}
for datasetsize in np.arange(4, 784, step=50):
    X_subset = X_normalized[:datasetsize]
    mean_time, std_time = measure_time(lambda: X_subset.T @ X_subset)
    time_data['Size of Dataset'].append(datasetsize)
    time_data['Mean Time'].append(mean_time)
    time_data['Std Time'].append(std_time)
time_df = pd.DataFrame(time_data)
plt.errorbar(time_df['Size of Dataset'], time_df['Mean Time'], time_df['Std Time'], linewidth=2)
plt.xlabel('Size of Dataset')
plt.ylabel('Running Time')
plt.title('Running Time vs Size of Dataset')
plt.show()
time_data_pca = {'Number of Datapoints': [], 'Mean Time (PCA)': [], 'Std Time (PCA)': [],
                 'Mean Time (PCA_high_dim)': [], 'Std Time (PCA_high_dim)': []}
for datasetsize in np.arange(4, 784, step=100):
    X_subset = X_normalized[:datasetsize]
    mean_time_pca, std_time_pca = measure_time(lambda: PCA(X_subset, 2), repeat=10)
    mean_time_high_dim, std_time_high_dim = measure_time(lambda: PCA_high_dim(X_subset, 2), repeat=10)
    time_data_pca['Number of Datapoints'].append(datasetsize)
    time_data_pca['Mean Time (PCA)'].append(mean_time_pca)
    time_data_pca['Std Time (PCA)'].append(std_time_pca)
    time_data_pca['Mean Time (PCA_high_dim)'].append(mean_time_high_dim)
    time_data_pca['Std Time (PCA_high_dim)'].append(std_time_high_dim)
time_df_pca = pd.DataFrame(time_data_pca)
plt.errorbar(time_df_pca['Number of Datapoints'], time_df_pca['Mean Time (PCA)'], time_df_pca['Std Time (PCA)'], label='PCA', linewidth=2)
plt.errorbar(time_df_pca['Number of Datapoints'], time_df_pca['Mean Time (PCA_high_dim)'], time_df_pca['Std Time (PCA_high_dim)'], label='PCA_high_dim', linewidth=2)
plt.xlabel('Number of Datapoints')
plt.ylabel('Run Time')
plt.title('Run Time vs Number of Datapoints')
plt.legend()
plt.show()
mean_time_pca, std_time_pca = measure_time(lambda: PCA(X_normalized, 2))
mean_time_high_dim, std_time_high_dim = measure_time(lambda: PCA_high_dim(X_normalized, 2))
print("Time taken for PCA:", mean_time_pca, "+/-", std_time_pca)
print("Time taken for PCA_high_dim:", mean_time_high_dim, "+/-", std_time_high_dim)