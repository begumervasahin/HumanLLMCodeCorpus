import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def swpca(dataset, catvar, k=0.05, trset=False):
    N = dataset.shape[0]
    training = False
    if not isinstance(trset, np.ndarray) or trset is False:
        trset = np.ones(N, dtype=bool)
    else:
        training = True
    subjMean = dataset.mean(axis=1)
    X = (dataset.T - subjMean).T
    meanTr = X[trset].mean(axis=0)
    X -= meanTr
    varTr = X[trset].var(axis=0)
    varTr = np.maximum(varTr, 1)
    X /= varTr
    if training:
        XNTEST = X[~trset]
    XNTRAIN = X[trset]
    U, s, Wt = svd(XNTRAIN, full_matrices=False)
    W = Wt.T
    ind = np.argsort(s)[::-1]
    U, s, W = U[:, ind], s[ind], W[:, ind]
    STr = XNTRAIN.dot(W)
    if training:
        STe = XNTEST.dot(W)
    labs = np.unique(catvar)
    F, p_val = f_oneway(STr[catvar[trset] == labs[0]], STr[catvar[trset] == labs[1]])
    weights = 1 - np.exp(-p_val / k)
    A = np.linalg.pinv(W)
    weightMat = np.diag(weights)
    if training:
        XTRhat = STr.dot(weightMat).dot(A)
        XTEhat = STe.dot(weightMat).dot(A)
        Xhat = np.zeros((N, XTRhat.shape[1]))
        Xhat[trset] = XTRhat
        Xhat[~trset] = XTEhat
    else:
        Xhat = STr.dot(weightMat).dot(A)
    Xhat = Xhat * varTr + meanTr
    Xhat = (Xhat.T + subjMean).T
    return Xhat, weights, A