import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = '~/yourdata'
data = pd.read_excel(path, sheet_name='sheet')
mean_vector = np.mean(data, axis=0)
variance_vector = np.var(data, axis=0)
num_rows, num_cols = data.shape
data_standardized = data - mean_vector
covariance_matrix = np.dot(data_standardized.T, data_standardized) / (num_rows - 1)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
for eigvec in eigenvectors:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(eigvec))
    print('Eigenvectors are unit vectors.')
index_sorted = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[index_sorted]
eigenvectors = eigenvectors[:, index_sorted]
total_variance = sum(eigenvalues)
explained_variance = [eigval / total_variance * 100 for eigval in eigenvalues]
cumulative_explained_variance = np.cumsum(explained_variance)
principal_components = ['PC%s' % i for i in range(1, len(eigenvalues) + 1)]
plt.scatter(explained_variance, principal_components, alpha=0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
num_components = 3
loadings = eigenvectors[:, :num_components]
scores = np.dot(data_standardized, loadings)
data_estimate = np.dot(scores, loadings.T)
data_original = data_estimate + mean_vector.values
residuals = data - data_original