def fonk1(current_node, current_sum, b4, b3):
    if current_node in b3:
        for neighbor, weight in b3[current_node]:
            b1 = current_sum + weight
            if b4[neighbor - 1] is None or b1 < b4[neighbor - 1]:
                b4[neighbor - 1] = b1
                fonk1(neighbor, b1, b4, b3)
    return b4
def fonk2():
    b2 = [
        [3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85],
        [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15],
        [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31],
        [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]
    ]
    a1 = 5
    a2 = 5
    b3 = {}
    for u, v, w in b2:
        if u in b3:
            b3[u].append((v, w))
        else:
            b3[u] = [(v, w)]
    b4 = [None] * a1
    b4[a2 - 1] = 0
    b4 = fonk1(a2, 0, b4, b3)
    if None not in b4:
        b5 = max(b4)
    else:
        b5 = -1
    print(b5)
if b6 = = "__main__":
    fonk2()