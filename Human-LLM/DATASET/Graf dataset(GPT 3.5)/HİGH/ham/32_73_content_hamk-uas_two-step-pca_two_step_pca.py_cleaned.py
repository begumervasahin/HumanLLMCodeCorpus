import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def fonk1(b20, lag):
    b1 = b20[lag:]
    for l in range(1, lag + 1):
        b1 = np.hstack((b1, b20[lag - l: -l]))
    return b1
def fonk2(b20, b26):
    n_samples, b2 = b20.shape
    b3 = np.zeros((n_samples - b26, b2))
    b4 = b20[b26:]
    b3 = b4 - b20[:-b26]
    return b3
def fonk3(b20, lag, b26):
    b5 = b20
    b1 = fonk1(b5, lag)
    b3 = fonk2(b5, b26)
    b6 = fonk2(b1, b26)
    b7 = b3.shape[0] - b6.shape[0]
    b3 = b3[b7:]
    b8 = np.linalg.inv(np.dot(b6.b16, b6))
    b9 = np.dot(b6.b16, b3)
    b10 = np.dot(b8,b9)
    return b10
def fonk4(b16, b17):
    """
    Computes b29 metric
    Arguments:
        b16 - numpy array, score matrix (or principal components, it is the same), usually you pick first "l" PCs,
            which explain most variance
        b17 - eigenvalues which correspond to b16
    Returns:
        b29 - Hotelling's b29 metric
    Computes b30 metric
    Arguments:
        b16 - numpy array, score matrix, unlike in Hotelling's b29 you use "m-l" PCs here,
            so b16 here is all principal components you didnt use in b29 calculations.
    Returns:
        b30 - numpy array, Squared Prediction Error
    Usual PCA decomposition which returns all intermediate parameters
    Arguments:
        b20 - numpy array with input b20 (should be already with zero mean and unit variance)
                most probably you want to pass b23(innovation part) here
    Returns:
        b16 - score matrix (Principal components)
        b15 - loading matrix (eigenvectors)
        b17 - eigenvalues
        b14 - variance explained for each principal component
    """
    b11 = np.cov(b20.b16)
    eig_vals, b12 = np.linalg.eig(b11)
    b13 = [[np.abs(eig_vals[i]), b12[:, i]] for i in range(len(eig_vals))]
    print("Eigen_values shape: {}".format(len(b13)))
    b13.sort()
    b13.reverse()
    b14 = [(i/sum(eig_vals)) for i in sorted(eig_vals, reverse=True)]
    b15 = np.array([i[1] for i in b13])
    b16 = np.dot(b20, b15.b16)
    b17 = np.array([i[0] for i in b13])
    return b16, b15, b17, b14
def fonk5(b16, b17, b14, var_explained_required):
    a1 = 0
    a2 = 0
    for i in b14:
        a1 = a1 + i
        a2 = a2 + 1
        if a1 >= var_explained_required:
            break
    return b16[:, :a2], b17[:a2], b16[:, a2:]
class class1:
    b18 = StandardScaler()
    def fonk6(self, b20, qMAX, DMAX, b19 = False):
        if isinstance(b20, pd.DataFrame):
            b20 = b20.values
        b21 = []
        for i in range(1, qMAX):
            b1 = fonk1(b20, i)
            b7 = b20.shape[0] - b1.shape[0]
            b22 = b20[b7:]
            b10 = fonk3(b22, i, 100)
            b23 = b22 - np.dot(b1, b10)
            b24 = np.var(b23)
            b21.append(b24)
            if b19:
                print("Iteration - b25: {}, Variance: {}".format(i, b24))
        self.b25 = b21.index(min(b21)) + 1
        b21 = []
        b1 = fonk1(b20, self.b25)
        b7 = b20.shape[0] - b1.shape[0]
        b20 = b20[b7:]
        for i in range(1, DMAX):
            b10 = fonk3(b20, self.b25, i)
            b23 = b20 - np.dot(b1, b10)
            b24 = np.var(b23)
            b21.append(b24)
            if b19:
                print("Iteration - b26: {}, Variance: {}".format(i, b24))
        self.b26 = b21.index(min(b21)) + 1
        print("Optimal parameters are Q: {}, b26: {}".format(self.b25, self.b26))
        self.b10 = fonk3(b20, self.b25, self.b26)
        b23 = b20 - np.dot(b1, self.b10)
        self.b18.fonk6(b23)
        with open("b18", "wb") as f:
            pickle.dump(self.b18, f, pickle.HIGHEST_PROTOCOL)
    def fonk7(self, b20, b14):
        if isinstance(b20, pd.DataFrame):
            b20 = b20.values
        b1 = fonk1(b20 , self.b25)
        b7 = b20.shape[0] - b1.shape[0]
        b20 = b20[b7:]
        b23 = b20 - np.dot(b1, self.b10)
        with open("b18", "rb") as f:
            self.b18 = pickle.load(f)
        b23 = self.b18.transform(b23)
        b16, b15, b17, b27 = pca(b23)
        T_l, E_l, b28 = fonk5(b16, b17, b27, b14)
        b29 = fonk4(T_l, E_l)
        b30 = computeSPE(b28)
        b31 = pd.DataFrame(b20=np.concatenate((b29, b30), axis=1), columns=['b29', 'b30'])
        return b31