import numpy as np
import sys
def parse_input_line(line):
    cluster, index, matrix_string = line.strip().split('\t')
    cluster = int(cluster)
    index = int(index)
    matrix = np.array([float(x) for x in matrix_string.split(',')])
    return cluster, index, matrix
def print_cluster_output(cluster, output_matrix, new_centroid):
    output_str = '%s\t%s\t%s' % (cluster, ','.join(map(str, output_matrix)), ','.join(map(str, new_centroid)))
    print(output_str)
output_matrix = []
sum_for_centroid = []
current_cluster = -2
matrix_length = -1
for line in sys.stdin:
    cluster, index, matrix = parse_input_line(line)
    matrix_length = len(matrix)
    if current_cluster != cluster:
        if current_cluster != -2:
            new_centroid = sum_for_centroid / len(output_matrix)
            print_cluster_output(current_cluster, output_matrix, new_centroid)
        output_matrix = []
        sum_for_centroid = np.zeros(matrix_length)
        current_cluster = cluster
    output_matrix.append(index)
    sum_for_centroid += matrix
new_centroid = sum_for_centroid / len(output_matrix)
print_cluster_output(current_cluster, output_matrix, new_centroid)