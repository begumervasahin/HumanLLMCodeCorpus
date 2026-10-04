import matplotlib.pyplot as plt
import networkx as nx
import sys
def prim(weighted_graph):
    vert_count = len(weighted_graph)
    listMST = []
    visited = []
    edge_list = []
    min_edge = [0, 1, weighted_graph[0][1]]
    v = 0
    for _ in range(vert_count - 1):
        visited.append(v)
        for u in range(vert_count):
            if weighted_graph[v][u] != 0:
                edge_list.append([v, u, weighted_graph[v][u]])
        for e in range(1, len(edge_list)):
            if edge_list[e][2] < min_edge[2] and edge_list[e][1] not in visited:
                min_edge = edge_list[e]
        listMST.append(min_edge)
        v = min_edge[1]
        edge_list.remove(min_edge)
        if edge_list:
            min_edge = edge_list[0]
    return listMST
def draw_graph(listMST, vert_list):
    G = nx.Graph()
    for edge in listMST:
        G.add_edge(vert_list[edge[0]], vert_list[edge[1]], weight=edge[2])
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()
def main(file_name):
    vert_set = set()
    with open(file_name) as f:
        for line in f:
            columns = line.strip().split()
            vert_set.add(columns[0])
            vert_set.add(columns[1])
    vert_list = list(vert_set)
    vert_count = len(vert_list)
    weighted_graph = [[0] * vert_count for _ in range(vert_count)]
    with open(file_name) as f:
        for line in f:
            columns = line.strip().split()
            i, j, weight = vert_list.index(columns[0]), vert_list.index(columns[1]), int(columns[2])
            weighted_graph[i][j] = weight
            weighted_graph[j][i] = weight
    listMST = prim(weighted_graph)
    total_weight = sum(edge[2] for edge in listMST)
    print("The minimum spanning tree:")
    for edge in listMST:
        print(f"{vert_list[edge[0]]} to {vert_list[edge[1]]} = {edge[2]} units")
    print(f"Total weight: {total_weight} units")
    draw_graph(listMST, vert_list)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        main(sys.argv[1])