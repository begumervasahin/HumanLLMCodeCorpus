def fonk1(pqueue):
    b1 = float('inf')
    b2 = None
    for key, value in pqueue.items():
        if value < b1:
            b1 = value
            b2 = key
    if b2 is not None:
        del pqueue[b2]
    return b2
def fonk2(b9, start):
    b3 = {}
    b4 = {}
    b5 = {}
    for node in b9:
        b4[node] = float('inf')
        b5[node] = None
        b3[node] = b4[node]
    b4[start] = 0
    b3[start] = b4[start]
    while b3:
        b6 = fonk1(b3)
        for neighbor, weight in b9.get(b6, {}).items():
            b7 = b4[b6] + weight
            if b7 < b4[neighbor]:
                b4[neighbor] = b7
                b5[neighbor] = b6
                b3[neighbor] = b7
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
    print("Shortest b4 from start node 0 to all other nodes:")
    for node, distance in b4.items():
        print(f"Node {node}: b10 = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in b5.items():
        print(f"Node {node}: b11 = {predecessor}")