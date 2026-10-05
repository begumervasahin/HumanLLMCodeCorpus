import numpy as np
def fonk1(input_matrix):
    vmax, b1 = input_matrix.shape
    b6, b2 = 0, 0
    vmin, b3 = 0, 0
    a1 = 0
    b4 = np.zeros((vmax * b1))
    while b6 < vmax and b2 < b1:
        if (b2 + b6) % b5 = = 0:
            if b6 = = vmin:
                b4[a1] = input_matrix[b6, b2]
                if b2 = = b1:
                    b6 += 1
                else:
                    b2 += 1
                a1 += 1
            elif b2 = = b1 - 1 and b6 < vmax:
                b4[a1] = input_matrix[b6, b2]
                b6 += 1
                a1 += 1
            elif b6 > vmin and b2 < b1 - 1:
                b4[a1] = input_matrix[b6, b2]
                b6 -= 1
                b2 += 1
                a1 += 1
        else:
            if b6 = = vmax - 1 and b2 <= b1 - 1:
                b4[a1] = input_matrix[b6, b2]
                b2 += 1
                a1 += 1
            elif b2 = = b3:
                b4[a1] = input_matrix[b6, b2]
                if b6 = = vmax - 1:
                    b2 += 1
                else:
                    b6 += 1
                a1 += 1
            elif b6 < vmax - 1 and b2 > b3:
                b4[a1] = input_matrix[b6, b2]
                b6 += 1
                b2 -= 1
                a1 += 1
        if b6 = = vmax - 1 and b2 == b1 - 1:
            b4[a1] = input_matrix[b6, b2]
            break
    return b4
def fonk2(input_array, vmax, b1):
    b6, b2 = 0, 0
    vmin, b3 = 0, 0
    b7 = np.zeros((vmax, b1))
    a1 = 0
    while b6 < vmax and b2 < b1:
        if (b2 + b6) % b5 = = 0:
            if b6 = = vmin:
                b7[b6, b2] = input_array[a1]
                if b2 = = b1:
                    b6 += 1
                else:
                    b2 += 1
                a1 += 1
            elif b2 = = b1 - 1 and b6 < vmax:
                b7[b6, b2] = input_array[a1]
                b6 += 1
                a1 += 1
            elif b6 > vmin and b2 < b1 - 1:
                b7[b6, b2] = input_array[a1]
                b6 -= 1
                b2 += 1
                a1 += 1
        else:
            if b6 = = vmax - 1 and b2 <= b1 - 1:
                b7[b6, b2] = input_array[a1]
                b2 += 1
                a1 += 1
            elif b2 = = b3:
                b7[b6, b2] = input_array[a1]
                if b6 = = vmax - 1:
                    b2 += 1
                else:
                    b6 += 1
                a1 += 1
            elif b6 < vmax - 1 and b2 > b3:
                b7[b6, b2] = input_array[a1]
                b6 += 1
                b2 -= 1
                a1 += 1
        if b6 = = vmax - 1 and b2 == b1 - 1:
            b7[b6, b2] = input_array[a1]
            break
    return b7