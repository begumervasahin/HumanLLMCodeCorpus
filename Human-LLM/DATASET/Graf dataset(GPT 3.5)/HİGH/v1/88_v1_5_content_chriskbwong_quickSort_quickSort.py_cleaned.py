def fonk1(b8, b6, b5):
    b1 = b6 - 1
    b2 = b8[b5]
    for j in range(b6, b5):
        if b8[j] <= b2:
            b1 = b1 + 1
            b8[b1], b8[j] = b8[j], b8[b1]
    b8[b1 + 1], b8[b5] = b8[b5], b8[b1 + 1]
    return b1 + 1
def fonk2(b8, b6, b5):
    b3 = b5 - b6 + 1
    b4 = [0] * (b3)
    a1 = -1
    a1 = a1 + 1
    b4[a1] = b6
    a1 = a1 + 1
    b4[a1] = b5
    while a1 >= 0:
        b5 = b4[a1]
        a1 = a1 - 1
        b6 = b4[a1]
        a1 = a1 - 1
        b7 = fonk1(b8, b6, b5)
        if b7 - 1 > b6:
            a1 = a1 + 1
            b4[a1] = b6
            a1 = a1 + 1
            b4[a1] = b7 - 1
        if b7 + 1 < b5:
            a1 = a1 + 1
            b4[a1] = b7 + 1
            a1 = a1 + 1
            b4[a1] = b5
b8 = [4, 3, 5, 2, 1, 3, 2, 3]
b9 = len(b8)
fonk2(b8, 0, b9 - 1)
print("Sorted array is:")
for b1 in b8:
    print(b1, b10 = " ")