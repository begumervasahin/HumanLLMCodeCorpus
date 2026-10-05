def fonk1(b4):
    def fonk2(b4, start, end):
        b1 = b4[end]
        b2 = start - 1
        for b3 in range(start, end):
            if b4[b3] <= b1:
                b2 += 1
                b4[b2], b4[b3] = b4[b3], b4[b2]
        b4[b2 + 1], b4[end] = b4[end], b4[b2 + 1]
        return b2 + 1
    def fonk3(b4, start, end):
        if start < end:
            b1 = fonk2(b4, start, end)
            fonk3(b4, start, b1 - 1)
            fonk3(b4, b1 + 1, end)
    fonk3(b4, 0, len(b4) - 1)
    return b4
def fonk4(b4):
    def fonk5(b4, start, end):
        b1 = b4[start]
        b2 = start - 1
        b3 = end + 1
        while True:
            b2 += 1
            while b4[b2] < b1:
                b2 += 1
            b3 -= 1
            while b4[b3] > b1:
                b3 -= 1
            if b2 >= b3:
                return b3
            b4[b2], b4[b3] = b4[b3], b4[b2]
    def fonk6(b4, start, end):
        if start < end:
            b1 = fonk5(b4, start, end)
            fonk6(b4, start, b1)
            fonk6(b4, b1 + 1, end)
    fonk6(b4, 0, len(b4) - 1)
    return b4
b4 = [15, 4, 68, 24, 75, 16, 42]
b5 = fonk4(b4.copy())
b6 = fonk1(b4.copy())
print("Hoare quicksort result:", b5)
print("Lomuto quicksort result:", b6)