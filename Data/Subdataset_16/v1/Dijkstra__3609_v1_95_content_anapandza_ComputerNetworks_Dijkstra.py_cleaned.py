def fonk1(b3):
    b1 = float('inf')
    b2 = None
    for key, value in b3.items():
        if value < b1:
            b1 = value
            b2 = key
    if b2 is not None:
        del b3[b2]
    return b2
def fonk2(b9, start):
    b3 = {}
    b4 = {}
    b5 = {}
    for v in b9:
        b4[v] = float('inf')
        b5[v] = None
        b3[v] = b4[v]
    b4[start] = 0
    b3[start] = b4[start]
    while b3:
        b6 = fonk1(b3)
        for v, w in b9.get(b6, {}).items():
            b7 = b4[b6] + w
            if b7 < b4[v]:
                b4[v] = b7
                b5[v] = b6
                b3[v] = b7
    return b4, b5
if b8 = = '__main__':
    b9 = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    b4, b5 = fonk2(b9, 0)
    print("Shortest distance from start node 0 to all other nodes:")
    for v, d in b4.items():
        print(f"Node {v}: b10 = {d}")
    print("\nPredecessors of nodes in the shortest paths from start node 0:")
    for v, p in b5.items():
        print(f"Node {v}: b11 = {p}")