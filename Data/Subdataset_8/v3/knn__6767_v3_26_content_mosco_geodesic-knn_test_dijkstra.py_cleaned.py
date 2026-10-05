import numpy as np
import scipy.sparse.csgraph
def generate_random_weighted_graph(size):
    W = np.random.random((size, size))
    W += W.transpose()
    W[W < 1.0] = np.inf
    return scipy.sparse.csr_matrix(W)
def test_dijkstra_against_scipy(size=100, seeds=[0, 1, 2]):
    W = generate_random_weighted_graph(size)
    for seed in seeds:
        result0 = dijkstra.dijkstra(W, seed)
        result1 = scipy.sparse.csgraph.dijkstra(W, indices=[seed])[0]
        assert all(result0 == result1)
test_dijkstra_against_scipy()