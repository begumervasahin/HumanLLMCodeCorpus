import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors
def euclid(X, Y):
    return euclidean_distances(X, Y)
def gaussian_kernel(X, sigma):
    return np.exp(-np.square(X) / (2 * np.square(sigma)))
def mnn(X, m):
    _, indices = NearestNeighbors(n_neighbors=m, metric='euclidean').fit(X).kneighbors(X)
    nn = np.zeros(X.shape)
    np.put_along_axis(nn, indices, 1, axis=1)
    nn += nn.T
    nn[nn == 2] = 1
    return nn
def spectral(X, k, similarity_param, similarity=gaussian_kernel):
    S = euclid(X, X)
    W = similarity(S, similarity_param)
    D = np.diag(np.sum(W, axis=1))
    inverse_D_root = np.diag(np.power(D.diagonal(), -0.5))
    L = np.identity(X.shape[0]) - inverse_D_root.dot(W).dot(inverse_D_root)
    eigval, eigvec = np.linalg.eig(L)
    idx = np.argpartition(eigval, k)
    lowest_k = eigvec[:, idx[:k]]
    return kmeans.kmeans(lowest_k, k)[0]
