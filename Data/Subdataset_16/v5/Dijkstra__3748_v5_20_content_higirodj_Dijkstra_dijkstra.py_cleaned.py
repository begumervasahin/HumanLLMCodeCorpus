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
    while True:
        try:
            b10 = int(input(prompt))
            if 0 <= b10 < graph_size:
                return b10
            else:
                print(f"The value entered is out of bounds. Try again.")
        except ValueError:
            print(f"Invalid input. Please enter an integer.")
def fonk3():
    b11 = input('Enter the file name (without extension): ') + '.txt'
    b12 = np.loadtxt(b11)
    b13 = fonk2('Enter starting b10: ', len(b12))
    b14 = fonk2('Enter end b10: ', len(b12))
    costs, b15 = fonk1(b12, b13)
    print(f"The shortest path from the start b10 {b13} to every other b10 in the b12 is:\b1{costs}")
    b16 = []
    b10 = b14
    while b10 != b13:
        b16.append(b10)
        b10 = b15[b10]
    b16.append(b13)
    b16.reverse()
    print(f"The shortest path from the start b10 {b13} to the target b10 {b14} is {b16} with a b3 of {dict(costs).get(b14)}")
if b17 = = "__main__":
    fonk3()