import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b7, b15):
    b1 = nx.Graph()
    for edge in b7:
        b1.add_edge(b15[edge[0]], b15[edge[1]], b2 = edge[2])
    b3 = nx.spring_layout(b1, k=1.0, iterations=150)
    b4 = nx.get_edge_attributes(b1, 'b2')
    nx.draw(b1, b3, b5 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b1, b3, b6 = b4)
    plt.title("Minimum Spanning Tree")
    plt.show()
def fonk2(b18, b16):
    b7 = []
    b8 = [False] * b16
    b9 = []
    b8[0] = True
    for _ in range(b16 - 1):
        b10 = None
        for i in range(b16):
            if b8[i]:
                for j in range(b16):
                    if not b8[j] and b18[i][j] != 0:
                        if b10 is None or b10[2] > b18[i][j]:
                            b10 = [i, j, b18[i][j]]
        if b10:
            b7.append(b10)
            b8[b10[1]] = True
    return b7
if b11 = = "__main__":
    b12 = sys.argv[1]
    b13 = set()
    with open(b12) as f:
        for line in f:
            b14 = line.strip().split()
            b13.add(b14[0])
            b13.add(b14[1])
    b15 = list(b13)
    b16 = len(b15)
    b17 = {vert: idx for idx, vert in enumerate(b15)}
    b18 = [[0] * b16 for _ in range(b16)]
    with open(b12) as f:
        for line in f:
            b14 = line.strip().split()
            b18[b17[b14[0]]][b17[b14[1]]] = int(b14[2])
            b18[b17[b14[1]]][b17[b14[0]]] = int(b14[2])
    b7 = fonk2(b18, b16)
    b19 = sum(edge[2] for edge in b7)
    print("The minimum spanning tree is as follows:")
    for edge in b7:
        print(f"{b15[edge[0]]} to {b15[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b19} miles.")
    fonk1(b7, b15)