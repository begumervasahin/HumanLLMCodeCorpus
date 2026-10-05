def fonk1(b5, start, end):
    b1 = b5[start]
    b2 = start + 1
    b3 = end
    while True:
        while b2 <= b3 and b5[b2] <= b1:
            b2 += 1
        while b5[b3] >= b1 and b3 >= b2:
            b3 -= 1
        if b3 < b2:
            break
        else:
            b5[b2], b5[b3] = b5[b3], b5[b2]
    b5[start], b5[b3] = b5[b3], b5[start]
    return b3
def fonk2(b5, start, end):
    global a1
    if start < end:
        a1 += end - start
        b4 = fonk1(b5, start, end)
        a1 += abs(start - (b4 - 1))
        fonk2(b5, start, b4 - 1)
        a1 += abs((b4 + 1) - end)
        fonk2(b5, b4 + 1, end)
    return b5
def fonk3():
    global a1
    a1 = 0
    b5 = [int(x) for x in open("list.txt", "r").readlines()]
    b6 = fonk2(b5, 0, len(b5) - 1)
    print(b6)
if b7 = = "__main__":
    fonk3()
    print(a1)