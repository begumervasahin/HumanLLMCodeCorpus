def fonk1(b3):
    b1 = b3[:]
    b2 = False
    while not b2:
        a1 = 0
        for i in range(len(b1) - 1):
            if b1[i] > b1[i + 1]:
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
                a1 += 1
        if a1 = = 0:
            b2 = True
    return b1
def fonk2():
    b3 = [4, 2, 7, 1, 9, 5, 3]
    b4 = fonk1(b3)
    print("Original list:", b3)
    print("Sorted list:", b4)
if b5 = = "__main__":
    fonk2()