import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors
import kmeans
def compute_euclidean_distance_matrix(X, Y):
    return euclidean_distances(X, Y)
def compute_gaussian_kernel_similarity(distance_matrix, sigma):
    return np.exp(-np.square(distance_matrix) / (2 * np.square(sigma)))
def compute_m_nearest_neighbors_similarity(distance_matrix, m):
    _, indices = NearestNeighbors(n_neighbors=m, metric='euclidean').fit(distance_matrix).kneighbors(distance_matrix)
    nn = np.zeros(distance_matrix.shape)
    np.put_along_axis(nn, indices, 1, axis=1)
    nn += nn.T
    nn[nn == 2] = 1
    return nn
def spectral_clustering(X, k, similarity_param, similarity_function=compute_gaussian_kernel_similarity):
    distance_matrix = compute_euclidean_distance_matrix(X, X)
    similarity_matrix = similarity_function(distance_matrix, similarity_param)
    degree_matrix = np.diag(np.sum(similarity_matrix, axis=1))
    inverse_sqrt_degree_matrix = np.diag(np.power(degree_matrix.diagonal(), -0.5))
    laplacian_matrix = np.identity(X.shape[0]) - inverse_sqrt_degree_matrix.dot(similarity_matrix).dot(inverse_sqrt_degree_matrix)
    eigenvalues, eigenvectors = np.linalg.eig(laplacian_matrix)
    indices = np.argpartition(eigenvalues, k)[:k]
    smallest_eigenvectors = eigenvectors[:, indices]
    clustering_labels = kmeans.kmeans(smallest_eigenvectors, k)[0]
    return clustering_labels