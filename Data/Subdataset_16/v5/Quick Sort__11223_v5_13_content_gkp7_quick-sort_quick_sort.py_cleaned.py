def fonk1(b6):
    fonk2(b6, 0, len(b6) - 1)
def fonk2(b6, first, last):
    if first < last:
        b1 = fonk3(b6, first, last)
        fonk2(b6, first, b1 - 1)
        fonk2(b6, b1 + 1, last)
def fonk3(b6, first, last):
    b2 = b6[first]
    b3 = first + 1
    b4 = last
    while True:
        while b3 <= b4 and b6[b3] <= b2:
            b3 += 1
        while b4 >= b3 and b6[b4] >= b2:
            b4 -= 1
        if b4 < b3:
            break
        else:
            b6[b3], b6[b4] = b6[b4], b6[b3]
    b6[first], b6[b4] = b6[b4], b6[first]
    return b4
if b5 = = "__main__":
    b6 = [57, 26, 93, 77, 33, 44, 50, 20]
    fonk1(b6)
    print("Sorted list:", b6)