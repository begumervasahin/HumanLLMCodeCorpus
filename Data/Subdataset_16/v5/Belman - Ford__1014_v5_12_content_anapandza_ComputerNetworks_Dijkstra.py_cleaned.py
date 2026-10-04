def fonk1(b4):
    b1 = min(b4, key=b4.get)
    del b4[b1]
    return b1
def fonk2(b7, start):
    b2 = {node: float('inf') for node in b7}
    b3 = {node: None for node in b7}
    b2[start] = 0
    b4 = {node: b2[node] for node in b7}
    while b4:
        b5 = fonk1(b4)
        for v, weight in b7[b5].items():
            b6 = b2[b5] + weight
            if b6 < b2[v]:
                b4[v] = b6
                b2[v] = b6
                b3[v] = b5
    return b2, b3
def fonk3(b2, b3):
    print("Shortest distances from the start node to all other nodes:")
    for node, distance in b2.items():
        print(f"Node {node}: {distance}")
    print("\nPaths from the start node to all other nodes (predecessors of nodes):")
    for node, predecessor in b3.items():
        print(f"Node {node}: {predecessor}")
def fonk4():
    b7 = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    a1 = 0
    b2, b3 = fonk2(b7, a1)
    fonk3(b2, b3)
if b8 = = "__main__":
    fonk4()