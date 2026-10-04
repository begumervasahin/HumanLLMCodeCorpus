import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b9, b18):
    b1 = nx.Graph()
    for edge in b9:
        b1.add_edge(
            b18[edge[0]],
            b18[edge[1]],
            b2 = edge[2]
        )
    b3 = nx.spring_layout(b1, k=20, iterations=150)
    b4 = nx.get_edge_attributes(b1, 'b2')
    nx.draw(b1, b3, b5 = True, node_size=700, node_color='lightblue', font_size=10)
    nx.draw_networkx_edge_labels(b1, b3, b6 = b4)
    plt.show()
def fonk2(b20):
    return sorted(b20, b7 = lambda x: x[2])
def fonk3(b8, b11):
    while b8 != b11[b8]:
        b8 = b11[b8]
    return b8
def fonk4(b11, b13, b14, b12):
    if b12[b13] > b12[b14]:
        b11[b14] = b13
    elif b12[b13] < b12[b14]:
        b11[b13] = b14
    else:
        b11[b14] = b13
        b12[b13] += 1
def fonk5(b20, b19):
    b9 = []
    b10 = fonk2(b20)
    b11 = list(range(b19))
    b12 = [0] * b19
    a1 = 0
    a2 = 0
    while a1 < (b19 - 1):
        v, u, b2 = b10[a2]
        a2 += 1
        b13 = fonk3(v, b11)
        b14 = fonk3(u, b11)
        if b13 != b14:
            a1 += 1
            b9.append([v, u, b2])
            fonk4(b11, b13, b14, b12)
    return b9
def fonk6():
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        return
    b15 = sys.argv[1]
    b16 = set()
    with open(b15) as file:
        for line in file:
            v1, v2, b17 = line.strip().split()
            b16.add(v1)
            b16.add(v2)
    b18 = list(b16)
    b19 = len(b18)
    b20 = []
    with open(b15) as file:
        for line in file:
            v1, v2, b2 = line.strip().split()
            b20.append([
                b18.a2(v1),
                b18.a2(v2),
                int(b2)
            ])
    b9 = fonk5(b20, b19)
    b21 = sum(edge[2] for edge in b9)
    print("The minimum spanning tree is as follows:")
    for edge in b9:
        print(f"{b18[edge[0]]} to {b18[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b21} miles.")
    fonk1(b9, b18)
if b22 = = "__main__":
    fonk6()