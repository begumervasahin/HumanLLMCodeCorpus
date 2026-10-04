import numpy as np
def zigzag(input_matrix):
    rows, cols = input_matrix.shape
    output = np.zeros(rows * cols, dtype=input_matrix.dtype)
    index = 0
    for diag_sum in range(rows + cols - 1):
        if diag_sum % 2 == 0:
            row = min(diag_sum, rows - 1)
            col = diag_sum - row
            while row >= 0 and col < cols:
                output[index] = input_matrix[row, col]
                index += 1
                row -= 1
                col += 1
        else:
            col = min(diag_sum, cols - 1)
            row = diag_sum - col
            while col >= 0 and row < rows:
                output[index] = input_matrix[row, col]
                index += 1
                row += 1
                col -= 1
    return output
def inverse_zigzag(input_array, rows, cols):
    output_matrix = np.zeros((rows, cols), dtype=input_array.dtype)
    index = 0
    for diag_sum in range(rows + cols - 1):
        if diag_sum % 2 == 0:
            row = min(diag_sum, rows - 1)
            col = diag_sum - row
            while row >= 0 and col < cols:
                output_matrix[row, col] = input_array[index]
                index += 1
                row -= 1
                col += 1
        else:
            col = min(diag_sum, cols - 1)
            row = diag_sum - col
            while col >= 0 and row < rows:
                output_matrix[row, col] = input_array[index]
                index += 1
                row += 1
                col -= 1
    return output_matrix