import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mean = [5, 5]
cov = [[1, 0], [100, 100]]
data = pd.DataFrame(np.random.multivariate_normal(mean, cov, 100), columns=['x', 'y'])
plt.scatter(data['x'], data['y'], color='b', label='Original Data')
def subtract_mean(matrix):
    return matrix - matrix.mean()
def calculate_covariance(matrix):
    return matrix.cov()
def get_principal_components(eig_vals, eig_vecs, num_components):
    sorted_indices = np.argsort(-eig_vals)[:num_components]
    return eig_vecs[:, sorted_indices]
mean_adjusted_data = subtract_mean(data)
cov_matrix = calculate_covariance(mean_adjusted_data)
eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
principal_components = get_principal_components(eig_vals, eig_vecs, 2)
projected_data = mean_adjusted_data.dot(principal_components)
print(projected_data)
plt.scatter(projected_data.iloc[:, 0], projected_data.iloc[:, 1], color='r', marker='x', label='Transformed Data')
plt.legend()
plt.show()