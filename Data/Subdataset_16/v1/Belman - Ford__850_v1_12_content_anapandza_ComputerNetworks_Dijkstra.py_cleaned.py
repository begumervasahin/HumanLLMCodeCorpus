def fonk1(b3):
    b1 = float('inf')
    b2 = None
    for key in b3:
        if b3[key] < b1:
            b1 = b3[key]
            b2 = key
    del b3[b2]
    return b2
def fonk2(b9, start):
    b3 = {}
    b4 = {}
    b5 = {}
    for v in b9:
        b4[v] = float('inf')
        b5[v] = None
    b4[start] = 0
    for v in b9:
        b3[v] = b4[v]
    while b3:
        b6 = fonk1(b3)
        for v in b9[b6]:
            b7 = b9[b6][v]
            b8 = b4[b6] + b7
            if b8 < b4[v]:
                b3[v] = b8
                b4[v] = b8
                b5[v] = b6
    return b4, b5
def fonk3():
    b9 = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    a1 = 0
    b4, b5 = fonk2(b9, a1)
    print("Shortest distance from start node 0 to all other nodes is:")
    for v in b4:
        print(f"{v} = {b4[v]}")
    print("Paths from start node to all other nodes (predecessors of nodes):")
    for v in b5:
        print(f"{v} = {b5[v]}")
if b10 = = "__main__":
    fonk3()