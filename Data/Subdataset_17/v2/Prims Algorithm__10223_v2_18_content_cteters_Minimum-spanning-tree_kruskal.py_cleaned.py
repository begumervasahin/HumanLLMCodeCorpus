import matplotlib.pyplot as plt
import networkx as nx
import sys
def display_graph(MST_list, vert_list):
    G = nx.Graph()
    for edge in MST_list:
        G.add_edge(vert_list[edge[0]], vert_list[edge[1]], weight=int(edge[2]))
    pos = nx.spring_layout(G, k=20, iterations=150, weight='weight', scale=1.0)
    edge_labels = { (u, v): str(d['weight']) for u, v, d in G.edges(data=True) }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    node_size = max(len(vert_list) * 180, 100)
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def sort_edges(wc_graph):
    return sorted(wc_graph, key=lambda x: x[2])
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
def kruskal(wc_graph, vert_count):
    MST_list = []
    sorted_graph = sort_edges(wc_graph)
    parent = list(range(vert_count))
    rank = [0] * vert_count
    for edge in sorted_graph:
        u, v, weight = edge
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            MST_list.append(edge)
            union(parent, rank, root_u, root_v)
            if len(MST_list) == vert_count - 1:
                break
    return MST_list
def main(file_name):
    with open(file_name) as f:
        edges = [line.strip().split() for line in f]
    vert_set = {edge[0] for edge in edges} | {edge[1] for edge in edges}
    vert_list = list(vert_set)
    vert_count = len(vert_set)
    wc_graph = [[vert_list.index(edge[0]), vert_list.index(edge[1]), int(edge[2])] for edge in edges]
    MST_list = kruskal(wc_graph, vert_count)
    total_weight = sum(edge[2] for edge in MST_list)
    print("The minimum spanning tree is as follows:")
    for edge in MST_list:
        print(f"{vert_list[edge[0]]} to {vert_list[edge[1]]} = {edge[2]} miles")
    print(f"Total weight: {total_weight} miles.")
    display_graph(MST_list, vert_list)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        sys.exit(1)
    main(sys.argv[1])