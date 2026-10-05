import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
import math
infinity = math.inf
def get_graph():
    V = int(input("Enter number of vertices: "))
    print("Enter the values of the adjacency matrix row-wise:")
    graph = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            graph[i][j] = int(input())
    return V, graph
def floydWarshall(graph, n):
    print("\n\n")
    print("D[0] :\n ", graph)
    print("\n")
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print("D[%d] :\n " % (k + 1), graph)
        print("\n")
num_vertices, adjacency_matrix = get_graph()
floydWarshall(adjacency_matrix, num_vertices)