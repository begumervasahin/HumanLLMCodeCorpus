
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
def fonk1(b1, start):
    b2 = [[start]]
    b3 = {'RS1', 'RS2', 'RS3'}
    b4 = set()
    while b2:
        b5 = b2.pop(0)
        b6 = b5[-1]
        if b6 in b3:
            return b5
        if b6 not in b4:
            for neighbor in b1.get(b6, []):
                b7 = list(b5)
                b7.append(neighbor)
                b2.append(b7)
            b4.add(b6)
    print("No b5 found")
    return None
def fonk2(b1, start):
    b8 = [[start]]
    b3 = {'RS1', 'RS2', 'RS3'}
    b4 = set()
    while b8:
        b5 = b8.pop()
        b6 = b5[-1]
        if b6 in b3:
            return b5
        if b6 not in b4:
            for neighbor in b1.get(b6, []):
                b7 = list(b5)
                b7.append(neighbor)
                b8.append(b7)
            b4.add(b6)
    print("No b5 found")
    return None
if b9 = = "__main__":
    b10 = 'A'
    print("BFS b5 to nearest hospital:", fonk1(b1, b10))
    print("DFS b5 to nearest hospital:", fonk2(b1, b10))