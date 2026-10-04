import numpy as np
def zigzag(input_matrix):
    vmax, hmax = input_matrix.shape
    output = np.zeros(vmax * hmax)
    v = h = i = 0
    while v < vmax and h < hmax:
        if (h + v) % 2 == 0:
            if v == 0 or h == hmax - 1:
                output[i] = input_matrix[v, h]
                i += 1
                if h == hmax - 1:
                    v += 1
                else:
                    h += 1
            else:
                output[i] = input_matrix[v, h]
                i += 1
                v -= 1
                h += 1
        else:
            if h == 0 or v == vmax - 1:
                output[i] = input_matrix[v, h]
                i += 1
                if v == vmax - 1:
                    h += 1
                else:
                    v += 1
            else:
                output[i] = input_matrix[v, h]
                i += 1
                v += 1
                h -= 1
        if v == vmax - 1 and h == hmax - 1:
            output[i] = input_matrix[v, h]
            break
    return output
def inverse_zigzag(input_array, vmax, hmax):
    output_matrix = np.zeros((vmax, hmax))
    v = h = i = 0
    while v < vmax and h < hmax:
        if (h + v) % 2 == 0:
            if v == 0 or h == hmax - 1:
                output_matrix[v, h] = input_array[i]
                i += 1
                if h == hmax - 1:
                    v += 1
                else:
                    h += 1
            else:
                output_matrix[v, h] = input_array[i]
                i += 1
                v -= 1
                h += 1
        else:
            if h == 0 or v == vmax - 1:
                output_matrix[v, h] = input_array[i]
                i += 1
                if v == vmax - 1:
                    h += 1
                else:
                    v += 1
            else:
                output_matrix[v, h] = input_array[i]
                i += 1
                v += 1
                h -= 1
        if v == vmax - 1 and h == hmax - 1:
            output_matrix[v, h] = input_array[i]
            break
    return output_matrix
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zigzag_output = zigzag(input_matrix)
inverse_output = inverse_zigzag(zigzag_output, 3, 3)
print("Original Matrix:\n", input_matrix)
print("Zigzag Output:\n", zigzag_output)
print("Reconstructed Matrix:\n", inverse_output)