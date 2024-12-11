import copy
def fonk1(b6):
    b1 = []
    while len(b1) < len(b6):
        b2 = fonk2(b6, b1)
        b1.append(b2)
        for v in range(len(b6)):
            if b2 in b6[v]:
                b6[v].remove(b2)
    return b1
def fonk2(b6, b1):
    for v in range(len(b6)):
        if len(b6[v]) == 0 and v not in b1:
            return v
    return None
def fonk3(b6, b7):
    b3 = [0] * len(b6)
    b4 = fonk1(copy.deepcopy(b6))
    for node in b4:
        b5 = b7[node]
        for parent_node in b6[node]:
            if b5 < b3[parent_node] + b7[node]:
                b5 = b3[parent_node] + b7[node]
        b3[node] = b5
    return b3
b6 = [[3, 2, 1], [], [8, 5, 4, 3], [7, 6], [8, 6, 5], [7, 6], [9, 8], [9], [9], []]
b7 = [10] * len(b6)
print("Arrival time (b3) values are:", fonk3(b6, b7))