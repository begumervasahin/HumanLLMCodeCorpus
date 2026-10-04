import numpy as np
import cupy as cp
a1 = 1e6
def fonk1(b6, b5):
    b1 = cp.ones([b5, b5]) * a1
    for k in range(b5):
        b2 = cp.log(cp.dot(cp.exp(b6[:, k].reshape(b5, 1)),
                           cp.exp(b6[k, :].reshape(1, b5))))
        b3 = cp.sign(b1 - b2)
        b4 = cp.where(b3 > 0)
        b1[b4] = b2[b4]
    return b1
def fonk2(b5 = 4):
    b6 = np.random.binomial(1, 0.5, [b5, b5])
    b6 = np.triu(b6, 1)
    b6 += b6.T
    b6 = cp.array(b6)
    b7 = cp.array(np.random.exponential(scale=1, size=(b5, b5)))
    b7 = cp.multiply(b6, b7)
    b7 = cp.array(np.triu(b7.get(), 1))
    b7 += b7.T
    b7 += (cp.ones([b5, b5]) - b6) * a1
    cp.fill_diagonal(b7, 0)
    return b7
def fonk3():
    b5 = 4
    b6 = fonk2(b5)
    print("Adjacency Matrix:\n", b6)
    b8 = fonk1(b6, b5)
    print("Shortest Path Distances:\n", b8)
if b9 = = '__main__':
    fonk3()