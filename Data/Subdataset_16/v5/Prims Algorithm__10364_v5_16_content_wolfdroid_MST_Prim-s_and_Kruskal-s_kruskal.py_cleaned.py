import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b14):
    return sorted(b14, b1 = lambda x: x[2])
def fonk2(root, b4):
    if root != b4[root]:
        b4[root] = fonk2(b4[root], b4)
    return b4[root]
def fonk3(b4, b8, b7, b5):
    if b5[b8] > b5[b7]:
        b4[b7] = b8
    elif b5[b8] < b5[b7]:
        b4[b8] = b7
    else:
        b4[b7] = b8
        b5[b8] += 1
def fonk4(b14, b16):
    b2 = []
    b3 = fonk1(b14)
    b4 = list(range(b16))
    b5 = [0] * b16
    a1 = 0
    a2 = 0
    while a1 < b16 - 1:
        v, u, b6 = b3[a2]
        a2 += 1
        b7 = fonk2(v, b4)
        b8 = fonk2(u, b4)
        if b8 != b7:
            a1 += 1
            b2.append([v, u, b6])
            fonk3(b4, b8, b7, b5)
    return b2
def fonk5(b2, b15):
    b9 = nx.Graph()
    for edge in b2:
        b9.add_edge(b15[edge[0]], b15[edge[1]], b6 = edge[2])
    b10 = nx.spring_layout(b9, a2=20, iterations=150)
    b11 = {(u, v): f"{d['b6']}" for u, v, d in b9.edges(data=True)}
    nx.draw_networkx(b9, b10, b12 = True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b9, b10, b11 = b11)
    plt.axis('off')
    plt.show()
def fonk6(b19):
    b13 = set()
    b14 = []
    with open(b19) as f:
        for line in f:
            v1, v2, b6 = line.strip().split(' ')
            b13.add(v1)
            b13.add(v2)
            b14.append((v1, v2, int(b6)))
    b15 = list(b13)
    b16 = len(b13)
    b17 = [(b15.index(v1), b15.index(v2), b6) for v1, v2, b6 in b14]
    return b17, b15, b16
if b18 = = "__main__":
    b19 = sys.argv[1]
    b17, b15, b16 = fonk6(b19)
    b2 = fonk4(b17, b16)
    b20 = sum(b6 for _, _, b6 in b2)
    print("The minimum spanning tree:")
    for v1, v2, b6 in b2:
        print(f"{b15[v1]} to {b15[v2]} = {b6} units")
    print(f"Total b6: {b20} units")
    fonk5(b2, b15)