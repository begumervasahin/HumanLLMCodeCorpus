import numpy as np
from numpy import linalg as LA
def compute_Z(X, centering=True, scaling=True):
    Z = X.astype(float)
    rows, cols = Z.shape
    if centering:
        means = X.mean(axis=0)
        Z -= means
    if scaling:
        std = np.std(Z, axis=0)
        Z /= std
    return Z
def compute_covariance_matrix(Z):
    return Z.T @ Z
def find_pcs(COV):
    eigenValues, eigenVectors = LA.eig(COV)
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    return eigenValues, eigenVectors
def project_data(Z, PCS, L, k=0, var=0):
    if k != 0:
        component_matrix = PCS[:, :k]
    else:
        total_variance = np.sum(L)
        cumulative_variance = 0
        num_components = 0
        for eigenvalue in L:
            cumulative_variance += eigenvalue
            num_components += 1
            if cumulative_variance / total_variance >= var:
                break
        component_matrix = PCS[:, :num_components]
    Z_star = Z @ component_matrix
    return Z_star
if __name__ == "__main__":
    X = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
    ])
    Z = compute_Z(X, centering=True, scaling=True)
    COV = compute_covariance_matrix(Z)
    eigenValues, eigenVectors = find_pcs(COV)
    Z_star = project_data(Z, eigenVectors, eigenValues, k=1)
    print("Projected data:\n", Z_star)