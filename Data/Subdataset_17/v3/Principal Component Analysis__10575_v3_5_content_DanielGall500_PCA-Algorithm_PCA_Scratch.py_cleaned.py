import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mean = [5, 5]
cov = [[1, 0], [0, 100]]
data = pd.DataFrame(np.random.multivariate_normal(mean, cov, 100), columns=['Feature 1', 'Feature 2'])
plt.scatter(data['Feature 1'], data['Feature 2'], color='b', label='Original Data')
def subtract_mean(matrix):
    return matrix.apply(lambda col: col - col.mean())
def calculate_covariance(matrix):
    return np.cov(matrix.T, bias=False)
def get_principal_components(eig_vals, eig_vecs, num_components):
    sorted_indices = np.argsort(eig_vals)[::-1]
    return eig_vecs[:, sorted_indices[:num_components]]
mean_adjusted_data = subtract_mean(data)
covariance_matrix = calculate_covariance(mean_adjusted_data)
eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
principal_components = get_principal_components(eig_vals, eig_vecs, 2)
transformed_data = np.dot(principal_components.T, mean_adjusted_data.T).T
plt.scatter(transformed_data[:, 0], transformed_data[:, 1], color='r', marker='x', label='PCA Transformed Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Transformation')
plt.legend()
plt.show()
print(transformed_data)