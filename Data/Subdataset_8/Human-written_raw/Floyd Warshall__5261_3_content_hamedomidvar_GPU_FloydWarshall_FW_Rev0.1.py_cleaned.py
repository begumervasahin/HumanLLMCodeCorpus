import numpy as np
import cupy as cp
myInf = 1e6
def FW(W,n):
    d = cp.ones([n,n])*myInf
    all_ones = cp.ones([n,n])
    for k in range(n):
        dk = cp.log(cp.dot(cp.exp(W[:,k].reshape(n,1)),cp.exp(W[k,:].reshape(1,n))))
        a = cp.sign(d-dk)
        where_to = cp.where(a>0)
        d[where_to] = dk[where_to]
    return d
n = 4
def make_W(n = 4):
    A = np.random.binomial(1,0.5,[n,n])
    A = np.triu(A,1)
    A +=  np.transpose(A)
    A = cp.array(A)
    W = cp.array(np.random.exponential(scale=1,size=(n,n)))
    W = cp.multiply(A,W)
    W = cp.array(np.triu(W.get(),1))
    W +=  cp.transpose(W)
    W += (cp.ones([n,n])-A)*myInf
    cp.fill_diagonal(W,0)
    W = cp.array(W)
    return W
W = make_W()
print("Adjacency Matrix:", W)
print("Distances:", FW(W,n))