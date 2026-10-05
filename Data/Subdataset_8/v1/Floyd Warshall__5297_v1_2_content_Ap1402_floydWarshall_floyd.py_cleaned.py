from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
def FloydWarshall(graph):
    matrix_floyd = deepcopy(graph)
    V = len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                aux = matrix_floyd[i][k] + matrix_floyd[k][j]
                if matrix_floyd[i][j] > aux:
                    matrix_floyd[i][j] = aux
    return matrix_floyd
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, ",", end=" ")
        print("")
def get_input():
    INF = 99999
    print("Create Adjacency Matrix")
    V = int(input("Number of vertices: "))
    graph = []
    for v1 in range(V):
        graph.append([])
        for v2 in range(V):
            if v1 == v2:
                graph[v1].append(0)
            else:
                print("Distance from vertex", v1 + 1, "to", v2 + 1, ": ", end="")
                aux = input()
                if aux == '':
                    distance = INF
                else:
                    distance = int(aux)
                graph[v1].append(distance)
    return graph
if __name__ == "__main__":
    adjacency_matrix = get_input()
    shortest_paths = FloydWarshall(adjacency_matrix)
    print("Shortest path distances:")
    print_matrix(shortest_paths)
    g = nx.DiGraph()
    for v1 in range(len(adjacency_matrix)):
        for v2 in range(len(adjacency_matrix[v1])):
            weight = adjacency_matrix[v1][v2]
            if weight != 0 and weight != float("inf"):
                g.add_edge(v1, v2, weight=weight)
    nx.draw(g, with_labels=True)
    plt.show()