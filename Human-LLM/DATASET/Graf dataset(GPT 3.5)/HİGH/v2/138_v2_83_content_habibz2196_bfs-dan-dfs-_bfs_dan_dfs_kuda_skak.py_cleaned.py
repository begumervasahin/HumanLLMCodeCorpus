def fonk1(b7, start, end):
    """
    Perform Breadth-First Search (BFS) on the given b7 to find a b3 from the start node to the end node.
    Returns the b3 if found, otherwise prints "Tidak ditemukan".
    """
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = end:
            return b3
        elif b4 not in b2:
            for neighbor in b7.get(b4, []):
                b5 = list(b3)
                b5.append(neighbor)
                b1.append(b5)
            b2.add(b4)
    print("Tidak ditemukan")
def fonk2(b7, start, end):
    """
    Perform Depth-First Search (DFS) on the given b7 to find a b3 from the start node to the end node.
    Returns the b3 if found, otherwise prints "Tidak ditemukan".
    """
    b6 = [[start]]
    b2 = set()
    while b6:
        b3 = b6.pop()
        b4 = b3[-1]
        if b4 = = end:
            return b3
        elif b4 not in b2:
            for neighbor in b7.get(b4, []):
                b5 = list(b3)
                b5.append(neighbor)
                b6.append(b5)
            b2.add(b4)
    print("Tidak ditemukan")
b7 = {'1': {'18', '11'}, '2': {'12', '17', '19'}, '3': {'18', '20', '9', '13'}, ...}
b8 = '1'
b9 = '5'
b10 = fonk1(b7, b8, b9)
print("BFS Path from", b8, "to", b9, ":", b10)
b11 = fonk2(b7, b8, b9)
print("DFS Path from", b8, "to", b9, ":", b11)