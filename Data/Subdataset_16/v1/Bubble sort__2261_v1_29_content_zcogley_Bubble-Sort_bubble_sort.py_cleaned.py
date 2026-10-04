def fonk1(b5):
    b1 = b5[:]
    b2 = False
    while not b2:
        a1 = 0
        a2 = 0
        b3 = len(b1) if len(b1) % 2 == 0 else len(b1) - 1
        while a1 < b3 - 1:
            if b1[a1] > b1[a1 + 1]:
                b1[a1], b1[a1 + 1] = b1[a1 + 1], b1[a1]
                a2 += 1
            a1 += 1
        if a2 = = 0:
            b2 = True
    return b1
if b4 = = "__main__":
    b5 = [64, 25, 12, 22, 11]
    b6 = fonk1(b5)
    print("Sorted list:", b6)