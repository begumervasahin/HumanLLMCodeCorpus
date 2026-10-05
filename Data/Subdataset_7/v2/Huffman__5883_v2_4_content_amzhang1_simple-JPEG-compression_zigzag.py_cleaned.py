import numpy as np
def fonk1(b5):
    vmax, b1 = b5.shape
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    b2 = np.zeros((vmax * b1))
    while a2 < vmax and a1 < b1:
        if (a1 + a2) % b3 = = 0:
            if a2 = = a3:
                b2[a5] = b5[a2, a1]
                if a1 = = b1:
                    a2 += 1
                else:
                    a1 += 1
                a5 += 1
            elif a1 = = b1 - 1 and a2 < vmax:
                b2[a5] = b5[a2, a1]
                a2 += 1
                a5 += 1
            elif a2 > a3 and a1 < b1 - 1:
                b2[a5] = b5[a2, a1]
                a2 -= 1
                a1 += 1
                a5 += 1
        else:
            if a2 = = vmax - 1 and a1 <= b1 - 1:
                b2[a5] = b5[a2, a1]
                a1 += 1
                a5 += 1
            elif a1 = = a4:
                b2[a5] = b5[a2, a1]
                if a2 = = vmax - 1:
                    a1 += 1
                else:
                    a2 += 1
                a5 += 1
            elif a2 < vmax - 1 and a1 > a4:
                b2[a5] = b5[a2, a1]
                a2 += 1
                a1 -= 1
                a5 += 1
        if a2 = = vmax - 1 and a1 == b1 - 1:
            b2[a5] = b5[a2, a1]
            break
    return b2
def fonk2(input_array, vmax, b1):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b4 = np.zeros((vmax, b1))
    a5 = 0
    while a2 < vmax and a1 < b1:
        if (a1 + a2) % b3 = = 0:
            if a2 = = a3:
                b4[a2, a1] = input_array[a5]
                if a1 = = b1:
                    a2 += 1
                else:
                    a1 += 1
                a5 += 1
            elif a1 = = b1 - 1 and a2 < vmax:
                b4[a2, a1] = input_array[a5]
                a2 += 1
                a5 += 1
            elif a2 > a3 and a1 < b1 - 1:
                b4[a2, a1] = input_array[a5]
                a2 -= 1
                a1 += 1
                a5 += 1
        else:
            if a2 = = vmax - 1 and a1 <= b1 - 1:
                b4[a2, a1] = input_array[a5]
                a1 += 1
                a5 += 1
            elif a1 = = a4:
                b4[a2, a1] = input_array[a5]
                if a2 = = vmax - 1:
                    a1 += 1
                else:
                    a2 += 1
                a5 += 1
            elif a2 < vmax - 1 and a1 > a4:
                b4[a2, a1] = input_array[a5]
                a2 += 1
                a1 -= 1
                a5 += 1
        if a2 = = vmax - 1 and a1 == b1 - 1:
            b4[a2, a1] = input_array[a5]
            break
    return b4
b5 = np.array([[1, b3, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
b6 = fonk1(b5)
print("Zigzag b2:")
print(b6)
b7 = fonk2(b6, 3, 3)
print("\nInverse Zigzag b2:")
print(b7)