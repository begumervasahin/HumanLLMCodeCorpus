import numpy as np
import scipy.sparse
import scipy.sparse.csgraph
import dijkstra
def test_dijkstra_against_scipy():
    W = np.random.random((100, 100))
    W += W.T
    W[W < 1.0] = np.inf
    W = scipy.sparse.csr_matrix(W)
    for seed in [0, 1, 2]:
        result_custom = dijkstra.dijkstra(W, seed)
        result_scipy = scipy.sparse.csgraph.dijkstra(W, indices=seed)[0]
        assert np.array_equal(result_custom, result_scipy), f"Discrepancy found for seed {seed}"
if __name__ == "__main__":
    test_dijkstra_against_scipy()