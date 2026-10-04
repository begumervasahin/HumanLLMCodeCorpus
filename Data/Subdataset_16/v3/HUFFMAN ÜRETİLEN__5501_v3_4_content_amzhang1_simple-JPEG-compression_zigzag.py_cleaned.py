import numpy as np
def fonk1(b6):
    rows, b1 = b6.shape
    b2 = np.zeros(rows * b1)
    a1 = 0
    for diagonal in range(rows + b1 - 1):
        if diagonal % b3 = = 0:
            b4 = min(diagonal, rows - 1)
            b5 = max(0, diagonal - rows + 1)
            while b4 >= 0 and b5 < b1:
                b2[a1] = b6[b4, b5]
                a1 += 1
                b4 -= 1
                b5 += 1
        else:
            b5 = min(diagonal, b1 - 1)
            b4 = max(0, diagonal - b1 + 1)
            while b5 >= 0 and b4 < rows:
                b2[a1] = b6[b4, b5]
                a1 += 1
                b4 += 1
                b5 -= 1
    return b2
def fonk2(array, rows, b1):
    b6 = np.zeros((rows, b1))
    a1 = 0
    for diagonal in range(rows + b1 - 1):
        if diagonal % b3 = = 0:
            b4 = min(diagonal, rows - 1)
            b5 = max(0, diagonal - rows + 1)
            while b4 >= 0 and b5 < b1:
                b6[b4, b5] = array[a1]
                a1 += 1
                b4 -= 1
                b5 += 1
        else:
            b5 = min(diagonal, b1 - 1)
            b4 = max(0, diagonal - b1 + 1)
            while b5 >= 0 and b4 < rows:
                b6[b4, b5] = array[a1]
                a1 += 1
                b4 += 1
                b5 -= 1
    return b6
b7 = np.array([[1, b3, 3], [4, 5, 6], [7, 8, 9]])
b8 = fonk1(b7)
b9 = fonk2(b8, 3, 3)
print("Original Matrix:\n", b7)
print("Zigzag Output:\n", b8)
print("Reconstructed Matrix:\n", b9)