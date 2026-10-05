import numpy as np
import cupy as cp
INFINITY = 1e6
def floyd_warshall(adjacency_matrix, num_vertices):
    shortest_paths = cp.ones([num_vertices, num_vertices]) * INFINITY
    for k in range(num_vertices):
        intermediate_distances = cp.log(cp.dot(cp.exp(adjacency_matrix[:, k].reshape(num_vertices, 1)),
                                                cp.exp(adjacency_matrix[k, :].reshape(1, num_vertices))))
        shortest_paths = cp.minimum(shortest_paths, intermediate_distances)
    return shortest_paths
def generate_adjacency_matrix(num_vertices=4):
    connectivity_matrix = cp.array(np.random.binomial(1, 0.5, [num_vertices, num_vertices]))
    connectivity_matrix = cp.triu(connectivity_matrix, 1)
    connectivity_matrix += cp.transpose(connectivity_matrix)
    weights = cp.array(np.random.exponential(scale=1, size=(num_vertices, num_vertices)))
    adjacency_matrix = cp.multiply(connectivity_matrix, weights)
    adjacency_matrix = cp.array(cp.triu(adjacency_matrix.get(), 1))
    adjacency_matrix += cp.transpose(adjacency_matrix)
    adjacency_matrix += (cp.ones([num_vertices, num_vertices]) - connectivity_matrix) * INFINITY
    cp.fill_diagonal(adjacency_matrix, 0)
    return adjacency_matrix
if __name__ == "__main__":
    num_vertices = 4
    adjacency_matrix = generate_adjacency_matrix(num_vertices)
    print("Adjacency Matrix:")
    print(adjacency_matrix)
    shortest_paths = floyd_warshall(adjacency_matrix, num_vertices)
    print("Distances:")
    print(shortest_paths)