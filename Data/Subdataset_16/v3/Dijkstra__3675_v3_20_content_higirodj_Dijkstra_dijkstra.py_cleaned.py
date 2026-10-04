import numpy as np
def fonk1(b12, source):
    b1 = len(b12)
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
            if b12[current_node][neighbor] != 0 and neighbor not in b4:
                b9 = b3[current_node] + b12[current_node][neighbor]
                if b9 < b3[neighbor]:
                    b3[neighbor] = b9
                    b6[neighbor] = b9
                    b7[neighbor] = current_node
    return b5, b7
def fonk2(prompt, graph_size):
    b10 = int(input(prompt))
    while b10 >= graph_size or b10 < 0:
        b10 = int(input(f"The value entered is out of bounds. Try again: {prompt}"))
    return b10
def fonk3():
    b11 = input('Enter the file name (without extension): ') + '.txt'
    b12 = np.loadtxt(b11)
    b13 = fonk2('Enter starting b10: ', len(b12))
    b14 = fonk2('Enter end b10: ', len(b12))
    b15 = b14
    costs, b16 = fonk1(b12, b13)
    print(f"The shortest path from the start b10 {b13} to every other b10 in the b12 is:\b1{costs}")
    b17 = []
    while b14 != b13:
        b17.append(b14)
        b14 = b16[b14]
    b17.append(b13)
    b17.reverse()
    print(f"The shortest path from the start b10 {b13} to the target b10 {b15} is {b17} with a b3 of {dict(costs).get(b15)}")
if b18 = = "__main__":
    fonk3()