import matplotlib.pyplot as plt
import networkx as nx
def sort_edges(weighted_graph):
    return sorted(weighted_graph, key=lambda x: x[2])
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]
def union(parent, rank, root1, root2):
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        rank[root1] += 1
def kruskal(weighted_graph, num_vertices):
    mst = []
    sorted_edges = sort_edges(weighted_graph)
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    for edge in sorted_edges:
        v, u, weight = edge
        root_v = find(parent, v)
        root_u = find(parent, u)
        if root_v != root_u:
            mst.append(edge)
            union(parent, rank, root_v, root_u)
    return mst
def draw_graph(mst, vertices):
    graph = nx.Graph()
    for edge in mst:
        graph.add_edge(vertices[edge[0]], vertices[edge[1]], weight=edge[2])
    pos = nx.spring_layout(graph, k=20, iterations=150)
    weights = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)
    plt.show()
def main(file_name):
    vertices = set()
    weighted_graph = []
    with open(file_name) as file:
        for line in file:
            v1, v2, weight = line.strip().split()
            vertices.add(v1)
            vertices.add(v2)
            weighted_graph.append((v1, v2, int(weight)))
    vertex_list = list(vertices)
    vertex_count = len(vertex_list)
    indexed_graph = [(vertex_list.index(v1), vertex_list.index(v2), weight) for v1, v2, weight in weighted_graph]
    mst = kruskal(indexed_graph, vertex_count)
    total_weight = sum(edge[2] for edge in mst)
    print("The minimum spanning tree:")
    for edge in mst:
        print(f"{vertex_list[edge[0]]} to {vertex_list[edge[1]]} = {edge[2]} units.")
    print(f"Total weight: {total_weight} units.")
    draw_graph(mst, vertex_list)
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    file_name = sys.argv[1]
    main(file_name)