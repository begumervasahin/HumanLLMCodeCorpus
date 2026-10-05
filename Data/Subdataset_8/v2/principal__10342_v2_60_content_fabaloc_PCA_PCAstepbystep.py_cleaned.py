
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path_to_data = '~/yourdata'
data = pd.read_excel(path_to_data, sheet_name='sheet')
data_frame = pd.DataFrame(data)
mean_vector = np.mean(data_frame, axis=0)
variance_vector = np.var(data_frame, axis=0)
num_rows, num_columns = data_frame.shape
standardized_data = data_frame - mean_vector
covariance_matrix = (standardized_data.T.dot(standardized_data)) / (num_rows - 1)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
for vector in eigenvectors:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(vector))
    print('Eigenvectors are unit vectors.')
sorted_indices = eigenvalues.argsort()[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
total_variance = sum(sorted_eigenvalues)
explained_variance = [(value / total_variance) * 100 for value in sorted_eigenvalues]
cumulative_explained_variance = np.cumsum(explained_variance)
principal_component_labels = ['PC%s' % index for index in range(1, len(sorted_eigenvalues) + 1)]
plt.scatter(explained_variance, principal_component_labels, alpha=0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
num_components_to_retain = 3
loadings = sorted_eigenvectors[:, :num_components_to_retain]
scores = standardized_data.dot(loadings)
reconstructed_data = scores.dot(loadings.T)
reconstructed_data += mean_vector.values
residuals = data_frame - reconstructed_data