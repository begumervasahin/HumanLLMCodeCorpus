
b1 = {
    'A': {'RS1', 'C', 'E'},
    'B': {'E', 'D'},
    'C': {'A', 'B', 'RS2'},
    'D': {'B', 'F', 'K', 'RS3'},
    'E': {'A', 'B'},
    'F': {'D', 'G'},
    'G': {'H', 'F', 'I'},
    'H': {'G'},
    'I': {'G', 'J'},
    'J': {'I'},
    'K': {'D', 'L', 'M'},
    'L': {'RS2', 'K'},
    'M': {'K'},
    'RS1': {'A'},
    'RS2': {'C', 'L'},
    'RS3': {'D'}
}
def fonk1(graph, b10):
    b2 = [[b10]]
    b3 = {'RS1', 'RS2', 'RS3'}
    b4 = set()
    while b2:
        b5 = b2.pop(0)
        b6 = b5[-1]
        if b6 in b3:
            return b5
        if b6 not in b4:
            for neighbor in graph.get(b6, []):
                b7 = b5 + [neighbor]
                b2.append(b7)
            b4.add(b6)
    print("Hospital not found")
    return None
def fonk2(graph, b10):
    b8 = [[b10]]
    b3 = {'RS1', 'RS2', 'RS3'}
    b4 = set()
    while b8:
        b5 = b8.pop()
        b6 = b5[-1]
        if b6 in b3:
            return b5
        if b6 not in b4:
            for neighbor in graph.get(b6, []):
                b7 = b5 + [neighbor]
                b8.append(b7)
            b4.add(b6)
    print("Hospital not found")
    return None
if b9 = = "__main__":
    b10 = input("Enter the starting position: ").strip()
    print("BFS searching for the nearest hospital from:", b10)
    b11 = fonk1(b1, b10)
    if b11:
        print("BFS Path:", " -> ".join(b11))
    print("\nDFS searching for the nearest hospital from:", b10)
    b12 = fonk2(b1, b10)
    if b12:
        print("DFS Path:", " -> ".join(b12))