import numpy as np
def zero_mean(data):
    mean = np.mean(data, axis=0)
    centered_data = data - mean
    return centered_data, mean
def pca(data):
    centered_data, mean = zero_mean(data)
    covariance_matrix = np.cov(centered_data, rowvar=0)
    eigenvalues, eigenvectors = np.linalg.eig(np.mat(covariance_matrix))
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    return sorted_eigenvalues, sorted_eigenvectors
def calculate_variance_percentage(eigenvalues, percentage):
    total_variance = np.sum(eigenvalues)
    cumulative_variance = 0
    num_components = 0
    for eigenvalue in eigenvalues:
        cumulative_variance += eigenvalue
        num_components += 1
        if cumulative_variance >= total_variance * percentage:
            break
    variance_ratios = eigenvalues[:num_components] / total_variance
    return num_components, variance_ratios
def all_variance_percentage(eigenvalues):
    _, variance_ratios = calculate_variance_percentage(eigenvalues, 1)
    return variance_ratios
def components_over_threshold(eigenvalues, threshold=0.1):
    _, variance_ratios = calculate_variance_percentage(eigenvalues, 1)
    num_components = np.sum(variance_ratios > threshold)
    return num_components, variance_ratios[:num_components]
def project_data(data, eigenvectors, num_components):
    top_eigenvectors = eigenvectors[:, :num_components]
    projected_data = np.dot(data, top_eigenvectors)
    return projected_data
if __name__ == "__main__":
    data_matrix = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
    ])
    eigenvalues, eigenvectors = pca(data_matrix)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
    num_components, variance_ratios = components_over_threshold(eigenvalues)
    print("Number of components with >10% variance:", num_components)
    print("Percentage of variance for these components:", variance_ratios)
    reduced_data = project_data(data_matrix, eigenvectors, num_components)
    print("Reduced data:\n", reduced_data)