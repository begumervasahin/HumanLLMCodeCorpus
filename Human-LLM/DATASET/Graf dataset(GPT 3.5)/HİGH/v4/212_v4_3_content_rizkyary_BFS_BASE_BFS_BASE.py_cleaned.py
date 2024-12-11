
b1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'H', 'J']),
    'C': set(['A', 'D', 'G']),
    'D': set(['C', 'E']),
    'E': set(['D', 'F']),
    'F': set(['E', 'G', 'K', 'L']),
    'G': set(['C', 'F']),
    'H': set(['B', 'I']),
    'I': set(['H', 'J', 'K']),
    'J': set(['B', 'I']),
    'K': set(['F', 'I', 'L']),
    'L': set(['F', 'K'])
}
def fonk1(b1, start, goal):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop(0)
        b5 = b4[-1]
        if b5 = = goal:
            return b4
        if b5 not in b3:
            for neighbor in b1.get(b5, []):
                b6 = list(b4)
                b6.append(neighbor)
                b2.append(b6)
            b3.add(b5)
    print("Tidak ditemukan")
    return None
b7 = 'A'
b8 = 'L'
b9 = fonk1(b1, b7, b8)
print("Path found:", b9) if b9 else print("Path not found")