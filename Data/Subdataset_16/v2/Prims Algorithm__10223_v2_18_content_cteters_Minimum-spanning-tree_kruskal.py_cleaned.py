import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b11, b19):
    b1 = nx.Graph()
    for edge in b11:
        b1.add_edge(b19[edge[0]], b19[edge[1]], b2 = int(edge[2]))
    b3 = nx.spring_layout(b1, k=20, iterations=150, b2='b2', scale=1.0)
    b4 = { (u, v): str(d['b2']) for u, v, d in b1.b17(data=True) }
    nx.draw_networkx_edge_labels(b1, b3, b4 = b4)
    b5 = max(len(b19) * 180, 100)
    nx.draw_networkx_nodes(b1, b3, b5 = b5, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b3, b6 = b1.b17, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b3, b7 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b21):
    return sorted(b21, b8 = lambda x: x[2])
def fonk3(b13, i):
    if b13[i] != i:
        b13[i] = fonk3(b13, b13[i])
    return b13[i]
def fonk4(b13, b14, x, y):
    b9 = fonk3(b13, x)
    b10 = fonk3(b13, y)
    if b9 != b10:
        if b14[b9] > b14[b10]:
            b13[b10] = b9
        elif b14[b9] < b14[b10]:
            b13[b9] = b10
        else:
            b13[b10] = b9
            b14[b9] += 1
def fonk5(b21, b20):
    b11 = []
    b12 = fonk2(b21)
    b13 = list(range(b20))
    b14 = [0] * b20
    for edge in b12:
        u, v, b2 = edge
        b15 = fonk3(b13, u)
        b16 = fonk3(b13, v)
        if b15 != b16:
            b11.append(edge)
            fonk4(b13, b14, b15, b16)
            if len(b11) == b20 - 1:
                break
    return b11
def fonk6(file_name):
    with open(file_name) as f:
        b17 = [line.strip().split() for line in f]
    b18 = {edge[0] for edge in b17} | {edge[1] for edge in b17}
    b19 = list(b18)
    b20 = len(b18)
    b21 = [[b19.index(edge[0]), b19.index(edge[1]), int(edge[2])] for edge in b17]
    b11 = fonk5(b21, b20)
    b22 = sum(edge[2] for edge in b11)
    print("The minimum spanning tree is as follows:")
    for edge in b11:
        print(f"{b19[edge[0]]} to {b19[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b22} miles.")
    fonk1(b11, b19)
if b23 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        sys.exit(1)
    fonk6(sys.argv[1])