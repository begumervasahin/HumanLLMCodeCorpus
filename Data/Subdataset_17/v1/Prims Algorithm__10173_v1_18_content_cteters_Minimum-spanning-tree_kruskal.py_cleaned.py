import matplotlib.pyplot as plt
import networkx as nx
import sys
def displayGraph(MST_list, vert_list):
    G = nx.Graph()
    for edge in MST_list:
        G.add_edge(
                vert_list[edge[0]],
                vert_list[edge[1]],
                weight=int(edge[2]))
    edge = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G, k=20, iterations=150, weight='weight', scale=1.0)
    weight = dict(map(lambda x: ((x[0], x[1]), str(x[2]['weight'])), G.edges(data=True)))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
    node_size = max(len(vert_list) * 180, 100)
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=edge, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def sortEdge(wc_graph):
    return sorted(wc_graph, key=lambda x: x[2])
def find(root, parent):
    while root != parent[root]:
        root = parent[root]
    return root
def union(parent, rootv, rootu, size):
    if size[rootv] > size[rootu]:
        parent[rootu] = rootv
    elif size[rootv] < size[rootu]:
        parent[rootv] = rootu
    else:
        parent[rootu] = rootv
        size[rootv] += 1
def kruskal(wc_graph, vert_cout):
    MST_list = []
    sort_graph = sortEdge(wc_graph)
    parent = list(range(vert_cout))
    size = [0] * vert_cout
    encounter = 0
    k = 0
    while encounter < (vert_cout - 1) and k < len(sort_graph):
        v, u, weight = sort_graph[k]
        k += 1
        rootu = find(v, parent)
        rootv = find(u, parent)
        if rootv != rootu:
            encounter += 1
            MST_list.append([v, u, weight])
            union(parent, rootv, rootu, size)
    return MST_list
def main(file_name):
    vert_set = set()
    with open(file_name) as f:
        for line in f:
            column = line.strip().split(' ')
            vert_set.add(column[0])
            vert_set.add(column[1])
    vert_list = list(vert_set)
    vert_cout = len(vert_set)
    wc_graph = []
    with open(file_name) as f:
        for line in f:
            column = line.strip().split(' ')
            wc_graph.append([
                vert_list.index(column[0]),
                vert_list.index(column[1]),
                int(column[2])])
    MST_list = kruskal(wc_graph, vert_cout)
    total = sum(edge[2] for edge in MST_list)
    print("The minimum spanning tree is as follows:")
    for edge in MST_list:
        print(f"{vert_list[edge[0]]} to {vert_list[edge[1]]} = {edge[2]} miles")
    print(f"total weight: {total} miles.")
    displayGraph(MST_list, vert_list)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        sys.exit(1)
    file_name = sys.argv[1]
    main(file_name)