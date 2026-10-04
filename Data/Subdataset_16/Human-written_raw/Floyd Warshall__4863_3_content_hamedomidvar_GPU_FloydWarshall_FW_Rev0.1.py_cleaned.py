import numpy as np
import cupy as cp
a1 = 1e6
def fonk1(b7,a2):
    b1 = cp.ones([a2,a2])*a1
    b2 = cp.ones([a2,a2])
    for k in range(a2):
        b3 = cp.log(cp.dot(cp.exp(b7[:,k].reshape(a2,1)),cp.exp(b7[k,:].reshape(1,a2))))
        b4 = cp.sign(b1-b3)
        b5 = cp.where(b4>0)
        b1[b5] = b3[b5]
    return b1
a2 = 4
def fonk2(a2 = 4):
    b6 = np.random.binomial(1,0.5,[a2,a2])
    b6 = np.triu(b6,1)
    b6 +=  np.transpose(b6)
    b6 = cp.array(b6)
    b7 = cp.array(np.random.exponential(scale=1,size=(a2,a2)))
    b7 = cp.multiply(b6,b7)
    b7 = cp.array(np.triu(b7.get(),1))
    b7 +=  cp.transpose(b7)
    b7 += (cp.ones([a2,a2])-b6)*a1
    cp.fill_diagonal(b7,0)
    b7 = cp.array(b7)
    return b7
b7 = fonk2()
print("Adjacency Matrix:", b7)
print("Distances:", fonk1(b7,a2))