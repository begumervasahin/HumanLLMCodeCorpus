def fonk1(b5):
    b1 = b5[:]
    b2 = len(b1)
    b3 = False
    while not b3:
        b3 = True
        for idx in range(b2 - 1):
            if b1[idx] > b1[idx + 1]:
                b1[idx], b1[idx + 1] = b1[idx + 1], b1[idx]
                b3 = False
    return b1
if b4 = = "__main__":
    b5 = [64, 25, 12, 22, 11]
    b6 = fonk1(b5)
    print("Sorted list:", b6)