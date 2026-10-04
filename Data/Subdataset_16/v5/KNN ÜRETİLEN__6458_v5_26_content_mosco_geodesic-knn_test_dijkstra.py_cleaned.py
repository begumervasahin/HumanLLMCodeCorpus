import numpy as np
import scipy.sparse as sparse
import scipy.sparse.csgraph as csgraph
import dijkstra
def fonk1(size, b1 = 1.0):
    b2 = np.random.random((size, size))
    b2 = (b2 + b2.T) / 2
    b2[b2 < b1] = np.inf
    return sparse.csr_matrix(b2)
def fonk2(b3 = 100, seeds=[0, 1, 2]):
    b2 = fonk1(b3)
    for seed in seeds:
        b4 = dijkstra.dijkstra(b2, seed)
        b5 = csgraph.dijkstra(b2, indices=seed)[0]
        assert np.allclose(b4, b5), f"Mismatch found for seed {seed}"
        print(f"Test passed for seed {seed}")
if b6 = = "__main__":
    fonk2()