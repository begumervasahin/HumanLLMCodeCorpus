a1 = 0
def fonk1(b6, start, end):
    global a1
    b1 = b6[start]
    b2 = start + 1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and b6[b2] <= b1:
            b2 = b2 + 1
        while b6[b3] >= b1 and b3 >= b2:
            b3 = b3 - 1
        if b3 < b2:
            b4 = True
        else:
            b6[b2], b6[b3] = b6[b3], b6[b2]
    b6[start], b6[b3] = b6[b3], b6[start]
    return b3
def fonk2(b6, start, end):
    global a1
    if start < end:
        a1 += end - start
        b5 = fonk1(b6, start, end)
        a1 += abs(start - (b5 - 1))
        fonk2(b6, start, b5 - 1)
        a1 += abs((b5 + 1) - end)
        fonk2(b6, b5 + 1, end)
    return b6
def fonk3():
    global a1
    b6 = [int(x) for x in open("list.txt", "r").readlines()]
    b7 = fonk2(b6, 0, len(b6) - 1)
    print(b7)
if b8 = = "__main__":
    fonk3()
    print(a1)