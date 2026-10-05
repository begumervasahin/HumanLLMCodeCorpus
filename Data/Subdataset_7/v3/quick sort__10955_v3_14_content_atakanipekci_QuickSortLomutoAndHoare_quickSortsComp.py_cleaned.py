def fonk1(b5):
    return fonk2(b5, 0, len(b5) - 1)
def fonk2(b5, start, end):
    if start < end:
        b1 = fonk3(b5, start, end)
        fonk2(b5, start, b1 - 1)
        fonk2(b5, b1 + 1, end)
    return b5
def fonk3(b5, start, end):
    b2 = b5[end]
    b3 = start - 1
    for b4 in range(start, end):
        if b5[b4] <= b2:
            b3 += 1
            b5[b3], b5[b4] = b5[b4], b5[b3]
    b5[b3 + 1], b5[end] = b5[end], b5[b3 + 1]
    return b3 + 1
def fonk4(b5):
    return fonk5(b5, 0, len(b5) - 1)
def fonk5(b5, start, end):
    if start < end:
        b1 = fonk6(b5, start, end)
        fonk5(b5, start, b1)
        fonk5(b5, b1 + 1, end)
    return b5
def fonk6(b5, start, end):
    b2 = b5[start]
    b3, b4 = start - 1, end + 1
    while True:
        b3 += 1
        while b5[b3] < b2:
            b3 += 1
        b4 -= 1
        while b5[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        b5[b3], b5[b4] = b5[b4], b5[b3]
b5 = [15, 4, 68, 24, 75, 16, 42]
b6 = fonk4(b5.copy())
print("Sorted using Hoare's partition scheme:", b6)
b7 = fonk1(b5.copy())
print("Sorted using Lomuto's partition scheme:", b7)