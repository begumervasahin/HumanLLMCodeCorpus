from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b11):
    b1 = len(b11)
    b2 = deepcopy(b11)
    for k in range(b1):
        for i in range(b1):
            for j in range(b1):
                b3 = b2[i][k] + b2[k][j]
                if b2[i][j] > b3:
                    b2[i][j] = b3
    return b2
def fonk2(matrix):
    for b5 in matrix:
        print("\t".join(str(item) for item in b5))
def fonk3():
    a1 = 99999
    print("Create Adjacency Matrix")
    b1 = int(input("Number of vertices: "))
    b4 = []
    for b6 in range(b1):
        b5 = []
        for v2 in range(b1):
            if b6 = = v2:
                b5.append(0)
            else:
                b7 = "Distance from vertex {} to {}: ".format(b6 + 1, v2 + 1)
                b8 = input(b7).strip()
                b9 = int(b8) if b8 else a1
                b5.append(b9)
        b4.append(b5)
    return b4
if b10 = = "__main__":
    b4 = fonk3()
    b2 = fonk1(b4)
    print("Shortest path distances:")
    fonk2(b2)
    b11 = nx.DiGraph()
    for b6 in range(len(b4)):
        for v2 in range(len(b4[b6])):
            b12 = b4[b6][v2]
            if b12 != 0 and b12 != float("inf"):
                b11.add_edge(b6, v2, b12 = b12)
    nx.draw(b11, b13 = True)
    plt.show()