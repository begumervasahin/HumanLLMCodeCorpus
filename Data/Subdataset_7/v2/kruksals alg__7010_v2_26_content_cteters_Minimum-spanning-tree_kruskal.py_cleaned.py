import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b15, b26):
    b1 = nx.Graph()
    for i in range(len(b15)):
        b1.add_edge(
            b26[b15[i][0]],
            b26[b15[i][1]],
            b2 = int(b15[i][2]))
    b3 = [(b19, b18) for (b19, b18, d) in b1.edges(data=True)]
    b4 = nx.spring_layout(b1, a3=20, b4=None, fixed=None, iterations=150, b2='b2', scale=1.0)
    b2 = dict(map(lambda x: ((x[0], x[1]), str(x[2]['b2'])), b1.edges(data=True)))
    nx.draw_networkx_edge_labels(b1, b4, b5 = b2)
    b6 = max(len(vert) for vert in b26)
    nx.draw_networkx_nodes(b1, b4, b7 = b6 * 180, node_shape='h', b6=100, alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b8 = b3, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b9 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b28):
    b10 = []
    b10.append(b28[0])
    b11 = b28[0]
    for i in range(1, len(b28)):
        b12 = b28[i][2]
        a1 = 0
        while b12 > b10[a1][2] and a1 < len(b10) - 1:
            a1 += 1
        b10.insert(a1, b28[i])
    b13 = b10[len(b10) - 1]
    b10.remove(b10[len(b10) - 1])
    a1 = 0
    while b13[2] > b10[a1][2] and a1 < len(b10) - 1:
        a1 += 1
    b10.insert(a1, b13)
    return b10
def fonk3(b14, b16):
    while b14 != b16[b14]:
        b14 = b16[b14]
    return b14
def fonk4(b16, b21, b20, b17):
    if b17[b21] > b17[b20]:
        b16[b20] = b21
    elif b17[b21] < b17[b20]:
        b16[b21] = b20
    else:
        b16[b20] = b21
        b17[b21] += 1
def fonk5(b28, b27):
    b15 = []
    b10 = fonk2(b28)
    b16 = list(range(b27))
    b17 = [0] * b27
    a2 = 0
    a3 = 0
    while a2 < (b27 - 1):
        b18 = b10[a3][0]
        b19 = b10[a3][1]
        a3 += 1
        b20 = fonk3(b18, b16)
        b21 = fonk3(b19, b16)
        if b21 != b20:
            a2 += 1
            b15.append([b18, b19, b10[a3][2]])
            fonk4(b16, b21, b20, b17)
    return b15
if b22 = = "__main__":
    b23 = sys.argv[1]
    b24 = set()
    with open(b23) as f:
        for i in f:
            b25 = i.strip().split(' ')
            b24.add(b25[0])
            b24.add(b25[1])
    b26 = list(b24)
    b27 = len(b24)
    b28 = []
    with open(b23) as f:
        for i in f:
            b25 = i.strip().split(' ')
            b28.append([
                int(b26.index(b25[0])),
                int(b26.index(b25[1])),
                int(b25[2])])
    b15 = fonk5(b28, b27)
    a4 = 0
    print("The minimum spanning tree is as follows:")
    for i in range(len(b15)):
        print(b26[b15[i][0]], " to ", b26[b15[i][1]], " = ", b15[i][2], "miles")
        a4 += b15[i][2]
    print("a4 b2: ", a4, " miles.")
    fonk1(b15, b26)