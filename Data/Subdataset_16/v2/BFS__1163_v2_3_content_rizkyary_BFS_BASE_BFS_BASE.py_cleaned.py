
b1 = {
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
def fonk1(b1, start, goal):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = b2.pop(0)
        b5 = b4[-1]
        if b5 = = goal:
            return b4
        elif b5 not in b3:
            for neighbor in b1.get(b5, []):
                b6 = list(b4)
                b6.append(neighbor)
                b2.append(b6)
            b3.add(b5)
    print("No b4 found")
    return None
if b7 = = "__main__":
    b8 = 'A'
    b9 = 'L'
    b4 = fonk1(b1, b8, b9)
    if b4:
        print(f"Path from {b8} to {b9}: {b4}")