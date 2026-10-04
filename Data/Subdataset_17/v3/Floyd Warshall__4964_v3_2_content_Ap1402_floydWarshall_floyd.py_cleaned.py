from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def floyd_warshall(graph):
    distance_matrix = deepcopy(graph)
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                new_distance = distance_matrix[i][k] + distance_matrix[k][j]
                if distance_matrix[i][j] > new_distance:
                    distance_matrix[i][j] = new_distance
    return distance_matrix
def print_matrix(matrix):
    for row in matrix:
        formatted_row = " , ".join(map(str, row))
        print(formatted_row)
        print("")
def request_graph_data():
    INFINITY = 99999
    graph = nx.DiGraph()
    print("Create Adjacency Matrix")
    num_vertices = int(input("Number of vertices: "))
    adjacency_matrix = []
    for v1 in range(num_vertices):
        adjacency_matrix.append([])
        for v2 in range(num_vertices):
            if v1 == v2:
                adjacency_matrix[v1].append(0)
            else:
                distance = input(f"Distance from {v1 + 1} to {v2 + 1} (leave blank for no direct path): ")
                if distance == '':
                    adjacency_matrix[v1].append(INFINITY)
                else:
                    distance = int(distance)
                    adjacency_matrix[v1].append(distance)
                    graph.add_edge(v1, v2, weight=distance)
    return adjacency_matrix, graph
def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()
def main():
    adjacency_matrix, graph_networkx = request_graph_data()
    shortest_paths_matrix = floyd_warshall(adjacency_matrix)
    print("Shortest Path Matrix:")
    print_matrix(shortest_paths_matrix)
    visualize_graph(graph_networkx)
if __name__ == '__main__':
    main()