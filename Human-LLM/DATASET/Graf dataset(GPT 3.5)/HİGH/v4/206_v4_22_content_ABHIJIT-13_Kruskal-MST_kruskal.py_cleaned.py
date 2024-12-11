def fonk1(b1):
    if b7[b1] == b1:
        return b1
    else:
        while b7[b1] != b1:
            b7[b1] = b7[b7[b1]]
            b1 = b7[b1]
        return b1
def fonk2(u, v):
    b2 = fonk1(u)
    b3 = fonk1(v)
    b7[b3] = b7[b2]
def fonk3(b6):
    global b7
    a1 = 0
    for edge in b6:
        u, v, b4 = edge
        if fonk1(u) != fonk1(v):
            a1 += b4
            fonk2(u, v)
    return a1
V, b5 = map(int, input().split())
b6 = []
for i in range(b5):
    b6.append(list(map(int, input().split())))
b6 = sorted(b6, key=lambda x: x[2])
b7 = list(range(V + 1))
print(fonk3(b6)))