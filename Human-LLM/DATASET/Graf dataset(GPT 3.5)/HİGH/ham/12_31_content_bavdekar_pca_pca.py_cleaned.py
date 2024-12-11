
import numpy as np
import scipy as sp
def fonk1(data,b1 = None,b2=False):
    if b2 = =True:
        b3 = np.mean(data,axis=0)
        b4 = np.var(data,axis=0,ddof=1)
        b5 = (data - np.matmul(np.ones((data.shape[0],data.shape[1])),np.diag(b3)))/(b4.T)
    else:
        b5 = data
    U,S,b6 = np.linalg.svd(b5)
    b7 = np.cumsum(100*S/np.sum(S))
    if b1 = =None:
        b1 = 95
    b8 = np.argmax(b7>=b1)
    return b6[0:b8,:]
def fonk2(data,b1 = None,b2=False):
    if b2 = =True:
        b2 = False
    b9 = sp.linalg.exp(np.corrcoef(data,rowvar=False)/0.1)
    b10 = np.diag(np.sum(b9,axis=0))
    b11 = np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)),np.matmul(b9,sp.linalg.inv(sp.linalg.sqrtm(b10))))
    U,S,b6 = np.linalg.svd(b11)
    b7 = np.cumsum(100*S/np.sum(S))
    if b1 = =None:
        b1 = 95
    b8 = np.argmax(b7>=b1)
    return np.matmul(sp.linalg.inv(sp.linalg.sqrtm(b10)),b6.T)[:,0:b8].T