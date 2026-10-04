import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
def plot_data_set(X, title="PCA Data"):
    plt.clf()
    plt.title(title)
    plt.scatter(X[:, 0], X[:, 1], c="b", marker='o')
    plt.xlabel('Fahrenheit')
    plt.ylabel('Celsius')
    plt.xlim(X.min(axis=0)[0], X.max(axis=0)[0])
    plt.ylim(X.min(axis=0)[1], X.max(axis=0)[1])
    plt.show()
def create_pca_set(size, variance=1.0):
    x = np.linspace(0, 50, num=size)
    data = np.c_[x, x]
    v = (np.random.rand(size) - 0.5) * variance
    offsets = np.c_[-v, 44.8 * v + 5]
    data += offsets
    return data
def create_fahrenheit_celsius_set(size, variance=1.0):
    v = (np.random.rand(size) - 0.5) * variance
    x0 = np.linspace(0, 100, num=size) + v
    v = (np.random.rand(size) - 0.5) * variance
    x1 = (x0 - 32.0) * 5.0 / 9.0 + v
    data = np.c_[x0, x1]
    return data
data = create_fahrenheit_celsius_set(100, 4.0)
plot_data_set(data, title="Original Data")
data_normalized = scale(data)
pca = PCA()
data_reduced = pca.fit_transform(data_normalized)
print(f"Number of principal components: {pca.n_components_}")
print(f"Components variance: {pca.explained_variance_}")
print(f"Components variance ratio: {pca.explained_variance_ratio_}")
print(f"Principal components: {pca.components_}")
data_manually_reconstructed = np.dot(data_reduced[:, 0].reshape((100, 1)), pca.components_[0].reshape((1, 2)))
plot_data_set(data_manually_reconstructed, title="Manually Reconstructed Data")
pca = PCA(1)
data_reduced = pca.fit_transform(data_normalized)
data_reconstructed = pca.inverse_transform(data_reduced)
plot_data_set(data_reconstructed, title="PCA Reconstructed Data")
mean_squared_error = np.mean(np.linalg.norm(data_normalized - data_reconstructed, axis=1))
print(f"Mean squared reconstruction error: {mean_squared_error}")