import numpy as np
import cupy as cp
a1 = 1e6
def fonk1(b6, b3):
    b1 = cp.ones([b3, b3]) * a1
    for k in range(b3):
        b2 = cp.log(cp.dot(cp.exp(b6[:, k].reshape(b3, 1)),
                                                cp.exp(b6[k, :].reshape(1, b3))))
        b1 = cp.minimum(b1, b2)
    return b1
def fonk2(b3 = 4):
    b4 = cp.array(np.random.binomial(1, 0.5, [b3, b3]))
    b4 = cp.triu(b4, 1)
    b4 += cp.transpose(b4)
    b5 = cp.array(np.random.exponential(scale=1, size=(b3, b3)))
    b6 = cp.multiply(b4, b5)
    b6 = cp.array(cp.triu(b6.get(), 1))
    b6 += cp.transpose(b6)
    b6 += (cp.ones([b3, b3]) - b4) * a1
    cp.fill_diagonal(b6, 0)
    return b6
if b7 = = "__main__":
    b3 = 4
    b6 = fonk2(b3)
    print("Adjacency Matrix:")
    print(b6)
    b1 = fonk1(b6, b3)
    print("Distances:")
    print(b1)