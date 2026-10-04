import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b16):
    b1 = sorted(b16, key=lambda x: x[2])
    return b1
def fonk2(b2, b4):
    while b2 != b4[b2]:
        b2 = b4[b2]
    return b2
def fonk3(b4, b8, b7, b5):
    if b5[b8] > b5[b7]:
        b4[b7] = b8
    elif b5[b8] < b5[b7]:
        b4[b8] = b7
    else:
        b4[b7] = b8
        b5[b8] += 1
def fonk4(b16, b18):
    b3 = []
    b1 = fonk1(b16)
    b4 = list(range(b18))
    b5 = [0] * b18
    a1 = 0
    a2 = 0
    while a1 < b18 - 1:
        v, u, b6 = b1[a2]
        a2 += 1
        b7 = fonk2(v, b4)
        b8 = fonk2(u, b4)
        if b8 != b7:
            a1 += 1
            b3.append([v, u, b6])
            fonk3(b4, b8, b7, b5)
    return b3
def fonk5(b3, b17):
    b9 = nx.Graph()
    for edge in b3:
        b9.add_edge(b17[edge[0]], b17[edge[1]], b6 = edge[2])
    b10 = nx.spring_layout(b9, a2=20, iterations=150)
    b11 = {(u, v): f"{d['b6']}" for u, v, d in b9.edges(data=True)}
    nx.draw_networkx(b9, b10, b12 = True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b9, b10, b11 = b11)
    plt.axis('off')
    plt.show()
if b13 = = "__main__":
    b14 = sys.argv[1]
    b15 = set()
    b16 = []
    with open(b14) as f:
        for line in f:
            v1, v2, b6 = line.strip().split(' ')
            b15.add(v1)
            b15.add(v2)
            b16.append((v1, v2, int(b6)))
    b17 = list(b15)
    b18 = len(b15)
    b19 = [(b17.index(v1), b17.index(v2), b6) for v1, v2, b6 in b16]
    b3 = fonk4(b19, b18)
    b20 = sum(b6 for _, _, b6 in b3)
    print("The minimum spanning tree:")
    for v1, v2, b6 in b3:
        print(f"{b17[v1]} to {b17[v2]} = {b6} units")
    print(f"Total b6: {b20} units")
    fonk5(b3, b17)