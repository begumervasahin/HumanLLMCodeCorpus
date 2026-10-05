import numpy as np
matrix_string = '1 2 3 4; 5 6 7 8; 0 1 2 3'
matrix = np.matrix(matrix_string)
shape = matrix.shape
print("Shape of the matrix:", shape)
element_0_1 = matrix[0, 1]
element_2_3 = matrix[2, 3]
print("Element at [0, 1]:", element_0_1)
print("Element at [2, 3]:", element_2_3)
matrix[0, 1] = -8
column_1 = matrix[:, 1]
print("Column 1 of the matrix:")
print(column_1)