import numpy as np
matrix_string = '1 2 3 4; 5 6 7 8; 0 1 2 3'
graph_matrix = np.matrix(matrix_string)
matrix_shape = graph_matrix.shape
element_1_2 = graph_matrix[0, 1]
element_2_3 = graph_matrix[1, 2]
graph_matrix[0, 1] = -8
first_row = graph_matrix[0, :]
second_column = graph_matrix[:, 1]
