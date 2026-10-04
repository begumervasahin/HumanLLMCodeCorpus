def fonk1(b9, b6, b5):
    b1 = b9[b5]
    b2 = b6 - 1
    for j in range(b6, b5):
        if b9[j] <= b1:
            b2 += 1
            b9[b2], b9[j] = b9[j], b9[b2]
    b9[b2 + 1], b9[b5] = b9[b5], b9[b2 + 1]
    return b2 + 1
def fonk2(b9, b6, b5):
    b3 = b5 - b6 + 1
    b4 = [0] * b3
    a1 = -1
    a1 += 1
    b4[a1] = b6
    a1 += 1
    b4[a1] = b5
    while a1 >= 0:
        b5 = b4[a1]
        a1 -= 1
        b6 = b4[a1]
        a1 -= 1
        b7 = fonk1(b9, b6, b5)
        if b7 - 1 > b6:
            a1 += 1
            b4[a1] = b6
            a1 += 1
            b4[a1] = b7 - 1
        if b7 + 1 < b5:
            a1 += 1
            b4[a1] = b7 + 1
            a1 += 1
            b4[a1] = b5
if b8 = = "__main__":
    b9 = [4, 3, 5, 2, 1, 3, 2, 3]
    b10 = len(b9)
    fonk2(b9, 0, b10 - 1)
    print("Sorted array is:")
    for element in b9:
        print(element, b11 = " ")