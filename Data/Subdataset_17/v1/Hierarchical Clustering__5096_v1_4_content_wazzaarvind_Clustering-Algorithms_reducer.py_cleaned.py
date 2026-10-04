import numpy as np
import sys
def process_input():
    output_matrix = []
    sum_for_centroid = []
    new_cluster = -2
    len_matrix = -1
    for line in sys.stdin:
        line = line.strip()
        cluster, index, matrix_string = line.split('\t')
        matrix = np.array([float(x) for x in matrix_string.split(',')])
        len_matrix = len(matrix)
        cluster = int(cluster)
        index = int(index)
        if new_cluster != cluster:
            if new_cluster != -2:
                new_centroid = sum_for_centroid / len(output_matrix)
                print(f'{new_cluster}\t{",".join(map(str, output_matrix))}\t{",".join(map(str, new_centroid))}')
            output_matrix = []
            sum_for_centroid = np.zeros(len(matrix))
            new_cluster = cluster
        output_matrix.append(index)
        sum_for_centroid += matrix
    new_centroid = sum_for_centroid / len(output_matrix)
    print(f'{new_cluster}\t{",".join(map(str, output_matrix))}\t{",".join(map(str, new_centroid))}')
if __name__ == "__main__":
    process_input()