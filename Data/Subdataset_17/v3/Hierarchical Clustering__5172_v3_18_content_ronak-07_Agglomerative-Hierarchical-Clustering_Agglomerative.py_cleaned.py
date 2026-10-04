import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import time
def find_minimum_distance_pair(distance_matrix, size):
    min_distance = float('inf')
    cluster1, cluster2 = -1, -1
    for i in range(size - 1):
        for j in range(i + 1, size):
            if distance_matrix[i][j] < min_distance:
                min_distance = distance_matrix[i][j]
                cluster1, cluster2 = i, j
    return cluster1, cluster2, min_distance
def update_cluster_indices(cluster1, cluster2, size, step, linkage_matrix, cluster_indices):
    if cluster_indices[cluster1] == -1 and cluster_indices[cluster2] == -1:
        linkage_matrix[step, 0] = cluster1
        linkage_matrix[step, 1] = cluster2
        cluster_indices[min(cluster1, cluster2)] = size + step
        linkage_matrix[step, 3] = 2
    elif cluster_indices[cluster1] != -1 and cluster_indices[cluster2] != -1:
        linkage_matrix[step, 0] = cluster_indices[cluster1]
        linkage_matrix[step, 1] = cluster_indices[cluster2]
        cluster_indices[min(cluster1, cluster2)] = size + step
        linkage_matrix[step, 3] = linkage_matrix[int(max(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
    elif cluster_indices[cluster1] != -1:
        linkage_matrix[step, 0] = cluster_indices[cluster1]
        linkage_matrix[step, 1] = cluster2
        linkage_matrix[step, 3] = linkage_matrix[int(max(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
        cluster_indices[cluster1] = size + step
    else:
        linkage_matrix[step, 0] = cluster1
        linkage_matrix[step, 1] = cluster_indices[cluster2]
        linkage_matrix[step, 3] = linkage_matrix[int(max(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
        cluster_indices[cluster2] = size + step
def merge_clusters(cluster1, cluster2, cluster_dict):
    if cluster1 < cluster2:
        cluster_dict[cluster1].extend(cluster_dict.pop(cluster2))
    else:
        cluster_dict[cluster2].extend(cluster_dict.pop(cluster1))
def update_distance_matrix(distance_matrix, cluster1, cluster2, size):
    for j in range(size):
        if j != cluster2:
            distance_matrix[j][cluster1] = min(distance_matrix[j][cluster1], distance_matrix[j][cluster2])
            distance_matrix[cluster1][j] = distance_matrix[j][cluster1]
        distance_matrix[j][cluster2] = float('inf')
        distance_matrix[cluster2][j] = float('inf')
def perform_clustering(distance_matrix, size, linkage_matrix, cluster_dict, cluster_indices):
    for step in range(size - 1):
        cluster1, cluster2, min_distance = find_minimum_distance_pair(distance_matrix, size)
        merge_clusters(cluster1, cluster2, cluster_dict)
        update_cluster_indices(cluster1, cluster2, size, step, linkage_matrix, cluster_indices)
        linkage_matrix[step, 2] = min_distance
        update_distance_matrix(distance_matrix, cluster1, cluster2, size)
def plot_dendrogram(linkage_matrix, size):
    plt.figure(figsize=(25, 25))
    plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
    plt.xlabel('Sequence No.')
    plt.ylabel('Distance')
    dendro_data = hierarchy.dendrogram(
        linkage_matrix,
        labels=list(range(size)),
        show_leaf_counts=True,
        p=25,
        truncate_mode='lastp'
    )
    for x_coords, y_coords in zip(dendro_data['icoord'], dendro_data['dcoord']):
        x = 0.5 * sum(x_coords[1:3])
        y = y_coords[1]
        plt.plot(x, y, 'ro')
        plt.annotate(f"{y:.3g}", (x, y), xytext=(0, 12), textcoords='offset points', va='top', ha='center')
    plt.show()
def main():
    distance_matrix = np.load('distance_matrix.npy')
    size = len(distance_matrix)
    linkage_matrix = np.zeros((size - 1, 4))
    cluster_dict = {i: [i] for i in range(size)}
    cluster_indices = {i: -1 for i in range(size)}
    start_time = time.time()
    perform_clustering(distance_matrix, size, linkage_matrix, cluster_dict, cluster_indices)
    print(f"Clustering done in {time.time() - start_time:.2f} seconds")
    plot_dendrogram(linkage_matrix, size)
if __name__ == "__main__":
    main()