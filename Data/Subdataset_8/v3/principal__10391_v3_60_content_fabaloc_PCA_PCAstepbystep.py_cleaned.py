import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
excel_path = '~/yourdata'
data = pd.read_excel(excel_path, sheet_name='sheet')
data_frame = pd.DataFrame(data)
mean_vector = data_frame.mean()
standardized_data = data_frame - mean_vector
covariance_matrix = np.cov(standardized_data, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
total_variance = np.sum(sorted_eigenvalues)
explained_variance = (sorted_eigenvalues / total_variance) * 100
num_principal_components = len(sorted_eigenvalues)
pc_labels = [f'PC{i}' for i in range(1, num_principal_components + 1)]
plt.scatter(explained_variance, pc_labels, alpha=0.5)
plt.title('Explained Variance')
plt.xlabel('Explained Variance (%)')
plt.ylabel('Principal Components')
plt.show()
num_components_to_retain = 3
loadings = sorted_eigenvectors[:, :num_components_to_retain]
scores = standardized_data.dot(loadings)
reconstructed_data = scores.dot(loadings.T) + mean_vector.values
residuals = data_frame - reconstructed_data