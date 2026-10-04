def fonk1(b5):
    fonk2(b5, 0, len(b5) - 1)
def fonk2(b5, first, last):
    if first < last:
        b1 = fonk3(b5, first, last)
        fonk2(b5, first, b1 - 1)
        fonk2(b5, b1 + 1, last)
def fonk3(b5, first, last):
    b2 = b5[first]
    b3 = first + 1
    b4 = last
    while True:
        while b3 <= b4 and b5[b3] <= b2:
            b3 += 1
        while b3 <= b4 and b5[b4] >= b2:
            b4 -= 1
        if b4 < b3:
            break
        else:
            b5[b3], b5[b4] = b5[b4], b5[b3]
    b5[first], b5[b4] = b5[b4], b5[first]
    return b4
b5 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b5)
print(b5)