import numpy as np
matrix_string = '1 2 3 4; 5 6 7 8; 0 1 2 3'
matrix = np.matrix(matrix_string)
print("Shape of the matrix:", matrix.shape)
element_1_2 = matrix[0, 1]
element_3_4 = matrix[2, 3]
print(f"Element at row 0, column 1: {element_1_2}")
print(f"Element at row 2, column 3: {element_3_4}")
matrix[0, 1] = -8
print("Modified matrix:")
print(matrix)
second_column = matrix[:, 1]
print("Second column of the matrix:")
print(second_column)