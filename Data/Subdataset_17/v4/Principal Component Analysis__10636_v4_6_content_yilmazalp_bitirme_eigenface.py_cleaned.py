import numpy as np
def as_row_matrix(X):
    if len(X) == 0:
        return np.array([])
    mat = np.empty((0, X[0].size), dtype=X[0].dtype)
    for row in X:
        mat = np.vstack((mat, np.asarray(row).reshape(1, -1)))
    return mat
def as_column_matrix(X):
    if len(X) == 0:
        return np.array([])
    mat = np.empty((X[0].size, 0), dtype=X[0].dtype)
    for col in X:
        mat = np.hstack((mat, np.asarray(col).reshape(-1, 1)))
    return mat
def pca(X, num_components=0):
    n, d = X.shape
    if num_components <= 0 or num_components > n:
        num_components = n
    mu = X.mean(axis=0)
    X = X - mu
    if n > d:
        C = np.dot(X.T, X)
        eigenvalues, eigenvectors = np.linalg.eigh(C)
    else:
        C = np.dot(X, X.T)
        eigenvalues, eigenvectors = np.linalg.eigh(C)
        eigenvectors = np.dot(X.T, eigenvectors)
    eigenvectors = np.apply_along_axis(lambda v: v / np.linalg.norm(v), 0, eigenvectors)
    idx = np.argsort(-eigenvalues)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    eigenvalues = eigenvalues[:num_components].copy()
    eigenvectors = eigenvectors[:, :num_components].copy()
    return eigenvalues, eigenvectors, mu
def project(W, X, mu=None):
    if mu is None:
        return np.dot(X, W)
    return np.dot(X - mu, W)
def reconstruct(W, Y, mu=None):
    if mu is None:
        return np.dot(Y, W.T)
    return np.dot(Y, W.T) + mu