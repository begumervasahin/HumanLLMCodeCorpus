def fonk1(graph, start):
    b1 = [[start]]
    b2 = {'RS1', 'RS2', 'RS3'}
    b3 = set()
    while b1:
        b4 = b1.pop(0)
        b5 = b4[-1]
        if b5 in b2:
            return b4
        if b5 not in b3:
            for neighbor in graph.get(b5, []):
                b6 = list(b4)
                b6.append(neighbor)
                b1.append(b6)
            b3.add(b5)
        if len(b1) == 0:
            print("Tidak ditemukan")
def fonk2(graph, start):
    b7 = [[start]]
    b2 = {'RS1', 'RS2', 'RS3'}
    b3 = set()
    while b7:
        b4 = b7.pop()
        b5 = b4[-1]
        if b5 in b2:
            return b4
        if b5 not in b3:
            for neighbor in graph.get(b5, []):
                b6 = list(b4)
                b6.append(neighbor)
                b7.append(b6)
            b3.add(b5)
        if len(b7) == 0:
            print("Tidak ditemukan")
b8 = {
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
if b9 = = "__main__":
    b10 = 'A'
    print("BFS Result:", fonk1(b8, b10))
    print("DFS Result:", fonk2(b8, b10))