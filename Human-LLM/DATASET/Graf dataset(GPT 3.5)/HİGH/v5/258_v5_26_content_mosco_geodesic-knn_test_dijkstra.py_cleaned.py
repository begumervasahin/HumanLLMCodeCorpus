import numpy as np
import scipy.sparse.csgraph
from dijkstra import dijkstra
def fonk1(a1):
    b1 = np.random.random((a1, a1))
    b1 += b1.transpose()
    b1[b1 < 1.0] = np.inf
    return scipy.sparse.csr_matrix(b1)
def fonk2():
    a1 = 100
    b1 = fonk1(a1)
    for seed in [0, 1, 2]:
        b2 = dijkstra(b1, seed)
        b3 = scipy.sparse.csgraph.dijkstra(b1, indices=[seed])[0]
        assert all(b2 = = b3)
fonk2()