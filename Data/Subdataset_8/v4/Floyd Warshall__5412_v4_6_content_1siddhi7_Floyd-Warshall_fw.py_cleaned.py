import numpy as np
import math
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
infinity = math.inf
def get_adjacency_matrix():
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the values of the adjacency matrix row-wise:")
    graph = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        for j in range(num_vertices):
            graph[i][j] = int(input())
    return num_vertices, graph
def floyd_warshall(graph, num_vertices):
    print("\n\n")
    print("Initial Matrix (D[0]):\n ", graph)
    print("\n")
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print("Matrix after iteration %d (D[%d]):\n " % (k + 1, k + 1), graph)
        print("\n")
num_vertices, graph = get_adjacency_matrix()
floyd_warshall(graph, num_vertices)