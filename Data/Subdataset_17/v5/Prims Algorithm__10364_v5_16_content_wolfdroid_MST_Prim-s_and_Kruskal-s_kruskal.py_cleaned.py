import matplotlib.pyplot as plt
import networkx as nx
import sys
def sort_edge(weighted_graph):
    return sorted(weighted_graph, key=lambda x: x[2])
def find(root, parent):
    if root != parent[root]:
        parent[root] = find(parent[root], parent)
    return parent[root]
def union(parent, rootv, rootu, size):
    if size[rootv] > size[rootu]:
        parent[rootu] = rootv
    elif size[rootv] < size[rootu]:
        parent[rootv] = rootu
    else:
        parent[rootu] = rootv
        size[rootv] += 1
def kruskal(weighted_graph, vert_count):
    mst = []
    sorted_graph = sort_edge(weighted_graph)
    parent = list(range(vert_count))
    size = [0] * vert_count
    edges_in_mst = 0
    k = 0
    while edges_in_mst < vert_count - 1:
        v, u, weight = sorted_graph[k]
        k += 1
        rootu = find(v, parent)
        rootv = find(u, parent)
        if rootv != rootu:
            edges_in_mst += 1
            mst.append([v, u, weight])
            union(parent, rootv, rootu, size)
    return mst
def draw_graph(mst, vert_list):
    G = nx.Graph()
    for edge in mst:
        G.add_edge(vert_list[edge[0]], vert_list[edge[1]], weight=edge[2])
    pos = nx.spring_layout(G, k=20, iterations=150)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.show()
def read_graph(file_name):
    vert_set = set()
    weighted_graph = []
    with open(file_name) as f:
        for line in f:
            v1, v2, weight = line.strip().split(' ')
            vert_set.add(v1)
            vert_set.add(v2)
            weighted_graph.append((v1, v2, int(weight)))
    vert_list = list(vert_set)
    vert_count = len(vert_set)
    indexed_graph = [(vert_list.index(v1), vert_list.index(v2), weight) for v1, v2, weight in weighted_graph]
    return indexed_graph, vert_list, vert_count
if __name__ == "__main__":
    file_name = sys.argv[1]
    indexed_graph, vert_list, vert_count = read_graph(file_name)
    mst = kruskal(indexed_graph, vert_count)
    total_weight = sum(weight for _, _, weight in mst)
    print("The minimum spanning tree:")
    for v1, v2, weight in mst:
        print(f"{vert_list[v1]} to {vert_list[v2]} = {weight} units")
    print(f"Total weight: {total_weight} units")
    draw_graph(mst, vert_list)