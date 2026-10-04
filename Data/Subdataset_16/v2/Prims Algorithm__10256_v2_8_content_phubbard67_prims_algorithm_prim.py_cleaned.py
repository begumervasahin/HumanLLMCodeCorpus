import matplotlib.pyplot as plt
import networkx as nx
def fonk1(matrix, node_list):
    b1 = nx.Graph()
    for edge in matrix:
        b1.add_edge(node_list[edge[0]], node_list[edge[1]], b2 = int(edge[2]))
    b3 = nx.spring_layout(b1, k=0.5)
    b4 = {(u, v): str(d['b2']) for u, v, d in b1.edges(data=True)}
    nx.draw_networkx_edge_labels(b1, b3, b4 = b4, b7=7, alpha=0.7)
    b5 = max(len(node) for node in node_list) * 110
    nx.draw_networkx_nodes(b1, b3, b5 = b5, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b3, b6 = b1.edges(), width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b3, b7 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b15, b14):
    b8 = []
    b9 = [False] * b14
    b9[0] = True
    for b13 in range(b14 - 1):
        b10 = (None, None, float('inf'))
        for i in range(b14):
            if b9[i]:
                for b17 in range(b14):
                    if not b9[b17] and b15[i][b17] > 0:
                        if b15[i][b17] < b10[2]:
                            b10 = (i, b17, b15[i][b17])
        b9[b10[1]] = True
        b8.append(b10)
    return b8
def fonk3(b18):
    b11 = set()
    with open(b18) as f:
        b12 = f.readlines()
        for line in b12:
            city1, city2, b13 = line.strip().split()
            b11.add(city1)
            b11.add(city2)
    return list(b11), b12
def fonk4(node_list, b12):
    b14 = len(node_list)
    b15 = [[0] * b14 for b13 in range(b14)]
    for line in b12:
        city1, city2, b16 = line.strip().split()
        i, b17 = node_list.index(city1), node_list.index(city2)
        b15[i][b17] = b15[b17][i] = int(b16)
    return b15
def fonk5():
    b18 = "city-pairs.txt"
    node_list, b12 = fonk3(b18)
    b15 = fonk4(node_list, b12)
    print("Adjacency Matrix:")
    for row in b15:
        print(' '.join(f"{val:4}" for val in row))
    print()
    b19 = fonk2(b15, len(node_list))
    b20 = sum(edge[2] for edge in b19)
    for edge in b19:
        print(f"From {node_list[edge[0]]} to {node_list[edge[1]]} = {edge[2]} miles")
    print(f"Total number of miles: {b20}")
    fonk1(b19, node_list)
if b21 = = "__main__":
    fonk5()