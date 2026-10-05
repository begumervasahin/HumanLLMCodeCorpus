from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def floyd_warshall(graph):
    num_vertices = len(graph)
    shortest_paths = deepcopy(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                intermediate_distance = shortest_paths[i][k] + shortest_paths[k][j]
                if shortest_paths[i][j] > intermediate_distance:
                    shortest_paths[i][j] = intermediate_distance
    return shortest_paths
def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(item) for item in row))
def get_adjacency_matrix():
    INF = 99999
    print("Create Adjacency Matrix")
    num_vertices = int(input("Number of vertices: "))
    adjacency_matrix = []
    for v1 in range(num_vertices):
        row = []
        for v2 in range(num_vertices):
            if v1 == v2:
                row.append(0)
            else:
                prompt = "Distance from vertex {} to {}: ".format(v1 + 1, v2 + 1)
                user_input = input(prompt).strip()
                distance = int(user_input) if user_input else INF
                row.append(distance)
        adjacency_matrix.append(row)
    return adjacency_matrix
if __name__ == "__main__":
    adjacency_matrix = get_adjacency_matrix()
    shortest_paths = floyd_warshall(adjacency_matrix)
    print("Shortest path distances:")
    print_matrix(shortest_paths)
    graph = nx.DiGraph()
    for v1 in range(len(adjacency_matrix)):
        for v2 in range(len(adjacency_matrix[v1])):
            weight = adjacency_matrix[v1][v2]
            if weight != 0 and weight != float("inf"):
                graph.add_edge(v1, v2, weight=weight)
    nx.draw(graph, with_labels=True)
    plt.show()