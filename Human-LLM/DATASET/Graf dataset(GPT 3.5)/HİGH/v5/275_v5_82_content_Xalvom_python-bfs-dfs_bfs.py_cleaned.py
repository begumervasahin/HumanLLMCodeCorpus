
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
print("********* BFS ***********")
b2 = input("Enter Start Node: ")
b3 = input("Enter Target Node: ")
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
                b8 = b6 + [neighbor]
                b4.append(b8)
            b5.add(b7)
    return "Path not found"
print(fonk1(b1, b2, b3))
print()
print("GitHub Repository: https: