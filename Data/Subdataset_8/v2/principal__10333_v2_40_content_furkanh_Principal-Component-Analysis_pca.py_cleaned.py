import numpy as np
class PCA:
    def __init__(self, num_components=None):
        self.num_components = num_components
    def fit(self, data):
        if self.num_components is None or self.num_components > data.shape[0]:
            self.num_components = data.shape[0]
        data_mean = np.mean(data, axis=0)
        self.data_mean = data_mean
        centered_data = data - data_mean
        covariance_matrix = np.matmul(centered_data.transpose(), centered_data) / (centered_data.shape[0] - 1)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        eigenvectors = eigenvectors[:, eigenvalues.argsort()[::-1]]
        eigenvalues.sort()
        eigenvalues = eigenvalues[::-1]
        self.eigenvalues = np.real(eigenvalues)
        self.eigenvectors = np.real(eigenvectors)
        self.pve_list = []
        total_variance = np.sum(self.eigenvalues)
        cumulative_variance = 0
        for i in range(self.eigenvalues.shape[0]):
            cumulative_variance += self.eigenvalues[i]
            self.pve_list.append(cumulative_variance / total_variance)
    def transform(self, data):
        centered_data = data - self.data_mean
        projected_data = np.matmul(centered_data, self.eigenvectors)[:, :self.num_components]
        return projected_data
if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(10, 5)
    pca = PCA(num_components=2)
    pca.fit(data)
    transformed_data = pca.transform(data)
    print("Original data shape:", data.shape)
    print("Transformed data shape:", transformed_data.shape)