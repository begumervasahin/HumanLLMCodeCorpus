from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
def fonk1(matrix):
    b1 = nx.Graph()
    for edge in matrix:
        b1.add_edge(nod_list[edge[0]], nod_list[edge[1]], b2 = int(edge[2]))
    b3 = nx.spring_layout(b1, k=40)
    b4 = dict(map(lambda b13: ((b13[0], b13[1]), str(b13[2]['b2'])), b1.edges(data=True)))
    nx.draw_networkx_edge_labels(b1, b3, b4 = b4, b7=7, alpha=0.7)
    b5 = max(len(nod) for nod in nod_list) * 110
    nx.draw_networkx_nodes(b1, b3, b5 = b5, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b3, b6 = 2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b3, b7 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.subplots_adjust(b8 = 0.00, bottom=0.00, right=1.00, top=1.00, wspace=0.2, hspace=0.2)
    plt.figure(1, b9 = (10, 10))
    plt.show()
def fonk2(b20):
    b10 = []
    b11 = [False] * b19
    a1 = 0
    b11[0] = True
    while a1 < b19 - 1:
        b12 = float('inf')
        b13 = b14 = 0
        for i in range(b19):
            if b11[i]:
                for j in range(b19):
                    if not b11[j] and b20[i][j]:
                        if b20[i][j] < b12:
                            b12 = b20[i][j]
                            b13, b14 = i, j
        b10.append([b13, b14, b20[b13][b14]])
        b11[b14] = True
        a1 += 1
    return b10
b15 = "city-pairs.txt"
b16 = set()
with open(b15) as f:
    for line in f:
        b17 = line.strip().split(' ')
        b16.add(b17[0])
        b16.add(b17[1])
b18 = list(b16)
b19 = len(b16)
b20 = [[0 for _ in range(b19)] for _ in range(b19)]
with open(b15) as f:
    for line in f:
        b17 = line.strip().split(' ')
        i, j, b2 = b18.index(b17[0]), b18.index(b17[1]), int(b17[2])
        b20[i][j] = b2
        b20[j][i] = b2
print("Adjacency Matrix:")
for row in b20:
    print(' '.join(f"{val:4}" for val in row))
b10 = fonk2(b20)
b21 = sum(edge[2] for edge in b10)
print("\nMinimum Spanning Tree:")
for edge in b10:
    print(f"From {b18[edge[0]]} to {b18[edge[1]]} = {edge[2]} miles")
print(f"Total number of miles: {b21}")
fonk1(b10)