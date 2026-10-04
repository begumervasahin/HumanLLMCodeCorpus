import numpy as np
import cupy as cp
a1 = 1e6
def fonk1(b8, b6):
    b1 = cp.ones([b6, b6]) * a1
    b2 = cp.ones([b6, b6])
    for k in range(b6):
        b3 = cp.log(cp.dot(cp.exp(b8[:, k].reshape(b6, 1)), cp.exp(b8[k, :].reshape(1, b6))))
        b4 = cp.sign(b1 - b3)
        b5 = cp.where(b4 > 0)
        b1[b5] = b3[b5]
    return b1
def fonk2(b6 = 4):
    b7 = np.random.binomial(1, 0.5, [b6, b6])
    b7 = np.triu(b7, 1)
    b7 += np.transpose(b7)
    b7 = cp.array(b7)
    b8 = cp.array(np.random.exponential(scale=1, size=(b6, b6)))
    b8 = cp.multiply(b7, b8)
    b8 = cp.array(np.triu(b8.get(), 1))
    b8 += cp.transpose(b8)
    b8 += (cp.ones([b6, b6]) - b7) * a1
    cp.fill_diagonal(b8, 0)
    b8 = cp.array(b8)
    return b8
if b9 = = '__main__':
    b6 = 4
    b8 = fonk2(b6)
    print("Adjacency Matrix:", b8)
    b10 = fonk1(b8, b6)
    print("Distances:", b10)