import numpy.linalg as LA
from scipy import stats
import pandas as pd
import numpy as np
csv = pd.read_csv('C:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
print("Data structure:", type(csv))
print("Data with labels:")
print(csv.head(3))
new_csv = csv[csv.columns[:-1]]
print("Data without class labels:")
print(new_csv.head(3))
transp = new_csv.T
print("Transposed data:")
print(transp)
transp["sum"] = transp.sum(axis=1)
print("Sum of each row:")
print(transp["sum"])
n = len(new_csv.columns)
mean = transp["sum"] / n
print("Mean:", mean)
z_score = (new_csv - mean) / new_csv.std()
cov_mat = np.cov(z_score, bias=True, rowvar=False)
eigen_values, eigen_vectors = LA.eig(cov_mat)
sorted_indices = eigen_values.argsort()[::-1]
sorted_eigen_values = eigen_values[sorted_indices]
sorted_eigen_vectors = eigen_vectors[:, sorted_indices]
dominant_eigenvectors = sorted_eigen_vectors[:, :2]
projected_data = z_score.dot(dominant_eigenvectors)
def PCA(data, threshold):
    sigma = np.cov(data, bias=True, rowvar=False)
    eigenvalues, eigenvectors = LA.eig(sigma)
    sorted_indices = eigenvalues.argsort()[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    total_variance = eigenvalues.sum()
    cumulative_percentage = np.cumsum((sorted_eigenvalues / total_variance) * 100)
    num_eigenvectors = np.argmax(cumulative_percentage >= threshold) + 1
    principal_eigenvectors = sorted_eigenvectors[:, :num_eigenvectors]
    reduced_data = data.dot(principal_eigenvectors)
    return reduced_data, sorted_eigenvalues, num_eigenvectors
reduced_data, eigenvalues, num_eigenvectors = PCA(new_csv, 95)
covariance_projected = np.cov(reduced_data, bias=True, rowvar=False)
trace_covariance_projected = np.trace(covariance_projected)
sum_principal_eigenvalues = eigenvalues[:num_eigenvectors].sum()
print("Covariance of the projected data points:", trace_covariance_projected)
print("Sum of the eigenvalues corresponding to the principal vectors:", sum_principal_eigenvalues)