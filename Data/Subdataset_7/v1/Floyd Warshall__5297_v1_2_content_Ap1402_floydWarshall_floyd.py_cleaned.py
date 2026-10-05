from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b5):
    b1 = deepcopy(b5)
    b2 = len(b5)
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
    b8 = fonk3()
    b9 = fonk1(b8)
    print("Shortest path distances:")
    fonk2(b9)
    b10 = nx.DiGraph()
    for b6 in range(len(b8)):
        for v2 in range(len(b8[b6])):
            b11 = b8[b6][v2]
            if b11 != 0 and b11 != float("inf"):
                b10.add_edge(b6, v2, b11 = b11)
    nx.draw(b10, b12 = True)
    plt.show()