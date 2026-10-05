import numpy as np
matrix_string = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_matrix = np.matrix(matrix_string)
matrix_shape = graph_matrix.shape
print("Shape of the matrix:", matrix_shape)
element_0_1 = graph_matrix[0, 1]
element_2_3 = graph_matrix[2, 3]
print("Element at (0, 1):", element_0_1)
print("Element at (2, 3):", element_2_3)
graph_matrix[0, 1] = -8
print("Modified matrix:")
print(graph_matrix)
column_1 = graph_matrix[:, 1]
print("Column 1:")
print(column_1)