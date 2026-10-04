import matplotlib.pyplot as plt
import networkx as nx
import sys
def displayGraph(MST_list, vert_list):
    G = nx.Graph()
    for edge in MST_list:
        G.add_edge(vert_list[edge[0]], vert_list[edge[1]], weight=edge[2])
    pos = nx.spring_layout(G, k=1.0, iterations=150)
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title("Minimum Spanning Tree")
    plt.show()
def prim(wc_graph, vert_count):
    MST_list = []
    visited_list = [False] * vert_count
    edge_list = []
    visited_list[0] = True
    for _ in range(vert_count - 1):
        min_edge = None
        for i in range(vert_count):
            if visited_list[i]:
                for j in range(vert_count):
                    if not visited_list[j] and wc_graph[i][j] != 0:
                        if min_edge is None or min_edge[2] > wc_graph[i][j]:
                            min_edge = [i, j, wc_graph[i][j]]
        if min_edge:
            MST_list.append(min_edge)
            visited_list[min_edge[1]] = True
    return MST_list
if __name__ == "__main__":
    file_name = sys.argv[1]
    vert_set = set()
    with open(file_name) as f:
        for line in f:
            column = line.strip().split()
            vert_set.add(column[0])
            vert_set.add(column[1])
    vert_list = list(vert_set)
    vert_count = len(vert_list)
    vert_index = {vert: idx for idx, vert in enumerate(vert_list)}
    wc_graph = [[0] * vert_count for _ in range(vert_count)]
    with open(file_name) as f:
        for line in f:
            column = line.strip().split()
            wc_graph[vert_index[column[0]]][vert_index[column[1]]] = int(column[2])
            wc_graph[vert_index[column[1]]][vert_index[column[0]]] = int(column[2])
    MST_list = prim(wc_graph, vert_count)
    total_weight = sum(edge[2] for edge in MST_list)
    print("The minimum spanning tree is as follows:")
    for edge in MST_list:
        print(f"{vert_list[edge[0]]} to {vert_list[edge[1]]} = {edge[2]} miles")
    print(f"Total weight: {total_weight} miles.")
    displayGraph(MST_list, vert_list)