from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def calculate_centroid(cluster_indices, matrix):
    centroid = sum(matrix[i] for i in cluster_indices) / len(cluster_indices)
    return centroid
def load_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    num_docs = int(lines[0].strip())
    num_words = int(lines[1].strip())
    row_indices, col_indices, values = [], [], []
    for line in lines[2:]:
        doc_id, word_id, count = map(int, line.split())
        row_indices.append(doc_id - 1)
        col_indices.append(word_id - 1)
        values.append(count)
    return num_docs, num_words, row_indices, col_indices, values
def normalize_matrix(num_docs, num_words, row_indices, col_indices, values):
    term_frequencies = Counter(col_indices)
    for i in range(len(values)):
        tf_idf_weight = math.log((num_docs + 1) / (term_frequencies[col_indices[i]] + 1), 2)
        values[i] *= tf_idf_weight
    sparse_matrix = csc_matrix((values, (row_indices, col_indices)), shape=(num_docs, num_words))
    normalization_factors = np.sqrt(sparse_matrix.power(2).sum(axis=1))
    normalized_matrix = sparse_matrix / normalization_factors
    return normalized_matrix
def hierarchical_clustering(num_docs, num_clusters, normalized_matrix):
    clusters = {i: normalized_matrix[i] for i in range(normalized_matrix.shape[0])}
    merged_clusters = {}
    heap = []
    for i in clusters:
        for j in clusters:
            if i < j:
                similarity = (clusters[i].multiply(clusters[j]).sum()) / \
                             (np.sqrt(clusters[i].power(2).sum()) * np.sqrt(clusters[j].power(2).sum()))
                hp.heappush(heap, (1 - similarity, i, j))
    while len(clusters) > num_clusters:
        _, cluster1, cluster2 = hp.heappop(heap)
        if cluster1 in merged_clusters or cluster2 in merged_clusters:
            continue
        merged_clusters[cluster1] = None
        merged_clusters[cluster2] = None
        new_cluster = (cluster1, cluster2) if isinstance(cluster1, int) else cluster1 + (cluster2,)
        new_centroid = calculate_centroid(new_cluster, normalized_matrix)
        del clusters[cluster1]
        del clusters[cluster2]
        for i in clusters:
            if i not in merged_clusters:
                similarity = (new_centroid.multiply(clusters[i]).sum()) / \
                             (np.sqrt(clusters[i].power(2).sum()) * np.sqrt(new_centroid.power(2).sum()))
                hp.heappush(heap, (1 - similarity, new_cluster, i))
        clusters[new_cluster] = new_centroid
    return clusters
def print_clusters(clusters):
    for cluster in clusters:
        if isinstance(cluster, int):
            print(cluster + 1)
        else:
            print(','.join(str(idx + 1) for idx in sorted(cluster)))
def main():
    file_path = sys.argv[1]
    num_clusters = int(sys.argv[2])
    num_docs, num_words, row_indices, col_indices, values = load_data(file_path)
    normalized_matrix = normalize_matrix(num_docs, num_words, row_indices, col_indices, values)
    clusters = hierarchical_clustering(num_docs, num_clusters, normalized_matrix)
    print_clusters(clusters)
if __name__ == "__main__":
    main()