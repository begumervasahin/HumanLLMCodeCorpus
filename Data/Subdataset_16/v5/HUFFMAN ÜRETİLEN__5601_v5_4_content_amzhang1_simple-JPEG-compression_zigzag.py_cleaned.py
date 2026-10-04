import numpy as np
def fonk1(input_matrix):
    rows, b1 = input_matrix.shape
    b2 = np.zeros(rows * b1, dtype=input_matrix.dtype)
    a1 = 0
    for diag_sum in range(rows + b1 - 1):
        if diag_sum % b3 = = 0:
            b4 = min(diag_sum, rows - 1)
            b5 = diag_sum - b4
            while b4 >= 0 and b5 < b1:
                b2[a1] = input_matrix[b4, b5]
                a1 += 1
                b4 -= 1
                b5 += 1
        else:
            b5 = min(diag_sum, b1 - 1)
            b4 = diag_sum - b5
            while b5 >= 0 and b4 < rows:
                b2[a1] = input_matrix[b4, b5]
                a1 += 1
                b4 += 1
                b5 -= 1
    return b2
def fonk2(input_array, rows, b1):
    b6 = np.zeros((rows, b1), dtype=input_array.dtype)
    a1 = 0
    for diag_sum in range(rows + b1 - 1):
        if diag_sum % b3 = = 0:
            b4 = min(diag_sum, rows - 1)
            b5 = diag_sum - b4
            while b4 >= 0 and b5 < b1:
                b6[b4, b5] = input_array[a1]
                a1 += 1
                b4 -= 1
                b5 += 1
        else:
            b5 = min(diag_sum, b1 - 1)
            b4 = diag_sum - b5
            while b5 >= 0 and b4 < rows:
                b6[b4, b5] = input_array[a1]
                a1 += 1
                b4 += 1
                b5 -= 1
    return b6