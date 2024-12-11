import numpy as np
import sklearn.neighbors
import scipy.sparse
import warnings
import matplotlib.pyplot as plt
import scipy.misc
def fonk1(b22, b2, b1 = 100):
    [m, n, b18] = b22.shape
    b22, b2 = b22/255.0, b2/255.0
    b3 = (b2 > 0.99).astype(int)
    b4 = (b2 < 0.01).astype(int)
    b5 = b3 + b4
    print('Finding nearest neighbors')
    a, b6 = np.unravel_index(np.arange(m*n), (m, n))
    b7 = np.append(np.transpose(b22.reshape(m*n,b18)), [ a, b6]/np.sqrt(m*m + n*n), axis=0).T
    b8 = sklearn.neighbors.NearestNeighbors(n_neighbors=10, n_jobs=4).fit(b7)
    b9 = b8.kneighbors(b7)[1]
    print('Computing sparse b13')
    b10 = np.repeat(np.arange(m*n), 10)
    b11 = b9.reshape(m*n*10)
    b12 = 1 - np.linalg.norm(b7[b10] - b7[b11], axis=1)/(b18+2)
    b13 = scipy.sparse.coo_matrix((b12, (b10, b11)),shape=(m*n, m*n))
    b14 = scipy.sparse.diags(np.ravel(b13.sum(axis=1)))
    b15 = b14-b13
    b16 = scipy.sparse.diags(np.ravel(b5[:,:, 0]))
    b17 = np.ravel(b3[:,:,0])
    b18 = 2*b1*np.transpose(b17)
    b19 = 2*(b15 + b1*b16)
    print('Solving linear system for b20')
    warnings.filterwarnings('error')
    b20 = []
    try:
        b20 = np.minimum(np.maximum(scipy.sparse.linalg.spsolve(b19, b18), 0), 1).reshape(m, n)
    except Warning:
        b21 = scipy.sparse.linalg.lsqr(b19, b18)
        b20 = np.minimum(np.maximum(b21[0], 0), 1).reshape(m, n)
    return b20
def fonk2():
    b22 = scipy.misc.imread('donkey.png')[:,:,:3]
    b2 = scipy.misc.imread('donkeyTrimap.png')[:,:,:3]
    b20 = fonk1(b22, b2)
    scipy.misc.imsave('donkeyAlpha.png', b20)
    plt.title('Alpha Matte')
    plt.imshow(b20, b23 = 'gray')
    plt.show()
if b24 = = '__main__':
    fonk2()