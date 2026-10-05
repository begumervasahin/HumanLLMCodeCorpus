import numpy as np
mat_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_mat = np.matrix(mat_str)
shape = graph_mat.shape
print("Shape of the matrix:", shape)
element_1_2 = graph_mat[0, 1]
element_2_3 = graph_mat[2, 3]
print("Element at (0, 1):", element_1_2)
print("Element at (2, 3):", element_2_3)
graph_mat[0, 1] = -8
print("Modified matrix:")
print(graph_mat)
column_1 = graph_mat[:, 1]
print("Column 1:")
print(column_1)