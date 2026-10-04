import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
import time
def minimum(value1, value2):
    return value1 if value1 < value2 else value2
def maximum(value1, value2):
    return value1 if value1 > value2 else value2
def perform_clustering(distance_matrix, size, step, linkage_matrix, cluster_dict, cluster_indices):
    min_distance = 9999.0
    cluster1 = cluster2 = -1
    for i in range(size - 1):
        for j in range(i + 1, size):
            if distance_matrix[i][j] < min_distance:
                min_distance = distance_matrix[i][j]
                cluster1, cluster2 = i, j
    if cluster1 < cluster2:
        cluster_dict[cluster1].extend(cluster_dict.pop(cluster2))
    else:
        cluster_dict[cluster2].extend(cluster_dict.pop(cluster1))
    if cluster_indices[cluster1] == -1 and cluster_indices[cluster2] == -1:
        linkage_matrix[step, 0] = cluster1
        linkage_matrix[step, 1] = cluster2
        cluster_indices[minimum(cluster1, cluster2)] = size + step
        linkage_matrix[step, 3] = 2
    elif cluster_indices[cluster1] != -1 and cluster_indices[cluster2] != -1:
        linkage_matrix[step, 0] = cluster_indices[cluster1]
        linkage_matrix[step, 1] = cluster_indices[cluster2]
        cluster_indices[cluster1 if cluster1 < cluster2 else cluster2] = size + step
        linkage_matrix[step, 3] = linkage_matrix[int(maximum(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
    elif cluster_indices[cluster1] != -1 and cluster_indices[cluster2] == -1:
        linkage_matrix[step, 0] = cluster_indices[cluster1]
        linkage_matrix[step, 1] = cluster2
        linkage_matrix[step, 3] = linkage_matrix[int(maximum(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
        cluster_indices[cluster1] = size + step
    elif cluster_indices[cluster1] == -1 and cluster_indices[cluster2] != -1:
        linkage_matrix[step, 0] = cluster1
        linkage_matrix[step, 1] = cluster_indices[cluster2]
        linkage_matrix[step, 3] = linkage_matrix[int(maximum(linkage_matrix[step, 0], linkage_matrix[step, 1]) - size), 3] + 1
        cluster_indices[cluster2] = size + step
    else:
        raise ValueError("Error in cluster assignment.")
    linkage_matrix[step, 2] = min_distance
    for j in range(size):
        if j != cluster2:
            distance_matrix[j][cluster1] = minimum(distance_matrix[j][cluster1], distance_matrix[j][cluster2])
            distance_matrix[cluster1][j] = distance_matrix[j][cluster1]
        distance_matrix[j][cluster2] = 9999.0
        distance_matrix[cluster2][j] = 9999.0
    return distance_matrix
def plot_dendrogram(*args, **kwargs):
    dendro_data = hierarchy.dendrogram(*args, **kwargs)
    if not kwargs.get('no_plot', False):
        for x_coords, y_coords in zip(dendro_data['icoord'], dendro_data['dcoord']):
            x = 0.5 * sum(x_coords[1:3])
            y = y_coords[1]
            plt.plot(x, y, 'ro')
            plt.annotate(f"{y:.3g}", (x, y), xytext=(0, 12), textcoords='offset points', va='top', ha='center')
    return dendro_data
distance_matrix = np.load('distance_matrix.npy')
size = len(distance_matrix)
linkage_matrix = np.zeros((size - 1, 4))
cluster_dict = {i: [i] for i in range(size)}
cluster_indices = {i: -1 for i in range(size)}
start_time = time.time()
for step in range(size - 1):
    distance_matrix = perform_clustering(distance_matrix, size, step, linkage_matrix, cluster_dict, cluster_indices)
print(f"Clustering done in {time.time() - start_time:.2f} seconds")
plt.figure(figsize=(25, 25))
plt.title('Hierarchical Clustering Dendrogram (Agglomerative)')
plt.xlabel('Sequence No.')
plt.ylabel('Distance')
plot_dendrogram(linkage_matrix, labels=list(range(size)), show_leaf_counts=True, p=25, truncate_mode='lastp')
plt.show()