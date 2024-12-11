import common as c
def fonk1(b10, b1 = 0, desc=0):
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
        b6 = len(b10)
        b7 = [[] for _ in range(b6)]
        for i in range(b6):
            b8 = fonk3(b10[i], pos, b3)
            b7[b8].append(b10[i])
            if b1 = = 2:
                print("    Bucket:", i, " :: ", b7)
        return [b7[x][y] for x in range(len(b7)) for y in range(len(b7[x]))]
    b3 = 10
    b9 = c.minimum(b10)[0]
    if b9:
        b10 = [x - b9 for x in b10]
    b11 = c.maximum(b10)[0]
    b12 = fonk2(b11, b3)
    for i in range(b12):
        b10 = fonk4(i, b3)
        if b1:
            print("Iteration", i + 1, ":", b10)
    if b9:
        b10 = [x + b9 for x in b10]
    if desc:
        b10 = b10[::-1]
    return b10