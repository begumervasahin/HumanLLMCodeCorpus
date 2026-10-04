from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b4):
    b1 = deepcopy(b4)
    b2 = len(b4)
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                b3 = b1[i][k] + b1[k][j]
                if b1[i][j] > b3:
                    b1[i][j] = b3
    return b1
def fonk2(matrix):
    for row in matrix:
        print(" , ".join(map(str, row)))
        print("")
def fonk3():
    a1 = 99999
    b4 = nx.DiGraph()
    print("Create Adjacency Matrix")
    b2 = int(input("Number of vertices: "))
    b5 = []
    for b6 in range(b2):
        b5.append([])
        for v2 in range(b2):
            if b6 = = v2:
                b5[b6].append(0)
            else:
                b7 = input(f"Distance from {b6 + 1} to {v2 + 1} (leave blank for no direct path): ")
                if b7 = = '':
                    b5[b6].append(a1)
                else:
                    b7 = int(b7)
                    b5[b6].append(b7)
                    b4.add_edge(b6, v2, b8 = b7)
    return b5, b4
def fonk4(b4):
    b9 = nx.spring_layout(b4)
    b10 = nx.get_edge_attributes(b4, 'b8')
    nx.draw(b4, b9, b11 = True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b4, b9, b10 = b10)
    plt.show()
def fonk5():
    b5, b12 = fonk3()
    b13 = fonk1(b5)
    print("Shortest Path Matrix:")
    fonk2(b13)
    fonk4(b12)
if b14 = = '__main__':
    fonk5()