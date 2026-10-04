def fonk1(b6, b4, b2, b3):
    while b2 <= b3:
        b1 = (b2 + b3)
        if b6[b1] < b4:
            b2 = b1 + 1
        elif b6[b1] > b4:
            b3 = b1 - 1
        else:
            return b1
    return b2
def fonk2(b6):
    for i in range(1, len(b6)):
        b4 = b6[i]
        b5 = fonk1(b6, b4, 0, i - 1)
        b6 = b6[:b5] + [b4] + b6[b5:i] + b6[i+1:]
    return b6
if b7 = = "__main__":
    b6 = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    b8 = fonk2(b6)
    print("Sorted array:")
    print(b8)