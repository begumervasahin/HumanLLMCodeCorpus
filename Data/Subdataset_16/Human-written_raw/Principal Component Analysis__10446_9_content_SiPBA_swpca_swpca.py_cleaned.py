import numpy as np
from scipy.linalg import svd
from scipy.stats import f_oneway
def fonk1(dataset, catvar, b1 = 0.05, b3=False):
    b2 = dataset.shape[0]
    if not b3:
        b3 = np.ones(b2)
        b4 = False
    else:
        b4 = True
    b5 = dataset.mean(axis=1)
    b6 = (dataset.transpose()-b5).transpose()
    del dataset
    b7 = b6[b3==1,:].mean(axis=0)
    b6 = b6 - b7
    b8 = b6[b3==1,:].var(axis=0)
    b8 = np.maximum(b8,1)
    b6 = b6/b8
    if b4:
        b9 = b6[b3!=1,:]
    b10 = b6[b3==1,:]
    del b6
    b14, b15, b11 = svd(b10, full_matrices=False)
    b12 = b11.T
    b13 = np.argsort(b15)[::-1]
    b14 = b14[:, b13]
    b15 = b15[b13]
    b12 = b12[:, b13]
    b16 = b10.dot(b12)
    if b4:
        b17 = b9.dot(b12)
    b18 = np.unique(catvar)
    F,b19 = f_oneway(b16[catvar[b3==1]==b18[0],:], b16[catvar[b3==1]==b18[1],:])
    b20 = 1-np.exp(-b19/b1)
    b21 = np.linalg.pinv(b12)
    b22 = np.diag(b20)
    if b4:
        b23 = b16.dot(b22).dot(b21)
        b24 = b17.dot(b22).dot(b21)
        b25 = np.zeros([b2,b23.shape[1]])
        b25[b3 = =1,:] = b23
        b25[b3!=1,:] = b24
        del b23,b24
    else:
        b25 = b16.dot(b22).dot(b21)
    b25 = b25*b8
    b25 = b25+b7
    b25 = (b25.T+b5).T
    return b25, b20, b21