import numpy as np
class PCA:
    def __init__(self, num_components=None):
        self.num_components = num_components
    def fit(self, data):
        if self.num_components is None or self.num_components > data.shape[0]:
            self.num_components = data.shape[0]
        self.data_mean = np.mean(data, axis=0)
        centered_data = data - self.data_mean
        covariance_matrix = np.cov(centered_data, rowvar=False)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        sorted_indices = np.argsort(eigenvalues)[::-1]
        self.eigenvalues = np.real(eigenvalues[sorted_indices])
        self.eigenvectors = np.real(eigenvectors[:, sorted_indices])
        total_variance = np.sum(self.eigenvalues)
        self.pve_list = np.cumsum(self.eigenvalues) / total_variance
    def transform(self, data):
        centered_data = data - self.data_mean
        projected_data = np.dot(centered_data, self.eigenvectors[:, :self.num_components])
        return projected_data
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(10, 5)
    pca = PCA(num_components=2)
    pca.fit(data)
    transformed_data = pca.transform(data)
    print("Original data shape:", data.shape)
    print("Transformed data shape:", transformed_data.shape)