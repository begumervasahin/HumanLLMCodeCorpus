def fonk1(b6):
    fonk2(b6, 0, len(b6) - 1)
def fonk2(b6, low, high):
    if low < high:
        b1 = fonk3(b6, low, high)
        fonk2(b6, low, b1 - 1)
        fonk2(b6, b1 + 1, high)
def fonk3(b6, low, high):
    b2 = b6[low]
    b3 = low + 1
    b4 = high
    b5 = False
    while not b5:
        while b3 <= b4 and b6[b3] <= b2:
            b3 += 1
        while b6[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            b6[b3], b6[b4] = b6[b4], b6[b3]
    b6[low], b6[b4] = b6[b4], b6[low]
    return b4
b6 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b6)
print(b6)