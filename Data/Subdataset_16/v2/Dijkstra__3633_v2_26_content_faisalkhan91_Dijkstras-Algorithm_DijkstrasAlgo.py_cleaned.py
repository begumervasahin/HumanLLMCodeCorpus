
b1 = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
b2 = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
}
def fonk1(b1, b2, start):
    b3 = {node: None for node in b1}
    b4 = {}
    b5 = start
    a1 = 0
    b3[b5] = a1
    while b3:
        for neighbor, distance in b2[b5].items():
            if neighbor not in b3:
                continue
            b6 = a1 + distance
            if b3[neighbor] is None or b6 < b3[neighbor]:
                b3[neighbor] = b6
        b4[b5] = a1
        del b3[b5]
        if not b3:
            break
        b7 = [node for node in b3.items() if node[1] is not None]
        b5, a1 = sorted(b7, key=lambda x: x[1])[0]
    return b4
def fonk2():
    b8 = 'B'
    b9 = fonk1(b1, b2, b8)
    print(f"\nThe shortest path tree using Dijkstra's algorithm starting from node '{b8}':")
    print(b9)
if b10 = = "__main__":
    fonk2()