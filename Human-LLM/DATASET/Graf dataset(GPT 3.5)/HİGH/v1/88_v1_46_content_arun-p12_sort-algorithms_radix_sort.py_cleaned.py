import common as c
def fonk1(b9, b1 = 0, desc=0):
    def fonk2(b2, b3):
        a1 = 0
        while b2:
            a1 += 1
            b2 = b2
        return a1
    def fonk3(b2, pos, b3 = 10):
        a1, b5, b4 = 0, 0, True
        while b4:
            a1 += 1
            b5 = b2 % b3
            b2 = b2
            if a1 > pos:
                b4 = False
        return b5
    def fonk4(pos, b3):
        b2 = len(b9)
        b6 = [[] for _ in range(b2)]
        for i in range(b2):
            b7 = fonk3(b9[i], pos, b3)
            b6[b7].append(b9[i])
            if b1 = = 2:
                print("    b6:", i, " :: ", b6)
        return [b6[x][y] for x in range(len(b6)) for y in range(len(b6[x]))]
    b3 = 10
    b8 = c.minimum(b9)[0]
    if b8:
        b9 = [x - b8 for x in b9]
    b10 = c.maximum(b9)[0]
    b11 = fonk2(b10, b3)
    for i in range(b11):
        b9 = fonk4(i, b3)
        if b1:
            print("Iteration", i + 1, ":", b9)
    if b8:
        b9 = [x + b8 for x in b9]
    if desc:
        b9 = b9[::-1]
    return b9
if b12 = = "__main__":
    b13 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", b13)
    b14 = fonk1(b13, b1=1, desc=0)
    print("Sorted Array:", b14)