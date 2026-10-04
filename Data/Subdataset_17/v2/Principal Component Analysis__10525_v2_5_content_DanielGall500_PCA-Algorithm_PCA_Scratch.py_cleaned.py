import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mean = [5, 5]
cov = [[1, 0], [0, 100]]
data = pd.DataFrame(np.random.multivariate_normal(mean, cov, 100))
plt.scatter(data[0], data[1], color='b', label='Original Data')
def subtract_mean(matrix):
    for col in matrix.columns:
        mean = np.mean(matrix[col])
        matrix[col] = matrix[col].apply(lambda x: x - mean)
    return matrix
def calculate_covariance(matrix):
    cols = matrix.columns
    cov_matrix = np.zeros((len(cols), len(cols)))
    for i, col1 in enumerate(cols):
        for j, col2 in enumerate(cols):
            cov_matrix[i, j] = np.mean(matrix[col1] * matrix[col2])
    return cov_matrix
def get_principal_components(eig_vals, eig_vecs, num_components):
    sorted_indices = np.argsort(-eig_vals)
    principal_components = eig_vecs[:, sorted_indices[:num_components]]
    return principal_components
mean_adjusted_data = subtract_mean(data.copy())
covariance_matrix = calculate_covariance(mean_adjusted_data)
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
principal_components = get_principal_components(eig_vals, eig_vecs, 2)
transformed_data = np.dot(principal_components.T, mean_adjusted_data.T)
plt.scatter(transformed_data[0], transformed_data[1], color='r', marker='x', label='PCA Transformed Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('PCA Transformation')
plt.legend()
plt.show()
print(transformed_data.T)