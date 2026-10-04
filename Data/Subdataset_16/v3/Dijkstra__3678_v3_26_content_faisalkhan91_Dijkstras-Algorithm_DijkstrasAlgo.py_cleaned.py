
b1 = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
b2 = {
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'B': {'A': 5, 'D': 1, 'G': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'D': {'A': 3, 'B': 1, 'E': 1, 'G': 1},
    'E': {'A': 12, 'C': 1, 'D': 1, 'F': 2},
    'F': {'A': 5, 'C': 16, 'E': 2},
    'G': {'B': 2, 'C': 2, 'D': 1}
}
def fonk1(b1, b2, start):
    b3 = {node: float('inf') for node in b1}
    b4 = {}
    b5 = start
    a1 = 0
    b3[b5] = a1
    while b3:
        for neighbor, distance in b2[b5].items():
            b6 = a1 + distance
            if b6 < b3[neighbor]:
                b3[neighbor] = b6
        b4[b5] = a1
        del b3[b5]
        if not b3:
            break
        b5, a1 = min(b3.items(), key=lambda x: x[1])
    return b4
def fonk2():
    b7 = 'B'
    b8 = fonk1(b1, b2, b7)
    print(f"\nThe shortest path tree using Dijkstra's algorithm starting from node '{b7}':")
    print(b8)
if b9 = = "__main__":
    fonk2()