import matplotlib.pyplot as plt
import networkx as nx
import sys
def prim(weighted_graph):
    vert_count = len(weighted_graph)
    listMST = []
    visited = [False] * vert_count
    edge_list = []
    visited[0] = True
    for i in range(vert_count):
        if weighted_graph[0][i] != 0:
            edge_list.append((0, i, weighted_graph[0][i]))
    while len(listMST) < vert_count - 1:
        edge_list.sort(key=lambda x: x[2])
        for edge in edge_list:
            if not visited[edge[1]]:
                listMST.append(edge)
                v = edge[1]
                visited[v] = True
                break
        edge_list = [edge for edge in edge_list if not (visited[edge[0]] and visited[edge[1]])]
        for i in range(vert_count):
            if weighted_graph[v][i] != 0 and not visited[i]:
                edge_list.append((v, i, weighted_graph[v][i]))
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
def read_graph(file_name):
    vert_set = set()
    with open(file_name) as f:
        for line in f:
            u, v, _ = line.strip().split()
            vert_set.add(u)
            vert_set.add(v)
    vert_list = list(vert_set)
    vert_count = len(vert_list)
    weighted_graph = [[0] * vert_count for _ in range(vert_count)]
    with open(file_name) as f:
        for line in f:
            u, v, weight = line.strip().split()
            i, j = vert_list.index(u), vert_list.index(v)
            weighted_graph[i][j] = int(weight)
            weighted_graph[j][i] = int(weight)
    return vert_list, weighted_graph
def main(file_name):
    vert_list, weighted_graph = read_graph(file_name)
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