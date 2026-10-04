def fonk1(b8, a1, b3):
    b1 = b8[b3]
    b2 = a1 - 1
    for j in range(a1, b3):
        if b8[j] <= b1:
            b2 += 1
            b8[b2], b8[j] = b8[j], b8[b2]
    b8[b2 + 1], b8[b3] = b8[b3], b8[b2 + 1]
    return b2 + 1
def fonk2(b8):
    a1 = 0
    b3 = len(b8) - 1
    b4 = b3 - a1 + 1
    b5 = [0] * b4
    a2 = -1
    a2 += 1
    b5[a2] = a1
    a2 += 1
    b5[a2] = b3
    while a2 >= 0:
        b3 = b5[a2]
        a2 -= 1
        a1 = b5[a2]
        a2 -= 1
        b6 = fonk1(b8, a1, b3)
        if b6 - 1 > a1:
            a2 += 1
            b5[a2] = a1
            a2 += 1
            b5[a2] = b6 - 1
        if b6 + 1 < b3:
            a2 += 1
            b5[a2] = b6 + 1
            a2 += 1
            b5[a2] = b3
if b7 = = "__main__":
    b8 = [4, 3, 5, 2, 1, 3, 2, 3]
    print("Original array is:")
    print(b8)
    fonk2(b8)
    print("Sorted array is:")
    print(b8)