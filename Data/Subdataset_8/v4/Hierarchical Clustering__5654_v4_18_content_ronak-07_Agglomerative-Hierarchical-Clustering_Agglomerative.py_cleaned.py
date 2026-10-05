import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import time
def minimum(x, y):
    return min(x, y)
def maximum(x, y):
    return max(x, y)
def agglomerative_clustering(distance_matrix):
    size = len(distance_matrix)
    linkage_matrix = np.zeros(shape=(size - 1, 4))
    clusters = {i: [i] for i in range(size)}
    new_clusters = {i: -1 for i in range(size)}
    for k in range(size - 1):
        min_val, m, n = find_closest_clusters(distance_matrix, clusters, new_clusters, size)
        update_linkage_matrix(linkage_matrix, k, m, n, min_val, new_clusters, size)
        update_distance_matrix(distance_matrix, clusters, m, n)
    return linkage_matrix
def find_closest_clusters(distance_matrix, clusters, new_clusters, size):
    min_val = float('inf')
    m, n = -1, -1
    for i in range(size - 1):
        for j in range(i + 1, size):
            if distance_matrix[i][j] < min_val:
                min_val = distance_matrix[i][j]
                m, n = i, j
    if m > n:
        m, n = n, m
    return min_val, m, n
def update_linkage_matrix(linkage_matrix, k, m, n, min_val, new_clusters, size):
    linkage_matrix[k][0] = m
    linkage_matrix[k][1] = n
    new_clusters[size + k] = k
    if new_clusters[m] == -1 and new_clusters[n] == -1:
        linkage_matrix[k][3] = 2
    elif new_clusters[m] != -1 and new_clusters[n] != -1:
        linkage_matrix[k][3] = linkage_matrix[new_clusters[m]][3] + 1
    else:
        linkage_matrix[k][3] = linkage_matrix[maximum(new_clusters[m], new_clusters[n])][3] + 1
    linkage_matrix[k][2] = min_val
def update_distance_matrix(distance_matrix, clusters, m, n):
    for i in range(len(distance_matrix)):
        if i != n:
            distance_matrix[m][i] = minimum(distance_matrix[m][i], distance_matrix[n][i])
            distance_matrix[i][m] = distance_matrix[m][i]
            distance_matrix[n][i] = float('inf')
            distance_matrix[i][n] = float('inf')
def plot_dendrogram(linkage_matrix, labels):
    plt.figure(figsize=(25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    sch.dendrogram(linkage_matrix, labels=labels, show_leaf_counts=True, p=25, truncate_mode='lastp')
    plt.show()
if __name__ == "__main__":
    distance_matrix = np.load('distance_matrix.npy')
    linkage_matrix = agglomerative_clustering(distance_matrix)
    labels = [i for i in range(len(distance_matrix))]
    plot_dendrogram(linkage_matrix, labels)