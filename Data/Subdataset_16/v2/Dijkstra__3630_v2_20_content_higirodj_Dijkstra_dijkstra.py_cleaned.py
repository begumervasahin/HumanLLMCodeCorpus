import numpy as np
def fonk1(b11, source):
    b1 = len(b11)
    b2 = float('inf')
    b3 = [b2] * b1
    b3[source] = 0
    b4 = []
    b5 = []
    b6 = {source: b3[source]}
    b7 = {}
    while b6:
        current_node, b8 = min(b6.items(), key=lambda x: x[1])
        del b6[current_node]
        b4.append(current_node)
        b5.append((current_node, b8))
        for neighbor in range(b1):
            if b11[current_node][neighbor] != 0 and neighbor not in b4:
                b9 = b3[current_node] + b11[current_node][neighbor]
                if b9 < b3[neighbor]:
                    b3[neighbor] = b9
                    b6[neighbor] = b9
                    b7[neighbor] = current_node
    return b5, b7
def fonk2():
    b10 = input('Enter the file name (without extension): ') + '.txt'
    b11 = np.loadtxt(b10)
    b12 = int(input('Enter starting node: '))
    while b12 >= len(b11) or b12 < 0:
        b12 = int(input('The value entered is out of bounds. Try again: '))
    b13 = int(input('Enter end node: '))
    while b13 >= len(b11) or b13 < 0:
        b13 = int(input('The value entered is out of bounds. Try again: '))
    b14 = b13
    costs, b15 = fonk1(b11, b12)
    print(f"The shortest path from the start node {b12} to every other node in the b11 is:\b1{costs}")
    b16 = []
    while b13 != b12:
        b16.append(b13)
        b13 = b15[b13]
    b16.append(b12)
    b16.reverse()
    print(f"The shortest path from the start node {b12} to the target node {b14} is {b16} with a b3 of {dict(costs).get(b14)}")
if b17 = = "__main__":
    fonk2()