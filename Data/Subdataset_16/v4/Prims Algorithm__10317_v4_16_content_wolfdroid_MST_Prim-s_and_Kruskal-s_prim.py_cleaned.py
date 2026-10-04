import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b19):
    b1 = []
    b2 = []
    b3 = []
    b4 = [0, 1, b19[0][1]]
    a1 = 0
    for _ in range(b18 - 1):
        b2.append(a1)
        for b20 in range(b18):
            if b19[a1][b20] != 0:
                b3.append([a1, b20, b19[a1][b20]])
        for edge in b3:
            if edge[2] < b4[2] and edge[1] not in b2:
                b4 = edge
        b1.append(b4)
        a1 = b4[1]
        b3.remove(b4)
        if b3:
            b4 = b3[0]
    return b1
def fonk2(b1):
    b5 = nx.Graph()
    for edge in b1:
        b5.add_edge(
            b17[edge[0]],
            b17[edge[1]],
            b6 = int(edge[2])
        )
    b7 = nx.spring_layout(b5, k=20, iterations=150, scale=1.0)
    b8 = dict(((b20, a1), str(d['b6'])) for b20, a1, d in b5.edges(data=True))
    nx.draw_networkx_edge_labels(b5, b7, b9 = b8)
    nx.draw_networkx_nodes(b5, b7, b10 = 600, node_color='lightblue')
    nx.draw_networkx_edges(b5, b7, b11 = b5.edges(), width=2, edge_color='black', alpha=0.5)
    nx.draw_networkx_labels(b5, b7, b12 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
if b13 = = "__main__":
    b14 = sys.argv[1]
    b15 = set()
    with open(b14) as f:
        for line in f:
            b16 = line.strip().split(' ')
            b15.add(b16[0])
            b15.add(b16[1])
    b17 = list(b15)
    b18 = len(b15)
    b19 = [[0 for _ in range(b18)] for _ in range(b18)]
    with open(b14) as f:
        for line in f:
            b16 = line.strip().split(' ')
            b20 = b17.index(b16[0])
            a1 = b17.index(b16[1])
            b6 = int(b16[2])
            b19[b20][a1] = b6
            b19[a1][b20] = b6
    b1 = fonk1(b19)
    b21 = sum(edge[2] for edge in b1)
    print("The minimum spanning tree:")
    for edge in b1:
        print(f"{b17[edge[0]]} to {b17[edge[1]]} = {edge[2]} units.")
    print(f"Total b6: {b21} units.")
    fonk2(b1)