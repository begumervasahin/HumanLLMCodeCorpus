import numpy as np
import math
np.set_printoptions(precision=2, suppress=True)
INFINITY = math.inf
def get_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the values of the adjacency matrix row-wise:")
    graph = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        for j in range(num_vertices):
            graph[i][j] = int(input(f"Edge from vertex {i} to vertex {j}: "))
    return num_vertices, graph
def floyd_warshall(graph, num_vertices):
    print("\nInitial Distance Matrix (D[0]):\n", graph, "\n")
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print(f"Distance Matrix after considering vertex {k} (D[{k+1}]):\n", graph, "\n")
def main():
    num_vertices, graph = get_graph()
    floyd_warshall(graph, num_vertices)
if __name__ == '__main__':
    main()