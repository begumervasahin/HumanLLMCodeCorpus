import statistics
def fonk1(b11, first, last):
    b1 = b11[first]
    b2 = b11[last]
    b3 = (first + last)
    b4 = statistics.median([b1, b11[b3], b2])
    if b4 = = b1:
        b5 = first
    elif b4 = = b2:
        b5 = last
    else:
        b5 = b3
    b11[last], b11[b5] = b11[b5], b11[last]
    b6 = b11[last]
    b7 = first
    b8 = last - 1
    while True:
        while b7 <= b8 and b11[b7] <= b6:
            b7 += 1
        while b7 <= b8 and b11[b8] >= b6:
            b8 -= 1
        if b8 < b7:
            break
        else:
            b11[b7], b11[b8] = b11[b8], b11[b7]
    b11[first], b11[b8] = b11[b8], b11[first]
    return b8
def fonk2(b11, first, last):
    if first < last:
        b9 = fonk1(b11, first, last)
        fonk2(b11, first, b9 - 1)
        fonk2(b11, b9 + 1, last)
if b10 = = "__main__":
    b11 = [56, 26, 93, 17, 31, 44]
    b12 = len(b11)
    fonk2(b11, 0, b12 - 1)
    print(b11)