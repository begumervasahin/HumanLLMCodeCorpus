import numpy as np
matrix_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_matrix = np.matrix(matrix_str)
print("Matrix shape:", graph_matrix.shape)
element_at_0_1 = graph_matrix[0, 1]
element_at_2_3 = graph_matrix[2, 3]
print("Element at (0,1):", element_at_0_1)
print("Element at (2,3):", element_at_2_3)
graph_matrix[0, 1] = -8
second_row = graph_matrix[1]
print("Second row:", second_row)
second_column = graph_matrix[:, 1]
print("Second column:", second_column)