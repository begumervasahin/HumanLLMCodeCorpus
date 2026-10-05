import numpy as np
import scipy.sparse.csgraph
def fonk1(b2):
    b1 = np.random.random((b2, b2))
    b1 += b1.transpose()
    b1[b1 < 1.0] = np.inf
    return scipy.sparse.csr_matrix(b1)
def fonk2(b2 = 100, seeds=[0, 1, 2]):
    b1 = fonk1(b2)
    for seed in seeds:
        b3 = dijkstra.dijkstra(b1, seed)
        b4 = scipy.sparse.csgraph.dijkstra(b1, indices=[seed])[0]
        assert all(b3 = = b4)
fonk2()