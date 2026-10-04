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
                b5[v2].append(0)
            else:
                print(f"Distance from {b6 + 1} to {v2 + 1}: ", b7 = "")
                b8 = input()
                if b8 = = '':
                    a2 = a1
                else:
                    a2 = int(b8)
                    b4.add_edge(b6, v2, b9 = a2)
                b5[b6].append(a2)
    return b5, b4
if b10 = = '__main__':
    adjacency_matrix, b11 = fonk3()
    b12 = fonk1(adjacency_matrix)
    print("Shortest Path Matrix:")
    fonk2(b12)
    b13 = nx.spring_layout(b11)
    b14 = nx.get_edge_attributes(b11, 'b9')
    nx.draw(b11, b13, b15 = True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b11, b13, b14 = b14)
    plt.show()