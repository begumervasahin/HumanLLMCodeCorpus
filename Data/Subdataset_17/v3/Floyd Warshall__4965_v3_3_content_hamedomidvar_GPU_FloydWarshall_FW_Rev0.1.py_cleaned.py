import numpy as np
import cupy as cp
INFINITY = 1e6
def floyd_warshall(adjacency_matrix, num_vertices):
    distance_matrix = cp.ones([num_vertices, num_vertices]) * INFINITY
    for k in range(num_vertices):
        dk = cp.log(cp.dot(cp.exp(adjacency_matrix[:, k].reshape(num_vertices, 1)),
                           cp.exp(adjacency_matrix[k, :].reshape(1, num_vertices))))
        update_mask = cp.sign(distance_matrix - dk)
        update_indices = cp.where(update_mask > 0)
        distance_matrix[update_indices] = dk[update_indices]
    return distance_matrix
def create_adjacency_matrix(num_vertices=4):
    adjacency_matrix = np.random.binomial(1, 0.5, [num_vertices, num_vertices])
    adjacency_matrix = np.triu(adjacency_matrix, 1)
    adjacency_matrix += adjacency_matrix.T
    adjacency_matrix = cp.array(adjacency_matrix)
    weight_matrix = cp.array(np.random.exponential(scale=1, size=(num_vertices, num_vertices)))
    weight_matrix = cp.multiply(adjacency_matrix, weight_matrix)
    weight_matrix = cp.array(np.triu(weight_matrix.get(), 1))
    weight_matrix += weight_matrix.T
    weight_matrix += (cp.ones([num_vertices, num_vertices]) - adjacency_matrix) * INFINITY
    cp.fill_diagonal(weight_matrix, 0)
    return weight_matrix
def main():
    num_vertices = 4
    adjacency_matrix = create_adjacency_matrix(num_vertices)
    print("Adjacency Matrix:\n", adjacency_matrix)
    shortest_paths_matrix = floyd_warshall(adjacency_matrix, num_vertices)
    print("Shortest Path Distances:\n", shortest_paths_matrix)
if __name__ == '__main__':
    main()