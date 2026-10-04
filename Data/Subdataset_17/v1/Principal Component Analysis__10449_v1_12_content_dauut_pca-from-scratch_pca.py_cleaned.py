import numpy as np
from numpy import linalg as LA
def compute_Z(X, centering=True, scaling=True):
    Z = X.astype(float)
    rows = Z.shape[0]
    cols = Z.shape[1]
    if centering:
        means = X.mean(0)
        for i in range(rows):
            for j in range(cols):
                Z[i, j] = Z[i, j] - means[j]
    if scaling:
        std = np.std(Z, axis=0)
        for i in range(cols):
            for j in range(rows):
                Z[j][i] = Z[j][i] / std[i]
    return Z
def compute_covariance_matrix(Z):
    return Z.T.dot(Z)
def find_pcs(COV):
    eigenValues, eigenVectors = LA.eig(COV)
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    return eigenValues, eigenVectors
def project_data(Z, PCS, L, k=0, var=0):
    eigen_pairs = [(np.abs(L[i]), PCS[:, i]) for i in range(len(L))]
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)
    component_matrix = np.copy(PCS)
    if k != 0:
        component_matrix = np.delete(component_matrix, range(k, component_matrix.shape[1]), axis=1)
        Z_star = Z.dot(component_matrix)
    else:
        tot_var = 0
        eigen_val_index = 0
        while tot_var < var:
            tot_var = tot_var + L[eigen_val_index] / np.sum(L)
            eigen_val_index = eigen_val_index + 1
        component_count = eigen_val_index
        component_matrix = np.delete(component_matrix, range(component_count, component_matrix.shape[1]), axis=1)
        Z_star = Z.dot(component_matrix)
    return Z_star
if __name__ == "__main__":
    X = np.array([[2.5, 2.4],
                  [0.5, 0.7],
                  [2.2, 2.9],
                  [1.9, 2.2],
                  [3.1, 3.0],
                  [2.3, 2.7],
                  [2.0, 1.6],
                  [1.0, 1.1],
                  [1.5, 1.6],
                  [1.1, 0.9]])
    Z = compute_Z(X, centering=True, scaling=True)
    COV = compute_covariance_matrix(Z)
    eigenValues, eigenVectors = find_pcs(COV)
    Z_star = project_data(Z, eigenVectors, eigenValues, k=1)
    print("Projected data:\n", Z_star)