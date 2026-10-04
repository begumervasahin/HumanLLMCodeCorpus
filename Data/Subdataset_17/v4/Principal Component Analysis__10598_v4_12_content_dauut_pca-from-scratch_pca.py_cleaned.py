import numpy as np
from numpy.linalg import eig
def compute_Z(X, centering=True, scaling=True):
    Z = X.astype(float)
    rows, cols = Z.shape
    if centering:
        means = X.mean(axis=0)
        Z -= means
    if scaling:
        std_devs = np.std(Z, axis=0)
        Z /= std_devs
    return Z
def compute_covariance_matrix(Z):
    return Z.T.dot(Z) / (Z.shape[0] - 1)
def find_pcs(COV):
    eigenvalues, eigenvectors = eig(COV)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    return eigenvalues, eigenvectors
def project_data(Z, PCS, L, k=0, var=0.0):
    if k != 0:
        component_matrix = PCS[:, :k]
    else:
        total_variance = 0
        eigen_val_index = 0
        while total_variance < var and eigen_val_index < len(L):
            total_variance += L[eigen_val_index] / np.sum(L)
            eigen_val_index += 1
        component_matrix = PCS[:, :eigen_val_index]
    Z_star = Z.dot(component_matrix)
    return Z_star