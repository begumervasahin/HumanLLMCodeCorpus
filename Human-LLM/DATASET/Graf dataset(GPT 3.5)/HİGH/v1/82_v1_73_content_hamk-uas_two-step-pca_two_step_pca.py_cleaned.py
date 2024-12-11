import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def fonk1(b20, lag):
    b1 = b20[lag:]
    for l in range(1, lag + 1):
        b1 = np.hstack((b1, b20[lag - l: -l]))
    return b1
def fonk2(b20, b18):
    n_samples, b2 = b20.shape
    b3 = b20[b18:] - b20[:-b18]
    return b3
def fonk3(b20, lag, b18):
    b4 = b20
    b1 = fonk1(b4, lag)
    b3 = fonk2(b4, b18)
    b5 = fonk2(b1, b18)
    b6 = b3.shape[0] - b5.shape[0]
    b3 = b3[b6:]
    b7 = np.linalg.inv(b5.b15 @ b5)
    b8 = b5.b15 @ b3
    b9 = b7 @ b8
    return b9
def fonk4(b15, E):
    b10 = np.zeros((b15.shape[0], 1))
    for i in range(b15.shape[0]):
        for k in range(b15.shape[1]):
            b10[i] += (b15[i, k] ** 2) / E[k]
    return b10
def fonk5(b15):
    b11 = np.zeros((b15.shape[0], 1))
    for i in range(b15.shape[0]):
        b11[i] = np.sum(b15[i] ** 2)
    return b11
def fonk6(b20):
    b12 = np.cov(b20.b15)
    eig_vals, b13 = np.linalg.eigh(b12)
    b14 = [(i / sum(eig_vals)) for i in sorted(eig_vals, reverse=True)]
    b15 = b20 @ b13
    return b15, b13, eig_vals, b14
def fonk7(b15, E, b14, var_explained_required):
    a1 = 0
    a2 = 0
    for i in b14:
        a1 += i
        a2 += 1
        if a1 >= var_explained_required:
            break
    return b15[:, :a2], E[:a2], b15[:, a2:]
class class1:
    def fonk8(self):
        self.b16 = StandardScaler()
        self.b17 = None
        self.b18 = None
        self.b9 = None
    def fonk9(self, b20, qMAX, DMAX, b19 = False):
        if isinstance(b20, pd.DataFrame):
            b20 = b20.values
        self.fonk10(b20, qMAX, DMAX, b19)
        b21 = b20 - fonk1(b20, self.b17) @ self.b9
        self.b16.fonk9(b21)
        with open("b16.pkl", "wb") as f:
            pickle.dump(self.b16, f)
    def fonk10(self, b20, qMAX, DMAX, b19):
        b22 = []
        for b17 in range(1, qMAX + 1):
            b1 = fonk1(b20, b17)
            b6 = b20.shape[0] - b1.shape[0]
            b23 = b20[b6:]
            b9 = fonk3(b23, b17, DMAX)
            b21 = b23 - b1 @ b9
            b24 = np.var(b21)
            b22.append(b24)
            if b19:
                print(f"Iteration - b17: {b17}, Variance: {b24}")
        self.b17 = np.argmin(b22) + 1
        b22 = []
        for b18 in range(1, DMAX + 1):
            b9 = fonk3(b20, self.b17, b18)
            b1 = fonk1(b20, self.b17)
            b21 = b20 - b1 @ b9
            b24 = np.var(b21)
            b22.append(b24)
            if b19:
                print(f"Iteration - b18: {b18}, Variance: {b24}")
        self.b18 = np.argmin(b22) + 1
        self.b9 = fonk3(b20, self.b17, self.b18)
        if b19:
            print(f"Optimal parameters are Q: {self.b17}, b18: {self.b18}")
    def fonk11(self, b20, b14):
        if isinstance(b20, pd.DataFrame):
            b20 = b20.values
        b1 = fonk1(b20, self.b17)
        b6 = b20.shape[0] - b1.shape[0]
        b20 = b20[b6:]
        b21 = b20 - b1 @ self.b9
        b21 = self.b16.transform(b21)
        b15, P, E, b25 = fonk6(b21)
        T_l, E_l, b26 = fonk7(b15, E, b25, b14)
        b10 = fonk4(T_l, E_l)
        b11 = fonk5(b26)
        b27 = pd.DataFrame(b20=np.hstack((b10, b11)), columns=['b10', 'b11'])
        return b27
