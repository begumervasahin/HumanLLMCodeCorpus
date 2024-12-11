def fonk1(b6):
    b1 = b6[:]
    b2 = False
    while not b2:
        a1 = 0
        a2 = 0
        b3 = len(b1) if len(b1) % 2 == 0 else len(b1) - 1
        while a1 < b3:
            b4 = b1[a1]
            b5 = b1[a1 + 1]
            if b4 > b5:
                b1[a1], b1[a1 + 1] = b5, b4
                a2 += 1
            a1 += 1
        if a2 = = 0:
            b2 = True
    return b1
def fonk2():
    b6 = [4, 2, 7, 1, 9, 5, 3]
    b7 = fonk1(b6)
    print("Original list:", b6)
    print("Sorted list:", b7)
if b8 = = "__main__":
    fonk2()