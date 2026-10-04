from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
def display_graph(matrix):
    G = nx.Graph()
    for edge in matrix:
        G.add_edge(nod_list[edge[0]], nod_list[edge[1]], weight=int(edge[2]))
    pos = nx.spring_layout(G, k=40)
    edge_labels = dict(map(lambda x: ((x[0], x[1]), str(x[2]['weight'])), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, alpha=0.7)
    node_size = max(len(nod) for nod in nod_list) * 110
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.subplots_adjust(left=0.00, bottom=0.00, right=1.00, top=1.00, wspace=0.2, hspace=0.2)
    plt.figure(1, figsize=(10, 10))
    plt.show()
def getPrim(g_matrix):
    mst_edges = []
    in_mst = [False] * nod_count
    edge_count = 0
    in_mst[0] = True
    while edge_count < nod_count - 1:
        min_val = float('inf')
        x = y = 0
        for i in range(nod_count):
            if in_mst[i]:
                for j in range(nod_count):
                    if not in_mst[j] and g_matrix[i][j]:
                        if g_matrix[i][j] < min_val:
                            min_val = g_matrix[i][j]
                            x, y = i, j
        mst_edges.append([x, y, g_matrix[x][y]])
        in_mst[y] = True
        edge_count += 1
    return mst_edges
file_name = "city-pairs.txt"
node_set = set()
with open(file_name) as f:
    for line in f:
        columns = line.strip().split(' ')
        node_set.add(columns[0])
        node_set.add(columns[1])
node_list = list(node_set)
nod_count = len(node_set)
g_matrix = [[0 for _ in range(nod_count)] for _ in range(nod_count)]
with open(file_name) as f:
    for line in f:
        columns = line.strip().split(' ')
        i, j, weight = node_list.index(columns[0]), node_list.index(columns[1]), int(columns[2])
        g_matrix[i][j] = weight
        g_matrix[j][i] = weight
print("Adjacency Matrix:")
for row in g_matrix:
    print(' '.join(f"{val:4}" for val in row))
mst_edges = getPrim(g_matrix)
total_miles = sum(edge[2] for edge in mst_edges)
print("\nMinimum Spanning Tree:")
for edge in mst_edges:
    print(f"From {node_list[edge[0]]} to {node_list[edge[1]]} = {edge[2]} miles")
print(f"Total number of miles: {total_miles}")
display_graph(mst_edges)