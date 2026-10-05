import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def fonk1(b21, lag):
    b1 = b21[lag:]
    for l in range(1, lag + 1):
        b1 = np.hstack((b1, b21[lag - l:-l]))
    return b1
def fonk2(b21, time_diff):
    b2 = b21[time_diff:] - b21[:-time_diff]
    return b2
def fonk3(b21, lag, time_diff):
    b3 = fonk1(b21, lag)
    b4 = fonk2(b21, time_diff)
    b5 = fonk2(b3, time_diff)
    b4 = b4[len(b4) - len(b5):]
    b6 = np.linalg.inv(b5.T @ b5)
    b7 = b6 @ (b5.T @ b4)
    return b7
def fonk4(principal_components, b13):
    b8 = np.zeros((principal_components.shape[0], 1))
    for i in range(principal_components.shape[0]):
        b8[i] = sum((principal_components[i, k] ** 2) / b13[k] for k in range(principal_components.shape[1]))
    return b8
def fonk5(principal_components):
    b9 = np.array([np.sum(np.square(row)) for row in principal_components]).reshape(-1, 1)
    return b9
def fonk6(b21):
    b10 = np.cov(b21.T)
    b13, b11 = np.linalg.eig(b10)
    b12 = b13.argsort()[::-1]
    b13 = b13[b12]
    b11 = b11[:, b12]
    b14 = [(i / sum(b13)) for i in b13]
    b15 = b21 @ b11
    return b15, b11, b13, b14
def fonk7(b15, b13, b14, threshold):
    a1 = 0
    for i, variance in enumerate(b14, b16 = 1):
        a1 += variance
        if a1 >= threshold:
            return b15[:, :i], b13[:i], b15[:, i:]
class class1:
    def fonk8(self):
        self.b17 = StandardScaler()
        self.b18 = None
        self.b19 = None
        self.b7 = None
    def fonk9(self, b21, q_max, D_max, b20 = False):
        b21 = b21.values if isinstance(b21, pd.DataFrame) else b21
        optimal_q, b22 = self._find_optimal_parameters(b21, q_max, D_max, b20)
        self.b18, self.b19 = optimal_q, b22
        b3 = fonk1(b21, self.b18)
        self.b7 = fonk3(b21[len(b21) - len(b3):], self.b18, self.b19)
        b23 = b21[len(b21) - len(b3):] - (b3 @ self.b7)
        self.b17.fonk9(b23)
        self._save_scaler()
        if b20:
            print(f"Optimal parameters are Q: {self.b18}, b19: {self.b19}")
    def fonk10(self, b21, variance_threshold):
        b21 = b21.values if isinstance(b21, pd.DataFrame) else b21
        b3 = fonk1(b21, self.b18)
        b23 = b21[len(b21) - len(b3):] - (b3 @ self.b7)
        self._load_scaler()
        b24 = self.b17.transform(b23)
        b15, _, b13, b14 = fonk6(b24)
        selected_scores, selected_eigenvalues, b25 = fonk7(
            b15, b13, b14, variance_threshold)
        b26 = fonk4(selected_scores, selected_eigenvalues)
        b27 = fonk5(b25)
        b28 = pd.DataFrame(np.concatenate((b8