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
    while b10 >= len(b9) or b10 < 0:
        b10 = int(input('The value entered is out of bounds. Try again: '))
    b11 = int(input('Enter the end node: '))
    while b11 >= len(b9) or b11 < 0:
        b11 = int(input('The value entered is out of bounds. Try again: '))
    distances, b12 = fonk1(b9, b10)
    b13 = b11
    b14 = []
    while True:
        b14.append(b13)
        if b13 = = b10:
            break
        b13 = b12[b13]
    b14.reverse()
    print(f"The shortest path from start node {b10} to every other node in the b9 is:")
    for node, b3 in enumerate(distances):
        print(f"Node {node}: b15 = {b3}")
    print(f"\nThe shortest path from start node {b10} to end node {b11} is:")
    print(b14)
    print(f"b15: {distances[b11]}")
if b16 = = "__main__":
    fonk2()