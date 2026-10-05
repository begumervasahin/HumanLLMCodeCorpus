from scipy.sparse import csc_matrix
import numpy as np
import math
import heapq as hp
import sys
from collections import Counter
def centroid(indices, matrix):
    centroid_sum = sum(matrix[i] for i in indices)
    return centroid_sum / len(indices)
file_path = sys.argv[1]
cluster_size = int(sys.argv[2])
with open(file_path, 'r') as file:
    file_content = file.readlines()
num_documents = int(file_content[0])
num_words = int(file_content[1])
row_indices = []
col_indices = []
values = []
for line in file_content[3:]:
    doc_idx, word_idx, value = map(int, line.strip().split())
    row_indices.append(doc_idx - 1)
    col_indices.append(word_idx - 1)
    values.append(value)
word_counts_per_doc = Counter(col_indices)
for i in range(len(values)):
    values[i] *= math.log(float(num_documents + 1) / (word_counts_per_doc[col_indices[i]] + 1), 2)
sparse_matrix = csc_matrix((values, (row_indices, col_indices)), shape=(num_documents, num_words))
norms = np.asarray(np.sqrt(sparse_matrix.power(2).sum(axis=1)))
normalized_matrix = csc_matrix(sparse_matrix / norms)
document_vectors = {i: normalized_matrix[i] for i in range(normalized_matrix.shape[0])}
similarity_heap = []
for i in range(normalized_matrix.shape[0]):
    for j in range(i + 1, normalized_matrix.shape[0]):
        temp_matrix = document_vectors[i].multiply(document_vectors[j])
        denominator = np.sqrt((document_vectors[i].power(2).sum())) * np.sqrt((document_vectors[j].power(2).sum()))
        similarity = (temp_matrix.sum()) / denominator
        hp.heappush(similarity_heap, (1 - similarity, i, j))
clustered_documents = {}
iterations = 0
while iterations < num_documents - cluster_size:
    similarity_tuple = hp.heappop(similarity_heap)
    if similarity_tuple[1] in clustered_documents or similarity_tuple[2] in clustered_documents:
        continue
    elif isinstance(similarity_tuple[1], int) and isinstance(similarity_tuple[2], int):
        clustered_documents[similarity_tuple[1]] = None
        clustered_documents[similarity_tuple[2]] = None
        current_cluster = (similarity_tuple[1], similarity_tuple[2])
        centroid_vector = centroid(current_cluster, normalized_matrix)
        del document_vectors[similarity_tuple[1]]
        del document_vectors[similarity_tuple[2]]
    else:
        clustered_documents[similarity_tuple[1]] = None
        clustered_documents[similarity_tuple[2]] = None
        if isinstance(similarity_tuple[1], int):
            current_cluster = similarity_tuple[2] + (similarity_tuple[1],)
        elif isinstance(similarity_tuple[2], int):
            current_cluster = similarity_tuple[1] + (similarity_tuple[2],)
        else:
            current_cluster = similarity_tuple[1] + similarity_tuple[2]
        del document_vectors[similarity_tuple[1]]
        del document_vectors[similarity_tuple[2]]
        centroid_vector = centroid(current_cluster, normalized_matrix)
    for i in document_vectors:
        if i not in clustered_documents:
            temp_matrix = centroid_vector.multiply(document_vectors[i])
            denominator = np.sqrt((document_vectors[i].power(2).sum())) * np.sqrt((centroid_vector.power(2).sum()))
            similarity = (temp_matrix.sum()) / denominator
            hp.heappush(similarity_heap, (1 - similarity, current_cluster, i))
    document_vectors[current_cluster] = centroid_vector
    iterations += 1
for cluster in clustered_documents:
    if isinstance(cluster, int):
        print(cluster + 1)
    else:
        print(','.join(str(doc_index + 1) for doc_index in sorted(cluster)))