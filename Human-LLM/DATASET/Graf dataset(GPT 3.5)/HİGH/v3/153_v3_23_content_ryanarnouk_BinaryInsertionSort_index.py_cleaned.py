def fonk1(b5, b3, b1, end):
    if b1 = = end:
        return b1 + (b5[b1] <= b3)
    if b1 > end:
        return b1
    b2 = (b1 + end)
    if b5[b2] < b3:
        return fonk1(b5, b3, b2 + 1, end)
    elif b5[b2] > b3:
        return fonk1(b5, b3, b1, b2 - 1)
    else:
        return b2
def fonk2(b5):
    for i in range(1, len(b5)):
        b3 = b5[i]
        b4 = fonk1(b5, b3, 0, i - 1)
        b5 = b5[:b4] + [b3] + b5[b4:i] + b5[i + 1:]
    return b5
if b6 = = "__main__":
    print("Sorted array:")
    b7 = fonk2([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
    print(b7)