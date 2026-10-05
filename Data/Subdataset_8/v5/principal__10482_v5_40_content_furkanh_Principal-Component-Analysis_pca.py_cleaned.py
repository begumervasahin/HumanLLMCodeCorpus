import numpy as np
class PCA:
    def __init__(self, n_components=None):
        self.n_components = n_components
    def fit(self, X):
        if self.n_components is None or self.n_components > X.shape[0]:
            self.n_components = X.shape[0]
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        covariance_matrix = np.matmul(X_centered.T, X_centered) / (X.shape[0] - 1)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        sorted_indices = eigenvalues.argsort()[::-1]
        eigenvectors = eigenvectors[:, sorted_indices]
        eigenvalues = eigenvalues[sorted_indices][::-1]
        self.eigenvalues = np.real(eigenvalues)
        self.eigenvectors = np.real(eigenvectors)
        total_variance = np.sum(self.eigenvalues)
        cumulative_variance = 0
        self.explained_variance_ratio = []
        for i in range(self.eigenvalues.shape[0]):
            cumulative_variance += self.eigenvalues[i]
            self.explained_variance_ratio.append(cumulative_variance / total_variance)
    def transform(self, X):
        X_centered = X - self.mean
        transformed_data = np.matmul(X_centered, self.eigenvectors)[:, :self.n_components]
        return transformed_data