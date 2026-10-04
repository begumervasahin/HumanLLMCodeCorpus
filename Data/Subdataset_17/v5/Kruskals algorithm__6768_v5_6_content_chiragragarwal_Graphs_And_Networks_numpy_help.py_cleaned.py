import numpy as np
matrix_string = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graph_matrix = np.matrix(matrix_string)
print("Matrix shape:", graph_matrix.shape)
element_0_1 = graph_matrix[0, 1]
element_2_3 = graph_matrix[2, 3]
print(f"Element at position (0, 1): {element_0_1}")
print(f"Element at position (2, 3): {element_2_3}")
graph_matrix[0, 1] = -8
print("Matrix after modifying element (0, 1):\n", graph_matrix)
row_1 = graph_matrix[1]
column_1 = graph_matrix[:, 1]
print("Row 1:\n", row_1)
print("Column 1:\n", column_1)