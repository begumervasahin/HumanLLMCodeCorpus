import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b9, b18):
    b1 = nx.Graph()
    for u, v, b2 in b9:
        b1.add_edge(b18[u], b18[v], b2 = b2)
    b3 = nx.spring_layout(b1)
    b4 = {(u, v): str(d['b2']) for u, v, d in b1.edges(data=True)}
    nx.draw(b1, b3, b5 = True, b4={node: node for node in b1.nodes()}, font_size=9)
    nx.draw_networkx_edge_labels(b1, b3, b6 = b4)
    plt.axis('off')
    plt.show()
def fonk2(edges):
    return sorted(edges, b7 = lambda x: x[2])
def fonk3(b8, b11):
    while b8 != b11[b8]:
        b8 = b11[b8]
    return b8
def fonk4(b11, b12, b14, b13):
    if b12[b14] > b12[b13]:
        b11[b13] = b14
    elif b12[b14] < b12[b13]:
        b11[b14] = b13
    else:
        b11[b13] = b14
        b12[b14] += 1
def fonk5(b10, b19):
    b9 = []
    b10 = fonk2(b10)
    b11 = list(range(b19))
    b12 = [0] * b19
    a1 = 0
    for u, v, b2 in b10:
        b13 = fonk3(u, b11)
        b14 = fonk3(v, b11)
        if b14 != b13:
            a1 += 1
            b9.append([u, v, b2])
            fonk4(b11, b12, b14, b13)
        if a1 = = b19 - 1:
            break
    return b9
def fonk6():
    if len(sys.argv) < 2:
        print("Usage: python prim.py <input_file>")
        return
    b15 = sys.argv[1]
    b16 = set()
    b10 = []
    with open(b15) as f:
        for line in f:
            b17 = line.strip().split(' ')
            b16.update(b17[:2])
            b10.append([int(b17[0]), int(b17[1]), int(b17[2])])
    b18 = sorted(b16)
    b19 = len(b18)
    b9 = fonk5(b10, b19)
    b20 = sum(b2 for _, _, b2 in b9)
    print("The minimum spanning tree is as follows:")
    for u, v, b2 in b9:
        print(f"{b18[u]} to {b18[v]} = {b2} miles")
    print("Total b2:", b20, "miles.")
    fonk1(b9, b18)
if b21 = = "__main__":
    fonk6()