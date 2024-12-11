import numpy as np
def fonk1(b11, source):
    b1 = len(b11)
    b2 = float('inf')
    b3 = [b2 for _ in range(b1)]
    b3[source] = 0
    b4 = set()
    b5 = []
    b6 = {source: b3[source]}
    b7 = {}
    while b6:
        current_node, b8 = min(b6.items(), key=lambda x: x[1])
        del b6[current_node]
        b4.add(current_node)
        b5.append((current_node, b8))
        for neighbor, weight in enumerate(b11[current_node]):
            if weight != 0 and neighbor not in b4:
                b9 = b3[current_node] + weight
                if b9 < b3[neighbor]:
                    b3[neighbor] = b9
                    b6[neighbor] = b9
                    b7[neighbor] = current_node
    return b5, b7
def fonk2():
    b10 = input('Enter the file name (without extension): ') + '.txt'
    b11 = np.loadtxt(b10)
    b1 = len(b11)
    b12 = int(input('Enter the starting node: '))
    while not (0 <= b12 < b1):
        b12 = int(input('Invalid input. Please enter a valid starting node: '))
    b13 = int(input('Enter the end node: '))
    while not (0 <= b13 < b1):
        b13 = int(input('Invalid input. Please enter a valid end node: '))
    b5, b14 = fonk1(b11, b12)
    print(f"The shortest paths from start node {b12} to every other node are:")
    for node, b8 in b5:
        print(f"Node {node}: b15 = {b8}")
    b16 = []
    b17 = b13
    while b17 != b12:
        b16.append(b17)
        b17 = b14[b17]
    b16.append(b12)
    b16.reverse()
    print(f"\nThe shortest path from start node {b12} to target node {b13} is:")
    print(b16)
    print(f"Total distance: {dict(b5).get(b13)}")
if b18 = = "__main__":
    fonk2()