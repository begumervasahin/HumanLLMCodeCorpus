import numpy as np
def zigzag(matrix):
    rows, cols = matrix.shape
    result = np.zeros(rows * cols)
    index = 0
    for diagonal in range(rows + cols - 1):
        if diagonal % 2 == 0:
            start_row = min(diagonal, rows - 1)
            start_col = max(0, diagonal - rows + 1)
            while start_row >= 0 and start_col < cols:
                result[index] = matrix[start_row, start_col]
                index += 1
                start_row -= 1
                start_col += 1
        else:
            start_col = min(diagonal, cols - 1)
            start_row = max(0, diagonal - cols + 1)
            while start_col >= 0 and start_row < rows:
                result[index] = matrix[start_row, start_col]
                index += 1
                start_row += 1
                start_col -= 1
    return result
def inverse_zigzag(array, rows, cols):
    matrix = np.zeros((rows, cols))
    index = 0
    for diagonal in range(rows + cols - 1):
        if diagonal % 2 == 0:
            start_row = min(diagonal, rows - 1)
            start_col = max(0, diagonal - rows + 1)
            while start_row >= 0 and start_col < cols:
                matrix[start_row, start_col] = array[index]
                index += 1
                start_row -= 1
                start_col += 1
        else:
            start_col = min(diagonal, cols - 1)
            start_row = max(0, diagonal - cols + 1)
            while start_col >= 0 and start_row < rows:
                matrix[start_row, start_col] = array[index]
                index += 1
                start_row += 1
                start_col -= 1
    return matrix
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zigzag_output = zigzag(input_matrix)
reconstructed_matrix = inverse_zigzag(zigzag_output, 3, 3)
print("Original Matrix:\n", input_matrix)
print("Zigzag Output:\n", zigzag_output)
print("Reconstructed Matrix:\n", reconstructed_matrix)