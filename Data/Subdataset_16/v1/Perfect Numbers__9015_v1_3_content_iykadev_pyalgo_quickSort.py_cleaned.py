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
    b5 = False
    while not b5:
        while b3 <= b4 and b6[b3] <= b2:
            b3 = b3 + 1
        while b6[b4] >= b2 and b4 >= b3:
            b4 = b4 - 1
        if b4 < b3:
            b5 = True
        else:
            b6[b3], b6[b4] = b6[b4], b6[b3]
    b6[first], b6[b4] = b6[b4], b6[first]
    return b4
b6 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b6)
print(b6)