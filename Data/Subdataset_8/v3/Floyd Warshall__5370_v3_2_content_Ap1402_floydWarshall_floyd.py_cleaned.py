from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def floyd_warshall(graph):
    shortest_paths = deepcopy(graph)
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                alternative_path = shortest_paths[i][k] + shortest_paths[k][j]
                if shortest_paths[i][j] > alternative_path:
                    shortest_paths[i][j] = alternative_path
    return shortest_paths
def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))
def get_adjacency_matrix():
    INF = float("inf")
    num_vertices = int(input("Enter the number of vertices: "))
    adjacency_matrix = []
    print("Enter the distance between vertices (use INF for infinity):")
    for v1 in range(num_vertices):
        row = []
        for v2 in range(num_vertices):
            if v1 == v2:
                row.append(0)
            else:
                distance = float(input(f"Distance from vertex {v1 + 1} to {v2 + 1}: "))
                row.append(distance if distance != INF else float("inf"))
        adjacency_matrix.append(row)
    return adjacency_matrix
if __name__ == "__main__":
    adjacency_matrix = get_adjacency_matrix()
    shortest_paths = floyd_warshall(adjacency_matrix)
    print("\nShortest path distances:")
    print_matrix(shortest_paths)
    graph = nx.DiGraph()
    for v1 in range(len(adjacency_matrix)):
        for v2 in range(len(adjacency_matrix[v1])):
            weight = adjacency_matrix[v1][v2]
            if weight != 0 and weight != float("inf"):
                graph.add_edge(v1, v2, weight=weight)
    nx.draw(graph, with_labels=True)
    plt.show()