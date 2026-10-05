import numpy as np
import cupy as cp
INF = 1e6
def floyd_warshall(W, n):
    d = cp.ones([n, n]) * INF
    for k in range(n):
        dk = cp.log(cp.dot(cp.exp(W[:, k].reshape(n, 1)), cp.exp(W[k, :].reshape(1, n))))
        a = cp.sign(d - dk)
        where_to = cp.where(a > 0)
        d[where_to] = dk[where_to]
    return d
def generate_adjacency_matrix(n=4):
    connectivity = np.random.binomial(1, 0.5, [n, n])
    connectivity = np.triu(connectivity, 1)
    connectivity += np.transpose(connectivity)
    connectivity = cp.array(connectivity)
    weights = cp.array(np.random.exponential(scale=1, size=(n, n)))
    W = cp.multiply(connectivity, weights)
    W = cp.array(np.triu(W.get(), 1))
    W += cp.transpose(W)
    W += (cp.ones([n, n]) - connectivity) * INF
    cp.fill_diagonal(W, 0)
    return W
if __name__ == "__main__":
    num_vertices = 4
    adjacency_matrix = generate_adjacency_matrix(num_vertices)
    print("Adjacency Matrix:")
    print(adjacency_matrix)
    distances = floyd_warshall(adjacency_matrix, num_vertices)
    print("Distances:")
    print(distances)