import numpy as np
matrix_string = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_matrix = np.matrix(matrix_string)
print("Shape of the matrix:", graph_matrix.shape)
print("Element at position (0, 1):", graph_matrix[0, 1])
print("Element at position (2, 3):", graph_matrix[2, 3])
graph_matrix[0, 1] = -8
print("Modified row 1:", graph_matrix[1])
print("Column 2:", graph_matrix[:, 1])