import statistics
def fonk1(b10, first, last):
    b1 = b10[first]
    b2 = (first + last)
    b3 = b10[last]
    b4 = statistics.median([b1, b10[b2], b3])
    if b4 = = b1:
        return first
    elif b4 = = b3:
        return last
    else:
        return b2
def fonk2(b10, first, last):
    b5 = fonk1(b10, first, last)
    b10[b5], b10[last] = b10[last], b10[b5]
    b6 = b10[last]
    b7 = first
    b8 = last - 1
    while True:
        while b7 <= b8 and b10[b7] <= b6:
            b7 += 1
        while b7 <= b8 and b10[b8] >= b6:
            b8 -= 1
        if b7 > b8:
            break
        b10[b7], b10[b8] = b10[b8], b10[b7]
    b10[b7], b10[last] = b10[last], b10[b7]
    return b7
def fonk3(b10, first, last):
    if first < last:
        b5 = fonk2(b10, first, last)
        fonk3(b10, first, b5 - 1)
        fonk3(b10, b5 + 1, last)
if b9 = = "__main__":
    b10 = [56, 26, 93, 17, 31, 44]
    fonk3(b10, 0, len(b10) - 1)
    print("Sorted array:", b10)