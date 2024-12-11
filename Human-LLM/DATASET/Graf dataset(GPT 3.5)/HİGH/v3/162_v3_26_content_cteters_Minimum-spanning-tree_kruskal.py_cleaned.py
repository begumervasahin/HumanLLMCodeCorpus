import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b10, b17):
    b1 = nx.Graph()
    for edge in b10:
        b1.add_edge(b17[edge[0]], b17[edge[1]], b2 = int(edge[2]))
    b3 = {(u, v): str(d['b2']) for u, v, d in b1.edges(data=True)}
    b4 = nx.spring_layout(b1, a2=20, iterations=150)
    nx.draw_networkx_nodes(b1, b4, b5 = 300, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b6 = 2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b7 = 9, font_family='sans-serif')
    nx.draw_networkx_edge_labels(b1, b4, b3 = b3)
    plt.axis('off')
    plt.show()
def fonk2(graph):
    b8 = sorted(graph, key=lambda x: x[2])
    return b8
def fonk3(b9, b11):
    while b9 != b11[b9]:
        b9 = b11[b9]
    return b9
def fonk4(b11, b12, b14, b13):
    if b12[b14] > b12[b13]:
        b11[b13] = b14
    elif b12[b14] < b12[b13]:
        b11[b14] = b13
    else:
        b11[b13] = b14
        b12[b14] += 1
def fonk5(b21, b20):
    b10 = []
    b8 = fonk2(b21)
    b11 = list(range(b20))
    b12 = [0] * b20
    a1 = 0
    a2 = 0
    while a1 < (b20 - 1):
        v, u, b2 = b8[a2]
        a2 += 1
        b13 = fonk3(v, b11)
        b14 = fonk3(u, b11)
        if b14 != b13:
            a1 += 1
            b10.append([v, u, b2])
            fonk4(b11, b12, b14, b13)
    return b10
if b15 = = "__main__":
    b16 = sys.argv[1]
    b17 = set()
    with open(b16) as f:
        for line in f:
            b18 = line.strip().split(' ')
            b17.update(b18[:2])
    b19 = list(b17)
    b20 = len(b17)
    b21 = []
    with open(b16) as f:
        for line in f:
            b18 = line.strip().split(' ')
            b21.append([b19.index(b18[0]), b19.index(b18[1]), int(b18[2])])
    b10 = fonk5(b21, b20)
    a3 = 0
    print("The minimum spanning tree is as follows:")
    for edge in b10:
        print(b19[edge[0]], " to ", b19[edge[1]], " = ", edge[2], "miles")
        a3 += edge[2]
    print("Total b2: ", a3, " miles.")
    fonk1(b10, b19)