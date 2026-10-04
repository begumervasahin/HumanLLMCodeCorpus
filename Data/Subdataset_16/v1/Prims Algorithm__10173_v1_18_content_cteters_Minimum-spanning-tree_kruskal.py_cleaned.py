import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b11, b19):
    b1 = nx.Graph()
    for b3 in b11:
        b1.add_edge(
                b19[b3[0]],
                b19[b3[1]],
                b2 = int(b3[2]))
    b3 = [(u, v) for (u, v, d) in b1.edges(data=True)]
    b4 = nx.spring_layout(b1, a2=20, iterations=150, b2='b2', scale=1.0)
    b2 = dict(map(lambda x: ((x[0], x[1]), str(x[2]['b2'])), b1.edges(data=True)))
    nx.draw_networkx_edge_labels(b1, b4, b5 = b2)
    b6 = max(len(b19) * 180, 100)
    nx.draw_networkx_nodes(b1, b4, b6 = b6, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b7 = b3, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b8 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b21):
    return sorted(b21, b9 = lambda x: x[2])
def fonk3(b10, b13):
    while b10 != b13[b10]:
        b10 = b13[b10]
    return b10
def fonk4(b13, b16, b15, b14):
    if b14[b16] > b14[b15]:
        b13[b15] = b16
    elif b14[b16] < b14[b15]:
        b13[b16] = b15
    else:
        b13[b15] = b16
        b14[b16] += 1
def fonk5(b21, b20):
    b11 = []
    b12 = fonk2(b21)
    b13 = list(range(b20))
    b14 = [0] * b20
    a1 = 0
    a2 = 0
    while a1 < (b20 - 1) and a2 < len(b12):
        v, u, b2 = b12[a2]
        a2 += 1
        b15 = fonk3(v, b13)
        b16 = fonk3(u, b13)
        if b16 != b15:
            a1 += 1
            b11.append([v, u, b2])
            fonk4(b13, b16, b15, b14)
    return b11
def fonk6(b24):
    b17 = set()
    with open(b24) as f:
        for line in f:
            b18 = line.strip().split(' ')
            b17.add(b18[0])
            b17.add(b18[1])
    b19 = list(b17)
    b20 = len(b17)
    b21 = []
    with open(b24) as f:
        for line in f:
            b18 = line.strip().split(' ')
            b21.append([
                b19.index(b18[0]),
                b19.index(b18[1]),
                int(b18[2])])
    b11 = fonk5(b21, b20)
    b22 = sum(b3[2] for b3 in b11)
    print("The minimum spanning tree is as follows:")
    for b3 in b11:
        print(f"{b19[b3[0]]} to {b19[b3[1]]} = {b3[2]} miles")
    print(f"b22 b2: {b22} miles.")
    fonk1(b11, b19)
if b23 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        sys.exit(1)
    b24 = sys.argv[1]
    fonk6(b24)