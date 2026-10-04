import matplotlib.pyplot as plt
import networkx as nx
def display_graph(matrix, node_list):
    G = nx.Graph()
    for edge in matrix:
        G.add_edge(node_list[edge[0]], node_list[edge[1]], weight=int(edge[2]))
    pos = nx.spring_layout(G, k=0.5)
    edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, alpha=0.7)
    node_size = max(len(node) for node in node_list) * 110
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def prim_algorithm(adj_matrix, node_count):
    selected_edges = []
    selected_nodes = [False] * node_count
    selected_nodes[0] = True
    for _ in range(node_count - 1):
        min_edge = (None, None, float('inf'))
        for i in range(node_count):
            if selected_nodes[i]:
                for j in range(node_count):
                    if not selected_nodes[j] and adj_matrix[i][j] > 0:
                        if adj_matrix[i][j] < min_edge[2]:
                            min_edge = (i, j, adj_matrix[i][j])
        selected_nodes[min_edge[1]] = True
        selected_edges.append(min_edge)
    return selected_edges
def read_city_pairs(file_name):
    nodes = set()
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            city1, city2, _ = line.strip().split()
            nodes.add(city1)
            nodes.add(city2)
    return list(nodes), lines
def create_adj_matrix(node_list, lines):
    node_count = len(node_list)
    adj_matrix = [[0] * node_count for _ in range(node_count)]
    for line in lines:
        city1, city2, distance = line.strip().split()
        i, j = node_list.index(city1), node_list.index(city2)
        adj_matrix[i][j] = adj_matrix[j][i] = int(distance)
    return adj_matrix
def main():
    file_name = "city-pairs.txt"
    node_list, lines = read_city_pairs(file_name)
    adj_matrix = create_adj_matrix(node_list, lines)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(' '.join(f"{val:4}" for val in row))
    print()
    prim_edges = prim_algorithm(adj_matrix, len(node_list))
    total_miles = sum(edge[2] for edge in prim_edges)
    for edge in prim_edges:
        print(f"From {node_list[edge[0]]} to {node_list[edge[1]]} = {edge[2]} miles")
    print(f"Total number of miles: {total_miles}")
    display_graph(prim_edges, node_list)
if __name__ == "__main__":
    main()