def fonk1(b6, start, goal):
    b1 = [[start]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = goal:
            return b3
        if b4 not in b2:
            for neighbor in b6.get(b4, []):
                b5 = list(b3)
                b5.append(neighbor)
                b1.append(b5)
            b2.add(b4)
    print("Path not found")
    return None
b6 = {
    'A': {'B', 'C'},
    'B': {'A', 'H', 'J'},
    'C': {'A', 'D', 'G'},
    'D': {'C', 'E'},
    'E': {'D', 'F'},
    'F': {'E', 'G', 'K', 'L'},
    'G': {'C', 'F'},
    'H': {'B', 'I'},
    'I': {'H', 'J', 'K'},
    'J': {'B', 'I'},
    'K': {'F', 'I', 'L'},
    'L': {'F', 'K'}
}
b7 = 'A'
b8 = 'L'
b9 = fonk1(b6, b7, b8)
if b9:
    print("Path found:", b9)
else:
    print("Path not found")