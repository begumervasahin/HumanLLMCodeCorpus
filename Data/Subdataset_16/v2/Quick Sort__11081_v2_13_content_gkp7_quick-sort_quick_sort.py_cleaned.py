def fonk1(b7):
    fonk2(b7, 0, len(b7) - 1)
def fonk2(b7, first, last):
    if first < last:
        b1 = fonk3(b7, first, last)
        fonk2(b7, first, b1 - 1)
        fonk2(b7, b1 + 1, last)
def fonk3(b7, first, last):
    b2 = b7[first]
    b3 = first + 1
    b4 = last
    b5 = False
    while not b5:
        while b3 <= b4 and b7[b3] <= b2:
            b3 = b3 + 1
        while b7[b4] >= b2 and b4 >= b3:
            b4 = b4 - 1
        if b4 < b3:
            b5 = True
        else:
            b7[b3], b7[b4] = b7[b4], b7[b3]
    b7[first], b7[b4] = b7[b4], b7[first]
    return b4
if b6 = = "__main__":
    b7 = [57, 26, 93, 77, 33, 44, 50, 20]
    fonk1(b7)
    print("Sorted list:", b7)