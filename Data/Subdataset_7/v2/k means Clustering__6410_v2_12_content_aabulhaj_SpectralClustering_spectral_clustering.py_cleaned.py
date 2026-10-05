import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors
def fonk1(X, Y):
    return euclidean_distances(X, Y)
def fonk2(b5, sigma):
    return np.exp(-np.square(b5) / (2 * np.square(sigma)))
def fonk3(b5, m):
    _, b1 = NearestNeighbors(n_neighbors=m, metric='euclidean').fit(b5).kneighbors(b5)
    b2 = np.zeros(b5.shape)
    np.put_along_axis(b2, b1, 1, b3 = 1)
    b2 += b2.T
    b2[b2 = = 2] = 1
    return b2
def fonk4(data_matrix, num_clusters, similarity_param, b4 = gaussian_kernel_similarity):
    b5 = fonk1(data_matrix, data_matrix)
    b6 = b4(b5, similarity_param)
    b7 = np.sum(b6, b3=1)
    b8 = np.diag(b7)
    b9 = np.diag(1 / np.sqrt(b7))
    b10 = np.identity(data_matrix.shape[0]) - b9.dot(b6).dot(b9)
    eigenvalues, b11 = np.linalg.eigh(b10)
    b12 = np.argsort(eigenvalues)
    b13 = b11[:, b12[0:num_clusters]]
    return b13
