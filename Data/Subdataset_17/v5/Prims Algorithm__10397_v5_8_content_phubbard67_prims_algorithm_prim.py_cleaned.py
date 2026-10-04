from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
def display_graph(matrix):
    G = nx.Graph()
    for edge in matrix:
        G.add_edge(node_list[edge[0]], node_list[edge[1]], weight=int(edge[2]))
    pos = nx.spring_layout(G, k=40)
    edge_labels = { (u, v): str(d['weight']) for u, v, d in G.edges(data=True) }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, alpha=0.7)
    node_size = max(len(node) for node in node_list) * 110
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.subplots_adjust(left=0.00, bottom=0.00, right=1.00, top=1.00, wspace=0.2, hspace=0.2)
    plt.figure(1, figsize=(10, 10))
    plt.show()
def prim_algorithm(graph_matrix):
    mst_edges = []
    in_mst = [False] * node_count
    in_mst[0] = True
    while len(mst_edges) < node_count - 1:
        min_val = float('inf')
        x = y = -1
        for i in range(node_count):
            if in_mst[i]:
                for j in range(node_count):
                    if not in_mst[j] and graph_matrix[i][j] and graph_matrix[i][j] < min_val:
                        min_val = graph_matrix[i][j]
                        x, y = i, j
        mst_edges.append([x, y, graph_matrix[x][y]])
        in_mst[y] = True
    return mst_edges
file_name = "city-pairs.txt"
node_set = set()
with open(file_name) as f:
    for line in f:
        city1, city2, _ = line.strip().split(' ')
        node_set.add(city1)
        node_set.add(city2)
node_list = list(node_set)
node_count = len(node_set)
graph_matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]
with open(file_name) as f:
    for line in f:
        city1, city2, weight = line.strip().split(' ')
        i, j = node_list.index(city1), node_list.index(city2)
        graph_matrix[i][j] = graph_matrix[j][i] = int(weight)
print("Adjacency Matrix:")
for row in graph_matrix:
    print(' '.join(f"{val:4}" for val in row))
mst_edges = prim_algorithm(graph_matrix)
total_miles = sum(edge[2] for edge in mst_edges)
print("\nMinimum Spanning Tree:")
for edge in mst_edges:
    print(f"From {node_list[edge[0]]} to {node_list[edge[1]]} = {edge[2]} miles")
print(f"Total number of miles: {total_miles}")
display_graph(mst_edges)