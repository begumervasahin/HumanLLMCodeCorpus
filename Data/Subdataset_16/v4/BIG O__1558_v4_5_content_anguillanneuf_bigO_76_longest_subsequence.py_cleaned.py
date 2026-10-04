
def fonk1(b9):
    if len(b9) < 2:
        return b9
    b1 = [None] * len(b9)
    b2 = [None] * len(b9)
    a1 = 1
    b1[0] = 0
    for i in range(1, len(b9)):
        if b9[i] > b9[b1[a1 - 1]]:
            b3 = a1
        else:
            b6, b4 = 0, a1 - 1
            while b6 + 1 < b4:
                b5 = (b6 + b4)
                if b9[i] > b9[b1[b5]]:
                    b6 = b5 + 1
                else:
                    b4 = b5
            b3 = b6
        b2[i] = b1[b3 - 1]
        b1[b3] = i
        a1 = max(a1, b3 + 1)
    b7 = []
    b8 = b1[a1 - 1]
    for _ in range(a1):
        b7.append(b9[b8])
        b8 = b2[b8]
    return b7[::-1]
b9 = [30, 10, 20, 50, 40, 60]
print(fonk1(b9))
def fonk2(b9):
    if not b9:
        return []
    b10 = [[] for _ in range(len(b9))]
    b11 = []
    for i in range(len(b9)):
        for b3 in range(i):
            if b9[i] > b9[b3]:
                if len(b10[b3]) + 1 > len(b10[i]):
                    b10[i] = b10[b3] + [b9[i]]
                    b11 = max(b10[i], b11, key=len)
        if not b10[i]:
            b10[i] = [b9[i]]
            b11 = max(b10[i], b11, key=len)
    return b11
print(fonk2([80, 90, 91, 81, 82, 83, 74, 85]))