import numpy as np
from numpy.linalg import eig
def compute_Z(X, centering=True, scaling=True):
    Z = X.astype(float)
    if centering:
        means = Z.mean(axis=0)
        Z -= means
    if scaling:
        std_devs = Z.std(axis=0, ddof=1)
        Z /= std_devs
    return Z
def compute_covariance_matrix(Z):
    return np.cov(Z, rowvar=False)
def find_pcs(COV):
    eigenvalues, eigenvectors = eig(COV)
    sorted_indices = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    return eigenvalues, eigenvectors
def project_data(Z, PCS, L, k=0, var=0.0):
    if k > 0:
        component_matrix = PCS[:, :k]
    else:
        total_variance = 0
        num_components = 0
        for eigenvalue in L:
            total_variance += eigenvalue / L.sum()
            num_components += 1
            if total_variance >= var:
                break
        component_matrix = PCS[:, :num_components]
    Z_star = Z.dot(component_matrix)
    return Z_star