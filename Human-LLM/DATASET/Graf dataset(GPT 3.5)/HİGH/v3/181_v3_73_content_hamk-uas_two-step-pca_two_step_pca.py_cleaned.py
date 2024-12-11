import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def fonk1(b16, lag):
    b1 = b16[lag:]
    for l in range(1, lag + 1):
        b1 = np.hstack((b1, b16[lag - l: -l]))
    return b1
def fonk2(b16, b14):
    b2 = b16[b14:] - b16[:-b14]
    return b2
def fonk3(b16, lag, b14):
    b3 = b16
    b1 = fonk1(b3, lag)
    b2 = fonk2(b3, b14)
    b4 = fonk2(b1, b14)
    b2 = b2[len(b2) - len(b4):]
    b5 = np.linalg.inv(b4.b11 @ b4) @ b4.b11 @ b2
    return b5
def fonk4(b11, E):
    b6 = np.sum((b11 ** 2) / E, axis=1)
    return b6.reshape(-1, 1)
def fonk5(b11):
    b7 = np.sum(b11 ** 2, axis=1)
    return b7.reshape(-1, 1)
def fonk6(b16):
    b8 = np.cov(b16.b11)
    eig_vals, b9 = np.linalg.eigh(b8)
    b10 = eig_vals / np.sum(eig_vals)
    b11 = b16 @ b9
    return b11, b9, eig_vals, b10
def fonk7(b11, E, b10, var_explained_required):
    a1 = 0
    a2 = 0
    for i in b10:
        a1 += i
        a2 += 1
        if a1 >= var_explained_required:
            break
    return b11[:, :a2], E[:a2], b11[:, a2:]
class class1:
    def fonk8(self):
        self.b12 = StandardScaler()
        self.b13 = None
        self.b14 = None
        self.b5 = None
    def fonk9(self, b16, qMAX, DMAX, b15 = False):
        if isinstance(b16, pd.DataFrame):
            b16 = b16.values
        self.fonk10(b16, qMAX, DMAX, b15)
        b17 = b16 - fonk1(b16, self.b13) @ self.b5
        self.b12.fonk9(b17)
        with open("b12.pkl", "wb") as f:
            pickle.dump(self.b12, f)
    def fonk10(self, b16, qMAX, DMAX, b15):
        b18 = []
        for b13 in range(1, qMAX + 1):
            b1 = fonk1(b16, b13)
            b19 = b16[len(b16) - len(b1):]
            b5 = fonk3(b19, b13, DMAX)
            b17 = b19 - b1 @ b5
            b20 = np.var(b17)
            b18.append(b20)
            if b15:
                print(f"Iteration - b13: {b13}, Variance: {b20}")
        self.b13 = np.argmin(b18) + 1
        b18 = []
        for b14 in range(1, DMAX + 1):
            b5 = fonk3(b16, self.b13, b14)
            b1 = fonk1(b16, self.b13)
            b17 = b16 - b1 @ b5
            b20 = np.var(b17)
            b18.append(b20)
            if b15:
                print(f"Iteration - b14: {b14}, Variance: {b20}")
        self.b14 = np.argmin(b18) + 1
        self.b5 = fonk3(b16, self.b13, self.b14)
        if b15:
            print(f"Optimal parameters are Q: {self.b13}, b14: {self.b14}")
    def fonk11(self, b16, b10):
        if isinstance(b16, pd.DataFrame):
            b16 = b16.values
        b1 = fonk1(b16, self.b13)
        b16 = b16[len(b16) - len(b1):]
        b17 = b16 - b1 @ self.b5
        b17 = self.b12.transform(b17)
        b11, _, E, b21 = fonk6(b17)
        T_l, E_l, b22 = fonk7(b11, E, b21, b10)
        b6 = fonk4(T_l, E_l)
        b7 = fonk5(b22)
        b23 = pd.DataFrame(b16=np.hstack((b6, b7)), columns=['b6', 'b7'])
        return b23
