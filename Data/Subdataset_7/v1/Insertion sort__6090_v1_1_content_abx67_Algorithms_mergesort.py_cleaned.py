def fonk1(b7, b1, b6, b5):
    if b1 = = b5 == b6:
        return
    b2 = [0] * (b5 - b1 + 1)
    b3 = [0] * (b6 - b5)
    for i in range(0, b5 - b1 + 1):
        b2[i] = b7[i + b1]
    for i in range(0, b6 - b5):
        b3[i] = b7[i + b5 + 1]
    b4 = b1
    a1 = 0
    for i in range(0, len(b2)):
        while a1 < len(b3) and b2[i] > b3[a1]:
            b7[b4] = b3[a1]
            a1 += 1
            b4 += 1
        b7[b4] = b2[i]
        b4 += 1
    while a1 < len(b3):
        b7[b4] = b3[a1]
        a1 += 1
        b4 += 1
def fonk2(b7, b1, b6):
    b5 = b1 + round((b6 - b1) / 2)
    if b6 = = b1:
        return
    elif (b6 - b1) == 1:
        fonk1(b7, b1, b6, b5)
    else:
        fonk2(b7, b1, b5)
        fonk2(b7, b5 + 1, b6)
    fonk1(b7, b1, b6, b5)
b7 = [38, 27, 43, 3, 9, 82, 10]
fonk2(b7, 0, len(b7) - 1)
print("Sorted array:", b7)