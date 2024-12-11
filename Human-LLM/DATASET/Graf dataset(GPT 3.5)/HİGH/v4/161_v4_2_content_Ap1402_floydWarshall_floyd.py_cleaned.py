from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b8):
    b1 = len(b8)
    b2 = deepcopy(b8)
    for k in range(b1):
        for i in range(b1):
            for j in range(b1):
                b3 = b2[i][k] + b2[k][j]
                if b2[i][j] > b3:
                    b2[i][j] = b3
    return b2
def fonk2(matrix):
    for row in matrix:
        for item in row:
            print(item, ",", b4 = " ")
        print("")
def fonk3():
    a1 = 99999
    print("Create Adjacency Matrix")
    b1 = int(input("Number of vertices: "))
    b5 = []
    for b6 in range(b1):
        b5.append([])
        for v2 in range(b1):
            if b6 = = v2:
                b5[b6].append(0)
            else:
                print("Distance from vertex", b6 + 1, "to", v2 + 1, ": ", b4 = "")
                b3 = input()
                if b3 = = '':
                    a2 = a1
                else:
                    a2 = int(b3)
                b5[b6].append(a2)
    return b5
if b7 = = "__main__":
    b5 = fonk3()
    b2 = fonk1(b5)
    print("Shortest path distances:")
    fonk2(b2)
    b8 = nx.DiGraph()
    for b6 in range(len(b5)):
        for v2 in range(len(b5[b6])):
            b9 = b5[b6][v2]
            if b9 != 0 and b9 != float("inf"):
                b8.add_edge(b6, v2, b9 = b9)
    nx.draw(b8, b10 = True)
    plt.show()