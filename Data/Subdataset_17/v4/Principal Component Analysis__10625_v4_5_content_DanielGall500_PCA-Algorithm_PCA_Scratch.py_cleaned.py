import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mean = [5, 5]
cov = [[1, 0], [100, 100]]
data = pd.DataFrame(np.random.multivariate_normal(mean, cov, 100))
plt.scatter(data[0], data[1], color='b', label='Original Data')
def subtract_mean(matrix):
    for col in matrix.columns:
        mean = np.mean(matrix[col])
        matrix[col] = matrix[col].apply(lambda x: x - mean)
    return matrix
def calculate_covariance(matrix):
    cov_matrix = matrix.cov()
    return cov_matrix
def get_principal_components(eig_vals, eig_vecs, dimensions):
    sorted_indices = np.argsort(-eig_vals)[:dimensions]
    principal_components = eig_vecs[:, sorted_indices]
    return principal_components
mean_adjusted = subtract_mean(data)
cov_matrix = calculate_covariance(mean_adjusted)
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
principal_components = get_principal_components(eig_vals, eig_vecs, 2)
feature_vector = np.dot(principal_components.T, mean_adjusted.T).T
print(feature_vector)
plt.scatter(feature_vector[:, 0], feature_vector[:, 1], color='r', marker='x', label='Transformed Data')
plt.legend()
plt.show()