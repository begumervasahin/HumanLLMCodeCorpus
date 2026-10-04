import numpy as np
import scipy as sp
import sys
def fonk1(a1,b7,b9):
    b1 = b9.shape[1]
    b2 = sys.maxint
    b3 = np.ones((b1),float)*np.inf
    b4 = np.zeros((b1),int)*b2
    b3[a1] = 0
    for i in range(0,b1-1):
        for u in range(0,b1):
            for v in range(0,b1):
                b5 = b9[u,v]
                if (b5 != 0):
                    if (b3[u]+b5 < b3[v]):
                        b3[v] = b3[u] + b5
                        b4[v] = u
    for u in range(0,b1):
        for v in range(0,b1):
            b5 = b9[u,v]
            if (b5 != 0):
                if (b3[u]+b5 < b3[v]):
                    print('graph contains a negative-weight cycle')
    b6 = [b7]
    while b4[b7] != a1:
        b6.append(b4[b7])
        b7 = b4[b7]
    b6.append(a1)
    return b6[::-1]
if b8 = = '__main__':
    a1 = 4
    b7 = 3
    b9 = np.array([[ 0, 20,  0, 80, 0,  0, 90,  0],
                    [ 0,  0,  0,  0, 0, 10,  0,  0],
                    [ 0,  0,  0, 10, 0, 50,  0, 20],
                    [ 0,  0, 10,  0, 0,  0, 20,  0],
                    [ 0, 50,  0,  0, 0,  0, 30,  0],
                    [ 0,  0, 10, 40, 0,  0,  0,  0],
                    [20,  0,  0,  0, 0,  0,  0,  0],
                    [ 0,  0,  0,  0, 0,  0,  0,  0]])
    b6 = fonk1(a1,b7,b9)
    print a1,' -> ',b7,' is ',b6