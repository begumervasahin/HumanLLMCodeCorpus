import numpy as np
import math
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
infinity = math.inf
def get_adjacency_matrix():
    num_vertices = int(input("Enter the number of vertices: "))
    print("Enter the values of the adjacency matrix row-wise:")
    adjacency_matrix = np.zeros((num_vertices, num_vertices))
    for i in range(num_vertices):
        adjacency_matrix[i] = list(map(int, input().split()))
    return num_vertices, adjacency_matrix
def floyd_warshall(adjacency_matrix, num_vertices):
    print("\n\n")
    print("Initial Matrix (D[0]):\n", adjacency_matrix)
    print("\n")
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
        print("Matrix after iteration %d (D[%d]):\n" % (k + 1, k + 1), adjacency_matrix)
        print("\n")
num_vertices, adjacency_matrix = get_adjacency_matrix()
floyd_warshall(adjacency_matrix, num_vertices)