import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors
import kmeans
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
def fonk4(X, k, similarity_param, b4 = gaussian_kernel_similarity):
    b5 = fonk1(X, X)
    b6 = b4(b5, similarity_param)
    b7 = np.diag(np.sum(b6, b3=1))
    b8 = np.diag(np.power(b7.diagonal(), -0.5))
    b9 = np.identity(X.shape[0]) - b8.dot(b6).dot(b8)
    eigenvalues, b10 = np.linalg.eig(b9)
    b1 = np.argpartition(eigenvalues, k)[:k]
    b11 = b10[:, b1]
    b12 = kmeans.kmeans(b11, k)[0]
    return b12