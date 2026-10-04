import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def swpca(dataset, catvar, k=0.05, trset=False):
    N = dataset.shape[0]
    if not trset:
        trset=np.ones(N)
        training = False
    else:
        training = True
    subjMean = dataset.mean(axis=1)
    X = (dataset.transpose()-subjMean).transpose()
    del dataset
    meanTr = X[trset==1,:].mean(axis=0)
    X = X - meanTr
    varTr = X[trset==1,:].var(axis=0)
    varTr = np.maximum(varTr,1)
    X = X/varTr
    if training:
        XNTEST = X[trset!=1,:]
    XNTRAIN = X[trset==1,:]
    del X
    U, s, Wt = svd(XNTRAIN, full_matrices=False)
    W = Wt.T
    ind = np.argsort(s)[::-1]
    U = U[:, ind]
    s = s[ind]
    W = W[:, ind]
    STr = XNTRAIN.dot(W)
    if training:
        STe = XNTEST.dot(W)
    labs = np.unique(catvar)
    F,p_val = f_oneway(STr[catvar[trset==1]==labs[0],:], STr[catvar[trset==1]==labs[1],:])
    weights = 1-np.exp(-p_val/k)
    A = np.linalg.pinv(W)
    weightMat = np.diag(weights)
    if training:
        XTRhat = STr.dot(weightMat).dot(A)
        XTEhat = STe.dot(weightMat).dot(A)
        Xhat = np.zeros([N,XTRhat.shape[1]])
        Xhat[trset==1,:] = XTRhat
        Xhat[trset!=1,:] = XTEhat
        del XTRhat,XTEhat
    else:
        Xhat = STr.dot(weightMat).dot(A)
    Xhat = Xhat*varTr
    Xhat = Xhat+meanTr
    Xhat = (Xhat.T+subjMean).T
    return Xhat, weights, A