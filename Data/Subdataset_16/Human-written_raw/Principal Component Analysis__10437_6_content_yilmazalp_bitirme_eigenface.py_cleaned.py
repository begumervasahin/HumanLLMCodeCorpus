import numpy as np
def asRowMatrix (X):
    if len (X) == 0:
        return np. array ([])
    b1 = np. empty ((0 , X [0]. size ), dtype =X [0]. dtype )
    for row in X:
        b1 = np. vstack (( b1 , np. asarray ( row ). reshape (1 , -1)))
    return b1
def asColumnMatrix (X):
    if len (X) == 0:
        return np. array ([])
    b1 = np. empty ((X [0]. size , 0) , dtype =X [0]. dtype )
    for col in X:
        b1 = np. hstack (( b1 , np. asarray ( col ). reshape ( -1 ,1)))
    return b1
def pca (b4, y, b2 = 0):
    [n,d] = b4.shape
    if (b2 <= 0) or (b2 >n):
        b2 = n
    b3 = b4.mean( axis =0)
    b4 = b4 - b3
    if n>d:
        b5 = np.dot(b4.T,b4)
        [b8,b6] = np.linalg.eigh(b5)
    else :
        b5 = np.dot(b4,b4.T)
        [b8 , b6] = np.linalg.eigh(b5)
        b6 = np.dot(b4.T, b6)
    for i in range(n):
        b6[:,i] = b6[:,i]/ np.linalg.norm(b6[:,i])
    b7 = np. argsort(-b8)
    b8 = b8[b7]
    b6 = b6[:,b7]
    b8 = b8[0: b2].copy()
    b6 = b6 [: ,0: b2 ].copy()
    return [b8, b6, b3]
def project (b4, X, b3 = None):
    if b3 is None:
        return np.dot(X,b4)
    return np.dot(X - b3, b4)
def reconstruct (b4, Y, b3 = None):
    if b3 is None :
        return np.dot(Y, b4.T)
    return np.dot(Y, b4.T) + b3