def fonk1(sender, start, current_sum, b2, b4):
    if start in b4:
        for x in b4[start]:
            b1 = current_sum + x[1]
            if b2[x[0] - 1] is None or b1 < b2[x[0] - 1]:
                b2[x[0] - 1] = b1
                b2 = fonk1(start, x[0], b1, b2, b4)
    return b2
def fonk2():
    b3 = [
        [3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85],
        [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15],
        [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31],
        [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]
    ]
    a1 = 5
    a2 = 5
    b4 = {}
    for u, v, w in b3:
        if u in b4:
            b4[u].append([v, w])
        else:
            b4[u] = [[v, w]]
    b2 = [None] * a1
    b2[a2 - 1] = 0
    b2 = fonk1(a2, a2, 0, b2, b4)
    if None not in b2:
        b5 = max(b2)
    else:
        b5 = -1
    print(b5)
if b6 = = "__main__":
    fonk2()