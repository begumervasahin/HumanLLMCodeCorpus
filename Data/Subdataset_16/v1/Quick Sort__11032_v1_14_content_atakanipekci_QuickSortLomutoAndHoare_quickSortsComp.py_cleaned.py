def fonk1(b6, start, end):
    if len(b6) == 1:
        return b6
    elif start < end:
        b1 = fonk3(b6, start, end)
        fonk1(b6, start, b1 - 1)
        fonk1(b6, b1 + 1, end)
    return b6
def fonk2(b6):
    return fonk1(b6, 0, len(b6) - 1)
def fonk3(b6, start, end):
    b2 = b6[end]
    b3 = start - 1
    for b4 in range(start, end):
        if b6[b4] <= b2:
            b3 += 1
            b6[b3], b6[b4] = b6[b4], b6[b3]
    b6[b3 + 1], b6[end] = b6[end], b6[b3 + 1]
    return b3 + 1
def fonk4(b6, start, end):
    if len(b6) == 1:
        return b6
    if start < end:
        b1 = fonk5(b6, start, end)
        fonk4(b6, start, b1)
        fonk4(b6, b1 + 1, end)
    return b6
def fonk5(b6, start, end):
    b2 = b6[start]
    b3 = start - 1
    b4 = end + 1
    while True:
        b3 += 1
        while b6[b3] < b2:
            b3 += 1
        b4 -= 1
        while b6[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        b6[b3], b6[b4] = b6[b4], b6[b3]
def fonk6(b6):
    return fonk4(b6, 0, len(b6) - 1)
if b5 = = "__main__":
    b6 = [15, 4, 68, 24, 75, 16, 42]
    b7 = b6.copy()
    b8 = fonk6(b7)
    print("Sorted using Hoare partition:", b8)
    b9 = b6.copy()
    b10 = fonk2(b9)
    print("Sorted using Lomuto partition:", b10)