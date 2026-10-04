import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b18, b17):
    b1 = []
    b2 = []
    b3 = []
    b4 = [0, 1, b18[0][1]]
    a1 = 0
    for _ in range(b17 - 1):
        b2.append(a1)
        for neighbor in range(b17):
            if b18[a1][neighbor] != 0:
                b3.append([a1, neighbor, b18[a1][neighbor]])
        for edge in b3:
            if edge[2] < b4[2] and edge[1] not in b2:
                b4 = edge
        b1.append(b4)
        a1 = b4[1]
        b3.remove(b4)
        if b3:
            b4 = b3[0]
    return b1
def fonk2(b1, b16, b17):
    b5 = nx.Graph()
    for edge in b1:
        b5.add_edge(
            b16[edge[0]],
            b16[edge[1]],
            b6 = int(edge[2])
        )
    b7 = nx.spring_layout(b5, k=20, iterations=150, scale=1.0)
    b8 = dict(((b19, b20), str(d['b6'])) for b19, b20, d in b5.b14(data=True))
    nx.draw_networkx_edge_labels(b5, b7, b9 = b8)
    nx.draw_networkx_nodes(b5, b7, b10 = 600, node_color='lightblue')
    nx.draw_networkx_edges(b5, b7, b11 = b5.b14(), width=2, edge_color='black', alpha=0.5)
    nx.draw_networkx_labels(b5, b7, b12 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk3(b22):
    b13 = set()
    b14 = []
    with open(b22) as f:
        for line in f:
            b15 = line.strip().split(' ')
            b13.add(b15[0])
            b13.add(b15[1])
            b14.append((b15[0], b15[1], int(b15[2])))
    b16 = list(b13)
    b17 = len(b13)
    b18 = [[0 for _ in range(b17)] for _ in range(b17)]
    for edge in b14:
        b19 = b16.index(edge[0])
        b20 = b16.index(edge[1])
        b6 = edge[2]
        b18[b19][b20] = b6
        b18[b20][b19] = b6
    return b18, b16, b17
if b21 = = "__main__":
    b22 = sys.argv[1]
    b18, b16, b17 = fonk3(b22)
    b1 = fonk1(b18, b17)
    b23 = sum(edge[2] for edge in b1)
    print("The minimum spanning tree:")
    for edge in b1:
        print(f"{b16[edge[0]]} to {b16[edge[1]]} = {edge[2]} units.")
    print(f"Total b6: {b23} units.")
    fonk2(b1, b16, b17)