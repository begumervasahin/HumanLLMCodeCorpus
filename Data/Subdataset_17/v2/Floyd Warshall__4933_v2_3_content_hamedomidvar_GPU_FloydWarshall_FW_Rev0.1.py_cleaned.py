import numpy as np
import cupy as cp
INFINITY = 1e6
def floyd_warshall(W, n):
    distance_matrix = cp.ones([n, n]) * INFINITY
    for k in range(n):
        dk = cp.log(cp.dot(cp.exp(W[:, k].reshape(n, 1)), cp.exp(W[k, :].reshape(1, n))))
        update_mask = cp.sign(distance_matrix - dk)
        update_indices = cp.where(update_mask > 0)
        distance_matrix[update_indices] = dk[update_indices]
    return distance_matrix
def create_adjacency_matrix(n=4):
    adjacency_matrix = np.random.binomial(1, 0.5, [n, n])
    adjacency_matrix = np.triu(adjacency_matrix, 1)
    adjacency_matrix += adjacency_matrix.T
    adjacency_matrix = cp.array(adjacency_matrix)
    weight_matrix = cp.array(np.random.exponential(scale=1, size=(n, n)))
    weight_matrix = cp.multiply(adjacency_matrix, weight_matrix)
    weight_matrix = cp.array(np.triu(weight_matrix.get(), 1))
    weight_matrix += weight_matrix.T
    weight_matrix += (cp.ones([n, n]) - adjacency_matrix) * INFINITY
    cp.fill_diagonal(weight_matrix, 0)
    return weight_matrix
def main():
    n = 4
    adjacency_matrix = create_adjacency_matrix(n)
    print("Adjacency Matrix:\n", adjacency_matrix)
    distances = floyd_warshall(adjacency_matrix, n)
    print("Distances:\n", distances)
if __name__ == '__main__':
    main()