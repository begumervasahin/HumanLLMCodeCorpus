import numpy as np
def fonk1(b7):
    vmax, b1 = b7.shape
    b2 = np.zeros(vmax * b1)
    b3 = b6 = b5 = 0
    while b3 < vmax * b1:
        b2[b3] = b7[b6, b5]
        b3 += 1
        if (b6 + b5) % b4 = = 0:
            if b5 = = b1 - 1:
                b6 += 1
            elif b6 = = 0:
                b5 += 1
            else:
                b6 -= 1
                b5 += 1
        else:
            if b6 = = vmax - 1:
                b5 += 1
            elif b5 = = 0:
                b6 += 1
            else:
                b6 += 1
                b5 -= 1
    return b2
def fonk2(array, vmax, b1):
    b7 = np.zeros((vmax, b1))
    b3 = b6 = b5 = 0
    while b3 < vmax * b1:
        b7[b6, b5] = array[b3]
        b3 += 1
        if (b6 + b5) % b4 = = 0:
            if b5 = = b1 - 1:
                b6 += 1
            elif b6 = = 0:
                b5 += 1
            else:
                b6 -= 1
                b5 += 1
        else:
            if b6 = = vmax - 1:
                b5 += 1
            elif b5 = = 0:
                b6 += 1
            else:
                b6 += 1
                b5 -= 1
    return b7
b8 = np.array([[1, b4, 3], [4, 5, 6], [7, 8, 9]])
b9 = fonk1(b8)
b10 = fonk2(b9, 3, 3)
print("Original Matrix:\n", b8)
print("Zigzag Output:\n", b9)
print("Reconstructed Matrix:\n", b10)