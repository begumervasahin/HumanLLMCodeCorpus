import numpy as np
import sys
output_matrix = []
sum_for_centroid = []
current_cluster = -2
matrix_length = -1
for line in sys.stdin:
    line = line.strip()
    cluster, index, matrix_string = line.split('\t')
    matrix = np.array([float(x) for x in matrix_string.split(',')])
    matrix_length = len(matrix)
    cluster = int(cluster)
    index = int(index)
    if current_cluster != cluster:
        if current_cluster != -2:
            new_centroid = sum_for_centroid / len(output_matrix)
            print('%s\t%s\t%s' % (current_cluster, ','.join(map(str, output_matrix)), ','.join(map(str, new_centroid))))
        output_matrix = []
        sum_for_centroid = np.zeros(matrix_length)
        current_cluster = cluster
    output_matrix.append(index)
    sum_for_centroid += matrix
new_centroid = sum_for_centroid / len(output_matrix)
print('%s\t%s\t%s' % (current_cluster, ','.join(map(str, output_matrix)), ','.join(map(str, new_centroid))))