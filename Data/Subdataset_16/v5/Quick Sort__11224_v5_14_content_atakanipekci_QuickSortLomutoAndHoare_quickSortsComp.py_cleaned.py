def fonk1(b6):
    def fonk2(b6, start, end):
        b1 = b6[end]
        b2 = start - 1
        for b4 in range(start, end):
            if b6[b4] <= b1:
                b2 += 1
                b6[b2], b6[b4] = b6[b4], b6[b2]
        b6[b2 + 1], b6[end] = b6[end], b6[b2 + 1]
        return b2 + 1
    def fonk3(b6, start, end):
        if start < end:
            b3 = fonk2(b6, start, end)
            fonk3(b6, start, b3 - 1)
            fonk3(b6, b3 + 1, end)
    fonk3(b6, 0, len(b6) - 1)
    return b6
def fonk4(b6):
    def fonk5(b6, start, end):
        b1 = b6[start]
        b2 = start - 1
        b4 = end + 1
        while True:
            b2 += 1
            while b6[b2] < b1:
                b2 += 1
            b4 -= 1
            while b6[b4] > b1:
                b4 -= 1
            if b2 >= b4:
                return b4
            b6[b2], b6[b4] = b6[b4], b6[b2]
    def fonk6(b6, start, end):
        if start < end:
            b3 = fonk5(b6, start, end)
            fonk6(b6, start, b3)
            fonk6(b6, b3 + 1, end)
    fonk6(b6, 0, len(b6) - 1)
    return b6
if b5 = = "__main__":
    b6 = [15, 4, 68, 24, 75, 16, 42]
    print("Original array:", b6)
    b7 = b6[:]
    b8 = fonk4(b7)
    print("Sorted array using Hoare partition:", b8)
    b7 = b6[:]
    b9 = fonk1(b7)
    print("Sorted array using Lomuto partition:", b9)