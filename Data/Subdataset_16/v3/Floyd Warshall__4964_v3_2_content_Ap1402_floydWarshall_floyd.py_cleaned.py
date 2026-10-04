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
        b4 = " , ".join(map(str, row))
        print(b4)
        print("")
def fonk3():
    a1 = 99999
    b5 = nx.DiGraph()
    print("Create Adjacency Matrix")
    b2 = int(input("Number of vertices: "))
    b6 = []
    for b7 in range(b2):
        b6.append([])
        for v2 in range(b2):
            if b7 = = v2:
                b6[b7].append(0)
            else:
                b8 = input(f"Distance from {b7 + 1} to {v2 + 1} (leave blank for no direct path): ")
                if b8 = = '':
                    b6[b7].append(a1)
                else:
                    b8 = int(b8)
                    b6[b7].append(b8)
                    b5.add_edge(b7, v2, b9 = b8)
    return b6, b5
def fonk4(b5):
    b10 = nx.spring_layout(b5)
    b11 = nx.get_edge_attributes(b5, 'b9')
    nx.draw(b5, b10, b12 = True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b5, b10, b11 = b11)
    plt.show()
def fonk5():
    b6, b13 = fonk3()
    b14 = fonk1(b6)
    print("Shortest Path Matrix:")
    fonk2(b14)
    fonk4(b13)
if b15 = = '__main__':
    fonk5()