from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b10):
    b1 = deepcopy(b10)
    b2 = len(b10)
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                b3 = b1[i][k] + b1[k][j]
                if b1[i][j] > b3:
                    b1[i][j] = b3
    return b1
def fonk2(matrix):
    for b6 in matrix:
        print("\t".join(map(str, b6)))
def fonk3():
    b4 = float("inf")
    b2 = int(input("Enter the number of vertices: "))
    b5 = []
    print("Enter the b8 between vertices (use b4 for infinity):")
    for b7 in range(b2):
        b6 = []
        for v2 in range(b2):
            if b7 = = v2:
                b6.append(0)
            else:
                b8 = float(input(f"Distance from vertex {b7 + 1} to {v2 + 1}: "))
                b6.append(b8 if b8 != b4 else float("inf"))
        b5.append(b6)
    return b5
if b9 = = "__main__":
    b5 = fonk3()
    b1 = fonk1(b5)
    print("\nShortest path distances:")
    fonk2(b1)
    b10 = nx.DiGraph()
    for b7 in range(len(b5)):
        for v2 in range(len(b5[b7])):
            b11 = b5[b7][v2]
            if b11 != 0 and b11 != float("inf"):
                b10.add_edge(b7, v2, b11 = b11)
    nx.draw(b10, b12 = True)
    plt.show()