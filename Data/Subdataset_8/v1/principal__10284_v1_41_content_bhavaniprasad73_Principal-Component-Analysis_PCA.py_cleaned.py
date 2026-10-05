import numpy as np
import pandas as pd
from numpy.linalg import norm, eig
from scipy.stats import zscore
csv = pd.read_csv('C:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
data = csv.iloc[:, :-1]
mean = data.mean(axis=1)
variance = data.var(axis=1)
std_dev = np.sqrt(variance)
z_normalized = (data.sub(mean, axis=0)).div(std_dev, axis=0)
cov_matrix = np.cov(z_normalized, bias=True, rowvar=False)
eigen_values, eigen_vectors = eig(cov_matrix)
sorted_indices = np.argsort(eigen_values)[::-1]
eigen_values = eigen_values[sorted_indices]
eigen_vectors = eigen_vectors[:, sorted_indices]
reduced_data = z_normalized.dot(eigen_vectors[:, :2])
covariance_projected = np.cov(reduced_data, bias=True, rowvar=False)
trace_covariance = np.trace(covariance_projected)
sum_principal_eigenvalues = np.sum(eigen_values[:2])
print("Covariance Matrix of the Projected Data Points:\n", covariance_projected)
print("Trace of Covariance Matrix:", trace_covariance)
print("Sum of Eigenvalues Corresponding to Principal Vectors:", sum_principal_eigenvalues)