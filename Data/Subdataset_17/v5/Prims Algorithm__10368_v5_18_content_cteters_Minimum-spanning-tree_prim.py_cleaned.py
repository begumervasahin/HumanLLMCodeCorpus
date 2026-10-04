import matplotlib.pyplot as plt
import networkx as nx
import sys
def display_graph(mst_edges, vertices):
    G = nx.Graph()
    for edge in mst_edges:
        G.add_edge(vertices[edge[0]], vertices[edge[1]], weight=edge[2])
    pos = nx.spring_layout(G, k=20, iterations=150, weight='weight')
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    node_size = max(len(vertex) for vertex in vertices) * 180
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def prim_algorithm(weighted_graph, vertex_count):
    mst_edges = []
    visited = []
    edges = []
    min_edge = [0, 1, weighted_graph[0][1]]
    current_vertex = 0
    for _ in range(vertex_count - 1):
        visited.append(current_vertex)
        for neighbor in range(vertex_count):
            if weighted_graph[current_vertex][neighbor] != 0:
                edges.append([current_vertex, neighbor, weighted_graph[current_vertex][neighbor]])
        for edge in edges[1:]:
            if edge[2] < min_edge[2] and edge[1] not in visited:
                min_edge = edge
        mst_edges.append(min_edge)
        current_vertex = min_edge[1]
        edges.remove(min_edge)
        if edges:
            min_edge = edges[0]
    return mst_edges
def main(file_name):
    vertices = set()
    with open(file_name) as file:
        for line in file:
            src, dest, _ = line.strip().split(' ')
            vertices.add(src)
            vertices.add(dest)
    vertex_list = list(vertices)
    vertex_count = len(vertices)
    weighted_graph = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    with open(file_name) as file:
        for line in file:
            src, dest, weight = line.strip().split(' ')
            idx1, idx2 = vertex_list.index(src), vertex_list.index(dest)
            weight = int(weight)
            weighted_graph[idx1][idx2] = weight
            weighted_graph[idx2][idx1] = weight
    mst_edges = prim_algorithm(weighted_graph, vertex_count)
    total_weight = sum(edge[2] for edge in mst_edges)
    print("The minimum spanning tree is as follows:")
    for edge in mst_edges:
        print(f"{vertex_list[edge[0]]} to {vertex_list[edge[1]]} = {edge[2]} miles")
    print(f"Total weight: {total_weight} miles.")
    display_graph(mst_edges, vertex_list)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py <file_name>")
        sys.exit(1)
    input_file_name = sys.argv[1]
    main(input_file_name)