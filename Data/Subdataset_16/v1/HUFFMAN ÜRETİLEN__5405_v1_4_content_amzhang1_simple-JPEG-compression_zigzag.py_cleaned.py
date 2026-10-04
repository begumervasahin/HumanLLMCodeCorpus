import numpy as np
def fonk1(b7):
    vmax, b1 = b7.shape
    b2 = np.zeros(vmax * b1)
    b3 = b5 = i = 0
    while b3 < vmax and b5 < b1:
        if (b5 + b3) % b4 = = 0:
            if b3 = = 0 or b5 == b1 - 1:
                b2[i] = b7[b3, b5]
                i += 1
                if b5 = = b1 - 1:
                    b3 += 1
                else:
                    b5 += 1
            else:
                b2[i] = b7[b3, b5]
                i += 1
                b3 -= 1
                b5 += 1
        else:
            if b5 = = 0 or b3 == vmax - 1:
                b2[i] = b7[b3, b5]
                i += 1
                if b3 = = vmax - 1:
                    b5 += 1
                else:
                    b3 += 1
            else:
                b2[i] = b7[b3, b5]
                i += 1
                b3 += 1
                b5 -= 1
        if b3 = = vmax - 1 and b5 == b1 - 1:
            b2[i] = b7[b3, b5]
            break
    return b2
def fonk2(input_array, vmax, b1):
    b6 = np.zeros((vmax, b1))
    b3 = b5 = i = 0
    while b3 < vmax and b5 < b1:
        if (b5 + b3) % b4 = = 0:
            if b3 = = 0 or b5 == b1 - 1:
                b6[b3, b5] = input_array[i]
                i += 1
                if b5 = = b1 - 1:
                    b3 += 1
                else:
                    b5 += 1
            else:
                b6[b3, b5] = input_array[i]
                i += 1
                b3 -= 1
                b5 += 1
        else:
            if b5 = = 0 or b3 == vmax - 1:
                b6[b3, b5] = input_array[i]
                i += 1
                if b3 = = vmax - 1:
                    b5 += 1
                else:
                    b3 += 1
            else:
                b6[b3, b5] = input_array[i]
                i += 1
                b3 += 1
                b5 -= 1
        if b3 = = vmax - 1 and b5 == b1 - 1:
            b6[b3, b5] = input_array[i]
            break
    return b6
b7 = np.array([[1, b4, 3], [4, 5, 6], [7, 8, 9]])
b8 = fonk1(b7)
b9 = fonk2(b8, 3, 3)
print("Original Matrix:\n", b7)
print("Zigzag Output:\n", b8)
print("Reconstructed Matrix:\n", b9)