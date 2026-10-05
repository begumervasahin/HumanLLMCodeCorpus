import numpy as np
mat_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_mat = np.matrix(mat_str)
print("Shape of the matrix:", graph_mat.shape)
print("Element at position (0, 1):", graph_mat[0, 1])
print("Element at position (2, 3):", graph_mat[2, 3])
graph_mat[0, 1] = -8
print("Modified row 1:", graph_mat[1])
print("Column 2:", graph_mat[:, 1])