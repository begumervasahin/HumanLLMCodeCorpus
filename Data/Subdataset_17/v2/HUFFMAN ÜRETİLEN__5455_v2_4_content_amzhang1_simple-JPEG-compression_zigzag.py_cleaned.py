import numpy as np
def zigzag(matrix):
    vmax, hmax = matrix.shape
    result = np.zeros(vmax * hmax)
    i = v = h = 0
    while i < vmax * hmax:
        result[i] = matrix[v, h]
        i += 1
        if (v + h) % 2 == 0:
            if h == hmax - 1:
                v += 1
            elif v == 0:
                h += 1
            else:
                v -= 1
                h += 1
        else:
            if v == vmax - 1:
                h += 1
            elif h == 0:
                v += 1
            else:
                v += 1
                h -= 1
    return result
def inverse_zigzag(array, vmax, hmax):
    matrix = np.zeros((vmax, hmax))
    i = v = h = 0
    while i < vmax * hmax:
        matrix[v, h] = array[i]
        i += 1
        if (v + h) % 2 == 0:
            if h == hmax - 1:
                v += 1
            elif v == 0:
                h += 1
            else:
                v -= 1
                h += 1
        else:
            if v == vmax - 1:
                h += 1
            elif h == 0:
                v += 1
            else:
                v += 1
                h -= 1
    return matrix
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zigzag_output = zigzag(input_matrix)
reconstructed_matrix = inverse_zigzag(zigzag_output, 3, 3)
print("Original Matrix:\n", input_matrix)
print("Zigzag Output:\n", zigzag_output)
print("Reconstructed Matrix:\n", reconstructed_matrix)