import numpy as np
def fonk1(b9, source):
    b1 = len(b9)
    b2 = float('inf')
    b3 = [b2 for _ in range(b1)]
    b3[source] = 0
    b4 = set()
    b5 = {}
    while len(b4) < b1:
        b6 = min(
            (node for node in range(b1) if node not in b4),
            b7 = lambda x: b3[x]
        )
        b4.add(b6)
        for neighbor, weight in enumerate(b9[b6]):
            if weight > 0 and neighbor not in b4:
                if b3[b6] + weight < b3[neighbor]:
                    b3[neighbor] = b3[b6] + weight
                    b5[neighbor] = b6
    return b3, b5
def fonk2():
    b8 = input('Enter the file name (without extension): ') + '.txt'
    b9 = np.loadtxt(b8)
    b10 = int(input('Enter the starting node: '))
    while not (0 <= b10 < len(b9)):
        b10 = int(input('Invalid input. Please enter a valid starting node: '))
    b11 = int(input('Enter the end node: '))
    while not (0 <= b11 < len(b9)):
        b11 = int(input('Invalid input. Please enter a valid end node: '))
    b3, b12 = fonk1(b9, b10)
    b13 = []
    b6 = b11
    while b6 != b10:
        b13.append(b6)
        b6 = b12[b6]
    b13.append(b10)
    b13.reverse()
    print(f"The shortest path from start node {b10} to every other node in the b9 is:")
    for node, distance in enumerate(b3):
        print(f"Node {node}: b14 = {distance}")
    print(f"\nThe shortest path from start node {b10} to end node {b11} is:")
    print(b13)
    print(f"b14: {b3[b11]}")
if b15 = = "__main__":
    fonk2()