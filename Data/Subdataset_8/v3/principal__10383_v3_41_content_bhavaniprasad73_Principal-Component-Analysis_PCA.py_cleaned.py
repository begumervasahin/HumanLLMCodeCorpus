import numpy as np
import pandas as pd
from numpy.linalg import eig
from scipy.stats import zscore
file_path = 'C:/Users/ebhavaniprasad/Desktop/magic04.txt'
data = pd.read_csv(file_path, header=None)
features = data.iloc[:, :-1]
z_normalized_features = zscore(features, axis=0)
covariance_matrix = np.cov(z_normalized_features, bias=True, rowvar=False)
eigen_values, eigen_vectors = eig(covariance_matrix)
sorted_indices = np.argsort(eigen_values)[::-1]
sorted_eigen_values = eigen_values[sorted_indices]
sorted_eigen_vectors = eigen_vectors[:, sorted_indices]
reduced_data = z_normalized_features.dot(sorted_eigen_vectors[:, :2])
covariance_projected_data = np.cov(reduced_data, bias=True, rowvar=False)
trace_of_covariance = np.trace(covariance_projected_data)
sum_of_principal_eigenvalues = np.sum(sorted_eigen_values[:2])
print("Covariance Matrix of the Projected Data Points:\n", covariance_projected_data)
print("Trace of Covariance Matrix:", trace_of_covariance)
print("Sum of Eigenvalues Corresponding to the First Two Principal Vectors:", sum_of_principal_eigenvalues)