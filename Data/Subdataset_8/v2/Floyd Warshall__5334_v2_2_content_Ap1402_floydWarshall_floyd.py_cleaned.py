from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def floyd_warshall(graph):
    matrix_floyd = deepcopy(graph)
    num_vertices = len(graph)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                aux = matrix_floyd[i][k] + matrix_floyd[k][j]
                if matrix_floyd[i][j] > aux:
                    matrix_floyd[i][j] = aux
    return matrix_floyd
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, ",", end=" ")
        print("")
def get_adjacency_matrix():
    INF = 99999
    print("Create Adjacency Matrix")
    num_vertices = int(input("Number of vertices: "))
    adjacency_matrix = []
    for v1 in range(num_vertices):
        adjacency_matrix.append([])
        for v2 in range(num_vertices):
            if v1 == v2:
                adjacency_matrix[v1].append(0)
            else:
                print("Distance from vertex", v1 + 1, "to", v2 + 1, ": ", end="")
                aux = input()
                if aux == '':
                    distance = INF
                else:
                    distance = int(aux)
                adjacency_matrix[v1].append(distance)
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