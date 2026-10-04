import numpy as np
import scipy.sparse
import scipy.sparse.csgraph
import dijkstra
def fonk1():
    b1 = np.random.random((100, 100))
    b1 += b1.transpose()
    b1[b1 < 1.0] = np.inf
    b1 = scipy.sparse.csr_matrix(b1)
    for seed in [0, 1, 2]:
        b2 = dijkstra.dijkstra(b1, seed)
        b3 = scipy.sparse.csgraph.dijkstra(b1, indices=[seed])[0]
        assert all(b2 = = b3), f"Discrepancy found for seed {seed}"
fonk1()