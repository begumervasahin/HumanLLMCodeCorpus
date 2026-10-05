def fonk1(b1):
    if b9[b1] == b1:
        return b1
    else:
        while b9[b1] != b1:
            b9[b1] = b9[b9[b1]]
            b1 = b9[b1]
        return b1
def fonk2(b4, b5):
    b2 = fonk1(b4)
    b3 = fonk1(b5)
    b9[b5] = b9[b4]
def fonk3(b8):
    global b9
    a1 = 0
    for edge in b8:
        b4 = edge[0]
        b5 = edge[1]
        b6 = edge[2]
        if fonk1(b4) != fonk1(b5):
            a1 += b6
            fonk2(b4, b5)
    return a1
V, b7 = map(int, input().split())
b8 = []
for i in range(b7):
    b8.append(list(map(int, input().split())))
b8 = sorted(b8, key=lambda x: x[2])
b9 = list(range(V + 1))
print(fonk3(b8))