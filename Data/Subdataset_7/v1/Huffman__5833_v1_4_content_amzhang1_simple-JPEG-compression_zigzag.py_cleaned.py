import numpy as np
def fonk1(input):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b1 = input.shape[0]
    b2 = input.shape[1]
    a5 = 0
    b3 = np.zeros((b1 * b2))
    while ((a2 < b1) and (a1 < b2)):
        if ((a1 + a2) % 2) == 0:
            if (a2 = = a3):
                b3[a5] = input[a2, a1]
                if (a1 = = b2):
                    a2 = a2 + 1
                else:
                    a1 = a1 + 1
                a5 = a5 + 1
            elif ((a1 = = b2 - 1) and (a2 < b1)):
                b3[a5] = input[a2, a1]
                a2 = a2 + 1
                a5 = a5 + 1
            elif ((a2 > a3) and (a1 < b2 - 1)):
                b3[a5] = input[a2, a1]
                a2 = a2 - 1
                a1 = a1 + 1
                a5 = a5 + 1
        else:
            if ((a2 = = b1 - 1) and (a1 <= b2 - 1)):
                b3[a5] = input[a2, a1]
                a1 = a1 + 1
                a5 = a5 + 1
            elif (a1 = = a4):
                b3[a5] = input[a2, a1]
                if (a2 = = b1 - 1):
                    a1 = a1 + 1
                else:
                    a2 = a2 + 1
                a5 = a5 + 1
            elif ((a2 < b1 - 1) and (a1 > a4)):
                b3[a5] = input[a2, a1]
                a2 = a2 + 1
                a1 = a1 - 1
                a5 = a5 + 1
        if ((a2 = = b1 - 1) and (a1 == b2 - 1)):
            b3[a5] = input[a2, a1]
            break
    return b3
def fonk2(input, b1, b2):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b3 = np.zeros((b1, b2))
    a5 = 0
    while ((a2 < b1) and (a1 < b2)):
        if ((a1 + a2) % 2) == 0:
            if (a2 = = a3):
                b3[a2, a1] = input[a5]
                if (a1 = = b2):
                    a2 = a2 + 1
                else:
                    a1 = a1 + 1
                a5 = a5 + 1
            elif ((a1 = = b2 - 1) and (a2 < b1)):
                b3[a2, a1] = input[a5]
                a2 = a2 + 1
                a5 = a5 + 1
            elif ((a2 > a3) and (a1 < b2 - 1)):
                b3[a2, a1] = input[a5]
                a2 = a2 - 1
                a1 = a1 + 1
                a5 = a5 + 1
        else:
            if ((a2 = = b1 - 1) and (a1 <= b2 - 1)):
                b3[a2, a1] = input[a5]
                a1 = a1 + 1
                a5 = a5 + 1
            elif (a1 = = a4):
                b3[a2, a1] = input[a5]
                if (a2 = = b1 - 1):
                    a1 = a1 + 1
                else:
                    a2 = a2 + 1
                a5 = a5 + 1
            elif ((a2 < b1 - 1) and (a1 > a4)):
                b3[a2, a1] = input[a5]
                a2 = a2 + 1
                a1 = a1 - 1
                a5 = a5 + 1
        if ((a2 = = b1 - 1) and (a1 == b2 - 1)):
            b3[a2, a1] = input[a5]
            break
    return b3
b4 = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
b5 = fonk1(b4)
print("Zigzag b3:")
print(b5)
b6 = fonk2(b5, 3, 3)
print("\nInverse Zigzag b3:")
print(b6)