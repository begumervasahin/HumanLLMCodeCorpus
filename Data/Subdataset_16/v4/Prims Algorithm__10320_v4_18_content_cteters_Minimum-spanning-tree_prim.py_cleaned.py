import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b8, b14, b15):
    b1 = nx.Graph()
    for edge in b8:
        b1.add_edge(b14[edge[0]], b14[edge[1]], b2 = edge[2])
    b3 = nx.spring_layout(b1, k=20, iterations=150, b2='b2')
    b4 = {(u, a1): d['b2'] for u, a1, d in b1.edges(data=True)}
    nx.draw_networkx_edge_labels(b1, b3, b4 = b4)
    b5 = max(len(vert) for vert in b14) * 180
    nx.draw_networkx_nodes(b1, b3, b5 = b5, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b3, b6 = b1.edges, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b3, b7 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b16, b15):
    b8 = []
    b9 = []
    b10 = []
    b11 = [0, 1, b16[0][1]]
    a1 = 0
    for _ in range(b15 - 1):
        b9.append(a1)
        for u in range(b15):
            if b16[a1][u] != 0:
                b10.append([a1, u, b16[a1][u]])
        for edge in b10[1:]:
            if edge[2] < b11[2] and edge[1] not in b9:
                b11 = edge
        b8.append(b11)
        a1 = b11[1]
        b10.remove(b11)
        if b10:
            b11 = b10[0]
    return b8
def fonk3(b19):
    b12 = set()
    with open(b19) as f:
        for line in f:
            b13 = line.strip().split(' ')
            b12.add(b13[0])
            b12.add(b13[1])
    b14 = list(b12)
    b15 = len(b12)
    b16 = [[0 for _ in range(b15)] for _ in range(b15)]
    with open(b19) as f:
        for line in f:
            b13 = line.strip().split(' ')
            idx1, b17 = b14.index(b13[0]), b14.index(b13[1])
            b2 = int(b13[2])
            b16[idx1][b17] = b16[b17][idx1] = b2
    b8 = fonk2(b16, b15)
    a2 = 0
    print("The minimum spanning tree is as follows:")
    for edge in b8:
        print(f"{b14[edge[0]]} to {b14[edge[1]]} = {edge[2]} miles")
        a2 += edge[2]
    print(f"Total b2: {a2} miles.")
    fonk1(b8, b14, b15)
if b18 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py <b19>")
        sys.exit(1)
    b19 = sys.argv[1]
    fonk3(b19)