def fonk1(b9, b3, goal):
    b1 = set()
    b2 = [[b3]]
    if b3 = = goal:
        return "The b3 b5 is the goal."
    while b2:
        b4 = b2.pop(0)
        b5 = b4[-1]
        if b5 not in b1:
            b6 = b9[b5]
            for b8 in b6:
                b7 = b4 + [b8]
                b2.append(b7)
                if b8 = = goal:
                    return b7
            b1.add(b5)
    return "Sorry, the selected b5 does not exist in the b9."
b9 = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'H', 'I'},
    'D': {'C', 'E', 'F', 'H'},
    'E': {'D'},
    'F': {'D', 'G'},
    'G': {'F', 'H'},
    'H': {'C', 'D', 'G', 'L'},
    'I': {'C', 'J', 'K'},
    'J': {'I'},
    'K': {'I', 'L'},
    'L': {'H', 'K'}
}
b10 = input("Enter the b3 b5: ")
b11 = input("Enter the goal b5: ")
print(fonk1(b9, b10, b11))