import matplotlib.pyplot as plt
import networkx as nx
import sys
def prim(weighted_graph, vert_count):
    listMST = []
    visited = []
    edge_list = []
    min_edge = [0, 1, weighted_graph[0][1]]
    current_vertex = 0
    for _ in range(vert_count - 1):
        visited.append(current_vertex)
        for neighbor in range(vert_count):
            if weighted_graph[current_vertex][neighbor] != 0:
                edge_list.append([current_vertex, neighbor, weighted_graph[current_vertex][neighbor]])
        for edge in edge_list:
            if edge[2] < min_edge[2] and edge[1] not in visited:
                min_edge = edge
        listMST.append(min_edge)
        current_vertex = min_edge[1]
        edge_list.remove(min_edge)
        if edge_list:
            min_edge = edge_list[0]
    return listMST
def draw_graph(listMST, vert_list, vert_count):
    G = nx.Graph()
    for edge in listMST:
        G.add_edge(
            vert_list[edge[0]],
            vert_list[edge[1]],
            weight=int(edge[2])
        )
    pos = nx.spring_layout(G, k=20, iterations=150, scale=1.0)
    weights = dict(((u, v), str(d['weight'])) for u, v, d in G.edges(data=True))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color='black', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def read_graph_from_file(file_name):
    vert_set = set()
    edges = []
    with open(file_name) as f:
        for line in f:
            column = line.strip().split(' ')
            vert_set.add(column[0])
            vert_set.add(column[1])
            edges.append((column[0], column[1], int(column[2])))
    vert_list = list(vert_set)
    vert_count = len(vert_set)
    weighted_graph = [[0 for _ in range(vert_count)] for _ in range(vert_count)]
    for edge in edges:
        u = vert_list.index(edge[0])
        v = vert_list.index(edge[1])
        weight = edge[2]
        weighted_graph[u][v] = weight
        weighted_graph[v][u] = weight
    return weighted_graph, vert_list, vert_count
if __name__ == "__main__":
    file_name = sys.argv[1]
    weighted_graph, vert_list, vert_count = read_graph_from_file(file_name)
    listMST = prim(weighted_graph, vert_count)
    total_weight = sum(edge[2] for edge in listMST)
    print("The minimum spanning tree:")
    for edge in listMST:
        print(f"{vert_list[edge[0]]} to {vert_list[edge[1]]} = {edge[2]} units.")
    print(f"Total weight: {total_weight} units.")
    draw_graph(listMST, vert_list, vert_count)