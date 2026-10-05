import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def shift_data(data, lag):
    tildaX = data[lag:]
    for l in range(1, lag + 1):
        tildaX = np.hstack((tildaX, data[lag - l: -l]))
    return tildaX
def delta(data, D):
    dX = data[D:] - data[:-D]
    return dX
def calcA(data, lag, D):
    X = data
    tildaX = shift_data(X, lag)
    dX = delta(X, D)
    dtildaX = delta(tildaX, D)
    dX = dX[len(dX) - len(dtildaX):]
    A = np.linalg.inv(dtildaX.T @ dtildaX) @ dtildaX.T @ dX
    return A
def computeT2(T, E):
    T2 = np.sum((T ** 2) / E, axis=1)
    return T2.reshape(-1, 1)
def computeSPE(T):
    SPE = np.sum(T ** 2, axis=1)
    return SPE.reshape(-1, 1)
def pca(data):
    cov_matrix = np.cov(data.T)
    eig_vals, eig_vectors = np.linalg.eigh(cov_matrix)
    var_explained = eig_vals / np.sum(eig_vals)
    T = data @ eig_vectors
    return T, eig_vectors, eig_vals, var_explained
def dividePCs(T, E, var_explained, var_explained_required):
    total_var = 0
    n_pca = 0
    for i in var_explained:
        total_var += i
        n_pca += 1
        if total_var >= var_explained_required:
            break
    return T[:, :n_pca], E[:n_pca], T[:, n_pca:]
class TS_PCA:
    def __init__(self):
        self.scaler = StandardScaler()
        self.q = None
        self.D = None
        self.A = None
    def fit(self, data, qMAX, DMAX, verbose=False):
        if isinstance(data, pd.DataFrame):
            data = data.values
        self._fit(data, qMAX, DMAX, verbose)
        U = data - shift_data(data, self.q) @ self.A
        self.scaler.fit(U)
        with open("scaler.pkl", "wb") as f:
            pickle.dump(self.scaler, f)
    def _fit(self, data, qMAX, DMAX, verbose):
        min_var = []
        for q in range(1, qMAX + 1):
            tildaX = shift_data(data, q)
            temp_data = data[len(data) - len(tildaX):]
            A = calcA(temp_data, q, DMAX)
            U = temp_data - tildaX @ A
            U_v = np.var(U)
            min_var.append(U_v)
            if verbose:
                print(f"Iteration - q: {q}, Variance: {U_v}")
        self.q = np.argmin(min_var) + 1
        min_var = []
        for D in range(1, DMAX + 1):
            A = calcA(data, self.q, D)
            tildaX = shift_data(data, self.q)
            U = data - tildaX @ A
            U_v = np.var(U)
            min_var.append(U_v)
            if verbose:
                print(f"Iteration - D: {D}, Variance: {U_v}")
        self.D = np.argmin(min_var) + 1
        self.A = calcA(data, self.q, self.D)
        if verbose:
            print(f"Optimal parameters are Q: {self.q}, D: {self.D}")
    def detect(self, data, var_explained):
        if isinstance(data, pd.DataFrame):
            data = data.values
        tildaX = shift_data(data, self.q)
        data = data[len(data) - len(tildaX):]
        U = data - tildaX @ self.A
        U = self.scaler.transform(U)
        T, _, E, var_explained_list = pca(U)
        T_l, E_l, T_rest = dividePCs(T, E, var_explained_list, var_explained)
        T2 = computeT2(T_l, E_l)
        SPE = computeSPE(T_rest)
        metrics_df = pd.DataFrame(data=np.hstack((T2, SPE)), columns=['T2', 'SPE'])
        return metrics_df
