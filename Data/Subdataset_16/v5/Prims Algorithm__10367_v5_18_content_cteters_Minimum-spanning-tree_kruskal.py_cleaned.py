import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b8, b17):
    b1 = nx.Graph()
    for edge in b8:
        b1.add_edge(b17[edge[0]], b17[edge[1]], b2 = edge[2])
    b3 = nx.spring_layout(b1, k=20, iterations=150)
    b4 = nx.get_edge_attributes(b1, 'b2')
    nx.draw(b1, b3, b5 = True, node_size=700, node_color='lightblue', font_size=10)
    nx.draw_networkx_edge_labels(b1, b3, b6 = b4)
    plt.show()
def fonk2(b19):
    return sorted(b19, b7 = lambda x: x[2])
def fonk3(b10, node):
    if b10[node] != node:
        b10[node] = fonk3(b10, b10[node])
    return b10[node]
def fonk4(b10, b11, root1, root2):
    if b11[root1] > b11[root2]:
        b10[root2] = root1
    elif b11[root1] < b11[root2]:
        b10[root1] = root2
    else:
        b10[root2] = root1
        b11[root1] += 1
def fonk5(b19, b18):
    b8 = []
    b9 = fonk2(b19)
    b10 = list(range(b18))
    b11 = [0] * b18
    a1 = 0
    a2 = 0
    while a1 < b18 - 1:
        v, u, b2 = b9[a2]
        a2 += 1
        b12 = fonk3(b10, v)
        b13 = fonk3(b10, u)
        if b12 != b13:
            a1 += 1
            b8.append([v, u, b2])
            fonk4(b10, b11, b12, b13)
    return b8
def fonk6():
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        return
    b14 = sys.argv[1]
    b15 = set()
    with open(b14) as file:
        for line in file:
            v1, v2, b16 = line.strip().split()
            b15.add(v1)
            b15.add(v2)
    b17 = list(b15)
    b18 = len(b17)
    b19 = []
    with open(b14) as file:
        for line in file:
            v1, v2, b2 = line.strip().split()
            b19.append([b17.a2(v1), b17.a2(v2), int(b2)])
    b8 = fonk5(b19, b18)
    b20 = sum(edge[2] for edge in b8)
    print("The minimum spanning tree is as follows:")
    for edge in b8:
        print(f"{b17[edge[0]]} to {b17[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b20} miles.")
    fonk1(b8, b17)
if b21 = = "__main__":
    fonk6()