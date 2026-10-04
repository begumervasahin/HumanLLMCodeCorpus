def fonk1(b7, b8, b9):
    b1 = [[b8]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = b9:
            return b3
        elif b4 not in b2:
            for branch in b7.get(b4, []):
                b5 = list(b3)
                b5.append(branch)
                b1.append(b5)
            b2.add(b4)
    return "Path not found"
if b6 = = "__main__":
    b7 = {
        'A': set(['B']),
        'B': set(['A', 'C']),
        'C': set(['B', 'D', 'H', 'I']),
        'D': set(['C', 'E', 'F', 'H', 'M']),
        'E': set(['D']),
        'F': set(['D', 'G', 'M']),
        'G': set(['F', 'H']),
        'H': set(['C', 'D', 'G', 'L']),
        'I': set(['C', 'J', 'K']),
        'J': set(['I']),
        'K': set(['I', 'L']),
        'L': set(['H', 'K']),
        'M': set(['D', 'F'])
    }
    b8 = input("Enter the b8 node: ")
    b9 = input("Enter the b9 node: ")
    b3 = fonk1(b7, b8, b9)
    print("Path from {} to {}: {}".format(b8, b9, b3))
    print("\nLink to GitHub repository: https: