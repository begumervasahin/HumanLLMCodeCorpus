def fonk1(b1, b5):
    if b5[b1] == b1:
        return b1
    else:
        while b5[b1] != b1:
            b5[b1] = b5[b5[b1]]
            b1 = b5[b1]
        return b1
def fonk2(u, v, b5):
    b2 = fonk1(u, b5)
    b3 = fonk1(v, b5)
    b5[b3] = b5[b2]
def fonk3(V, b7, b4):
    a1 = 0
    b4 = sorted(b4, key=lambda x: x[2])
    b5 = list(range(V + 1))
    for u, v, weight in b4:
        if fonk1(u, b5) != fonk1(v, b5):
            a1 += weight
            fonk2(u, v, b5)
    return a1
if b6 = = "__main__":
    V, b7 = map(int, input().split())
    b4 = [list(map(int, input().split())) for _ in range(b7)]
    print(fonk3(V, b7, b4)))