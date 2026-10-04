import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b7, b12):
    b1 = nx.Graph()
    for edge in b7:
        b1.add_edge(b12[edge[0]], b12[edge[1]], b2 = edge[2])
    b3 = nx.spring_layout(b1, k=1.0, iterations=150)
    b4 = nx.get_edge_attributes(b1, 'b2')
    nx.draw(b1, b3, b5 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b1, b3, b6 = b4)
    plt.title("Minimum Spanning Tree")
    plt.show()
def fonk2(b15, vertex_count):
    b7 = []
    b8 = [False] * vertex_count
    b8[0] = True
    for _ in range(vertex_count - 1):
        b9 = None
        for i in range(vertex_count):
            if b8[i]:
                for j in range(vertex_count):
                    if not b8[j] and b15[i][j] != 0:
                        if b9 is None or b9[2] > b15[i][j]:
                            b9 = [i, j, b15[i][j]]
        if b9:
            b7.append(b9)
            b8[b9[1]] = True
    return b7
def fonk3(b17):
    b10 = set()
    with open(b17) as f:
        for line in f:
            b11 = line.strip().split()
            b10.add(b11[0])
            b10.add(b11[1])
    b12 = list(b10)
    b13 = len(b12)
    b14 = {vert: idx for idx, vert in enumerate(b12)}
    b15 = [[0] * b13 for _ in range(b13)]
    with open(b17) as f:
        for line in f:
            b11 = line.strip().split()
            b15[b14[b11[0]]][b14[b11[1]]] = int(b11[2])
            b15[b14[b11[1]]][b14[b11[0]]] = int(b11[2])
    return b12, b15, b13
if b16 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py <input_file>")
        sys.exit(1)
    b17 = sys.argv[1]
    b12, b15, b13 = fonk3(b17)
    b7 = fonk2(b15, b13)
    b18 = sum(edge[2] for edge in b7)
    print("The minimum spanning tree is as follows:")
    for edge in b7:
        print(f"{b12[edge[0]]} to {b12[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b18} miles.")
    fonk1(b7, b12)