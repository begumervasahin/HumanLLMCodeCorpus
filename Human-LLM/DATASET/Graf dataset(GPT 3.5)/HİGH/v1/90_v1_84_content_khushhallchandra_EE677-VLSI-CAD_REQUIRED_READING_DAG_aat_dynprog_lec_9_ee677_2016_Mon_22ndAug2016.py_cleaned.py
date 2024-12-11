import copy
def fonk1(fanin_copy):
    b1 = []
    while len(b1) < len(fanin_copy):
        b2 = fonk2(fanin_copy, b1)
        b1.append(b2)
        for v in range(len(fanin_copy)):
            if b2 in fanin_copy[v]:
                fanin_copy[v].remove(b2)
    return b1
def fonk2(fanin_copy, b1):
    for v in range(len(fanin_copy)):
        if len(fanin_copy[v]) == 0 and v not in b1:
            return v
    return None
def fonk3(b6, b7):
    b3 = [0 for l in b6]
    b4 = fonk1(copy.deepcopy(b6))
    for v in b4:
        b5 = b7[v]
        for u in b6[v]:
            if b5 < b3[u] + b7[v]:
                b5 = b3[u] + b7[v]
        b3[v] = b5
    return b3
b6 = [[3, 2, 1], [], [8, 5, 4, 3], [7, 6], [8, 6, 5], [7, 6], [9, 8], [9], [9], []]
b7 = [10 for l in b6]
print("b3 values are ", fonk3(b6, b7))