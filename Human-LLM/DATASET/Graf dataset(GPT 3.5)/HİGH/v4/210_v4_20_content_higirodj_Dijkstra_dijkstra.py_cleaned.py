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
    b10 = input('Enter the file name: ') + '.txt'
    b11 = np.loadtxt(b10)
    b1 = len(b11)
    b12 = int(input('Enter starting node: '))
    while not (0 <= b12 < b1):
        b12 = int(input('Invalid input. Please enter a valid starting node: '))
    b13 = int(input('Enter end node: '))
    while not (0 <= b13 < b1):
        b13 = int(input('Invalid input. Please enter a valid end node: '))
    costs, b14 = fonk1(b11, b12)
    print(f"The shortest path from start node {b12} to every other node in the b11 is:")
    print(costs)
    b15 = []
    b16 = b13
    while b16 != b12:
        b15.append(b16)
        b16 = b14[b16]
    b15.append(b12)
    b15.reverse()
    print(f"\nThe shortest path from start node {b12} to target node {b13} is:")
    print(b15)
    print(f"Distance: {dict(costs).get(b13)}")
if b17 = = "__main__":
    fonk2()