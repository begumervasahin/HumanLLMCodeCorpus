import numpy as np
import scipy.sparse as sparse
import scipy.sparse.csgraph as csgraph
import dijkstra
def generate_random_weighted_graph(size, threshold=1.0):
    W = np.random.random((size, size))
    W = (W + W.T) / 2
    W[W < threshold] = np.inf
    return sparse.csr_matrix(W)
def test_dijkstra_against_scipy(graph_size=100, seeds=[0, 1, 2]):
    W = generate_random_weighted_graph(graph_size)
    for seed in seeds:
        result_custom = dijkstra.dijkstra(W, seed)
        result_scipy = csgraph.dijkstra(W, indices=seed)[0]
        assert np.allclose(result_custom, result_scipy), f"Mismatch found for seed {seed}"
        print(f"Test passed for seed {seed}")
if __name__ == "__main__":
    test_dijkstra_against_scipy()