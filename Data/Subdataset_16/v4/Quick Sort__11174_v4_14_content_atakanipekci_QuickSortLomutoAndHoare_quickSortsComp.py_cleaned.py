def fonk1(b5, start, end):
    if len(b5) == 1:
        return b5
    elif start < end:
        b1 = fonk3(b5, start, end)
        fonk1(b5, start, b1 - 1)
        fonk1(b5, b1 + 1, end)
    return b5
def fonk2(b5):
    return fonk1(b5, 0, len(b5) - 1)
def fonk3(b5, start, end):
    b1 = b5[end]
    b2 = start - 1
    for b3 in range(start, end):
        if b5[b3] <= b1:
            b2 += 1
            b5[b2], b5[b3] = b5[b3], b5[b2]
    b5[b2 + 1], b5[end] = b5[end], b5[b2 + 1]
    return b2 + 1
def fonk4(b5, start, end):
    if len(b5) == 1:
        return b5
    if start < end:
        b1 = fonk5(b5, start, end)
        fonk4(b5, start, b1)
        fonk4(b5, b1 + 1, end)
    return b5
def fonk5(b5, start, end):
    b1 = b5[start]
    b2 = start - 1
    b3 = end + 1
    while True:
        b2 += 1
        while b5[b2] < b1:
            b2 += 1
        b3 -= 1
        while b5[b3] > b1:
            b3 -= 1
        if b2 >= b3:
            return b3
        b5[b2], b5[b3] = b5[b3], b5[b2]
def fonk6(b5):
    return fonk4(b5, 0, len(b5) - 1)
if b4 = = "__main__":
    b5 = [15, 4, 68, 24, 75, 16, 42]
    print("Original array:", b5)
    b6 = b5[:]
    b7 = fonk6(b6)
    print("Sorted array using Hoare partition:", b7)
    b6 = b5[:]
    b8 = fonk2(b6)
    print("Sorted array using Lomuto partition:", b8)