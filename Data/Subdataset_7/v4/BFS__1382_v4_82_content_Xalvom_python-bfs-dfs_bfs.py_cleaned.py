
b1 = {
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
print("*********BFS***********")
b2 = input("Input Start Node: ")
b3 = input("Input Target Node: ")
print("***********************")
print()
def fonk1(b1, start, target):
    b4 = [[start]]
    b5 = set()
    while b4:
        b6 = b4.pop(0)
        b7 = b6[-1]
        if b7 = = target:
            return b6
        if b7 not in b5:
            for neighbor in b1.get(b7, []):
                b8 = list(b6)
                b8.append(neighbor)
                b4.append(b8)
            b5.add(b7)
    return "Path not found"
print(fonk1(b1, b2, b3))
print()
print("GitHub Repository: https: