from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b9):
    b1 = deepcopy(b9)
    b2 = len(b9)
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                b3 = b1[i][k] + b1[k][j]
                if b1[i][j] > b3:
                    b1[i][j] = b3
    return b1
def fonk2(matrix):
    for row in matrix:
        for item in row:
            print(item, ",", b4 = " ")
        print("")
def fonk3():
    a1 = 99999
    print("Create Adjacency Matrix")
    b2 = int(input("Number of vertices: "))
    b5 = []
    for b6 in range(b2):
        b5.append([])
        for v2 in range(b2):
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
    b8 = fonk1(b5)
    print("Shortest path distances:")
    fonk2(b8)
    b9 = nx.DiGraph()
    for b6 in range(len(b5)):
        for v2 in range(len(b5[b6])):
            b10 = b5[b6][v2]
            if b10 != 0 and b10 != float("inf"):
                b9.add_edge(b6, v2, b10 = b10)
    nx.draw(b9, b11 = True)
    plt.show()