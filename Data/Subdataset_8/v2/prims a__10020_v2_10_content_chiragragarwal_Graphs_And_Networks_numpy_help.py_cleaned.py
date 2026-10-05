import numpy as np
matrix_string = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
matrix = np.matrix(matrix_string)
print("The matrix has a shape of:", matrix.shape)
print("The element at row 0, column 1 is:", matrix[0, 1])
print("The element at row 2, column 3 is:", matrix[2, 3])
matrix[0, 1] = -8
print("Modified matrix:")
print(matrix)
print("The second column of the matrix is:")
print(matrix[:, 1])