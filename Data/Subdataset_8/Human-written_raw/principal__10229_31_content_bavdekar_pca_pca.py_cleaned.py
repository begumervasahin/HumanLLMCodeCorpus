
import numpy as np
import scipy as sp
def lpca(data,cv=None,normalize=False):
    if normalize==True:
        m = np.mean(data,axis=0)
        v = np.var(data,axis=0,ddof=1)
        data_zm_uv = (data - np.matmul(np.ones((data.shape[0],data.shape[1])),np.diag(m)))/(v.T)
    else:
        data_zm_uv = data
    U,S,Vt = np.linalg.svd(data_zm_uv)
    cve = np.cumsum(100*S/np.sum(S))
    if cv==None:
        cv = 95
    nx = np.argmax(cve>=cv)
    return Vt[0:nx,:]
def scpa(data,cv=None,normalize=False):
    if normalize==True:
        normalize=False
    W = sp.linalg.exp(np.corrcoef(data,rowvar=False)/0.1)
    D = np.diag(np.sum(W,axis=0))
    scaled_data = np.matmul(sp.linalg.inv(sp.linalg.sqrtm(D)),np.matmul(W,sp.linalg.inv(sp.linalg.sqrtm(D))))
    U,S,Vt = np.linalg.svd(scaled_data)
    cve = np.cumsum(100*S/np.sum(S))
    if cv==None:
        cv = 95
    nx = np.argmax(cve>=cv)
    return np.matmul(sp.linalg.inv(sp.linalg.sqrtm(D)),Vt.T)[:,0:nx].T