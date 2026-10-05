import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors
def euclidean_distance_matrix(X, Y):
    return euclidean_distances(X, Y)
def gaussian_kernel_similarity(distance_matrix, sigma):
    return np.exp(-np.square(distance_matrix) / (2 * np.square(sigma)))
def m_nearest_neighbors_similarity(distance_matrix, m):
    _, indices = NearestNeighbors(n_neighbors=m, metric='euclidean').fit(distance_matrix).kneighbors(distance_matrix)
    nearest_neighbors_matrix = np.zeros(distance_matrix.shape)
    np.put_along_axis(nearest_neighbors_matrix, indices, 1, axis=1)
    nearest_neighbors_matrix += nearest_neighbors_matrix.T
    nearest_neighbors_matrix[nearest_neighbors_matrix == 2] = 1
    return nearest_neighbors_matrix
def spectral_clustering(data_matrix, num_clusters, similarity_param, similarity_function=gaussian_kernel_similarity):
    distance_matrix = euclidean_distance_matrix(data_matrix, data_matrix)
    similarity_matrix = similarity_function(distance_matrix, similarity_param)
    row_sum = np.sum(similarity_matrix, axis=1)
    degree_matrix = np.diag(row_sum)
    degree_matrix_inverse_sqrt = np.diag(1 / np.sqrt(row_sum))
    laplacian_matrix = np.identity(data_matrix.shape[0]) - degree_matrix_inverse_sqrt.dot(similarity_matrix).dot(degree_matrix_inverse_sqrt)
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)
    sorted_indices = np.argsort(eigenvalues)
    selected_eigenvectors = eigenvectors[:, sorted_indices[0:num_clusters]]
    return selected_eigenvectors
