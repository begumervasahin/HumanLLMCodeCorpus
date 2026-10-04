
b1 = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'H', 'I'},
    'D': {'C', 'E', 'F', 'H', 'M'},
    'E': {'D'},
    'F': {'D', 'G', 'M'},
    'G': {'F', 'H'},
    'H': {'C', 'D', 'G', 'L'},
    'I': {'C', 'J', 'K'},
    'J': {'I'},
    'K': {'I', 'L'},
    'L': {'H', 'K'},
    'M': {'D', 'F'}
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
    return "Path not found"
if b7 = = "__main__":
    print("********* BFS ***********")
    b8 = input("Enter starting b5: ")
    b9 = input("Enter goal b5: ")
    print("*************************")
    print()
    b10 = fonk1(b1, b8, b9)
    print(b10)