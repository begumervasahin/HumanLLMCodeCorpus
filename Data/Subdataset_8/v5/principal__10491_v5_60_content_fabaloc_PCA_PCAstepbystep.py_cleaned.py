import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_path = '~/yourdata'
sheet_name = 'sheet'
data = pd.read_excel(data_path, sheet_name=sheet_name)
mean_vector = np.mean(data, axis=0)
variance_vector = np.var(data, axis=0)
data_standardized = data - mean_vector
num_rows, _ = data.shape
covariance_matrix = np.dot(data_standardized.T, data_standardized) / (num_rows - 1)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
for eigvec in eigenvectors:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(eigvec))
print('Eigenvectors are unit vectors.')
sorted_indices = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]
total_variance = sum(eigenvalues)
explained_variance = [(eigval / total_variance) * 100 for eigval in eigenvalues]
cumulative_explained_variance = np.cumsum(explained_variance)
num_components = len(eigenvalues)
principal_components = ['PC%s' % (i + 1) for i in range(num_components)]
plt.scatter(explained_variance, principal_components, alpha=0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
selected_components = 3
loadings = eigenvectors[:, :selected_components]
scores = np.dot(data_standardized, loadings)
data_estimate = np.dot(scores, loadings.T)
data_original = data_estimate + mean_vector.values
residuals = data - data_original