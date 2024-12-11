import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
def fonk1(b20, lag):
    b1 = b20[lag:]
    for l in range(1, lag + 1):
        b1 = np.hstack((b1, b20[lag - l:-l]))
    return b1
def fonk2(b20, time_diff):
    return b20[time_diff:] - b20[:-time_diff]
def fonk3(b20, lag, time_diff):
    b2 = fonk1(b20, lag)
    b3 = fonk2(b20, time_diff)
    b4 = fonk2(b2, time_diff)
    b3 = b3[len(b3) - len(b4):]
    b5 = np.linalg.inv(b4.T @ b4)
    b6 = b5 @ (b4.T @ b3)
    return b6
def fonk4(principal_components, b12):
    b7 = np.zeros((principal_components.shape[0], 1))
    for i in range(principal_components.shape[0]):
        b7[i] = sum((principal_components[i, k] ** 2) / b12[k] for k in range(principal_components.shape[1]))
    return b7
def fonk5(principal_components):
    b8 = np.array([np.sum(np.square(row)) for row in principal_components]).reshape(-1, 1)
    return b8
def fonk6(b20):
    b9 = np.cov(b20.T)
    b12, b10 = np.linalg.eig(b9)
    b11 = b12.argsort()[::-1]
    b12 = b12[b11]
    b10 = b10[:, b11]
    b13 = [(i / sum(b12)) for i in b12]
    b14 = b20 @ b10
    return b14, b10, b12, b13
def fonk7(b14, b12, b13, threshold):
    a1 = 0
    for i, variance in enumerate(b13, b15 = 1):
        a1 += variance
        if a1 >= threshold:
            return b14[:, :i], b12[:i], b14[:, i:]
class class1:
    def fonk8(self):
        self.b16 = StandardScaler()
        self.b17 = None
        self.b18 = None
        self.b6 = None
    def fonk9(self, b20, q_max, D_max, b19 = False):
        b20 = b20.values if isinstance(b20, pd.DataFrame) else b20
        optimal_q, b21 = self.fonk11(b20, q_max, D_max, b19)
        self.b17, self.b18 = optimal_q, b21
        b2 = fonk1(b20, self.b17)
        self.b6 = fonk3(b20[len(b20) - len(b2):], self.b17, self.b18)
        b22 = b20[len(b20) - len(b2):] - (b2 @ self.b6)
        self.b16.fonk9(b22)
        self._save_scaler()
        if b19:
            print(f"Optimal parameters are Q: {self.b17}, b18: {self.b18}")
    def fonk10(self, b20, variance_threshold):
        b20 = b20.values if isinstance(b20, pd.DataFrame) else b20
        b2 = fonk1(b20, self.b17)
        b22 = b20[len(b20) - len(b2):] - (b2 @ self.b6)
        self._load_scaler()
        b23 = self.b16.transform(b22)
        b14, _, b12, b13 = fonk6(b23)
        selected_scores, selected_eigenvalues, b24 = fonk7(
            b14, b12, b13, variance_threshold)
        b25 = fonk4(selected_scores, selected_eigenvalues)
        b26 = fonk5(b24)
        b27 = pd.DataFrame(np.concatenate((b25, b26), axis=1), columns=['b7', 'b8'])
        return b27
    def fonk11(self, b20, q_max, D_max, b19):
        """Finds the optimal lag (b17) and time difference (b18) parameters.
        Args:
            b20 (np.array): Input b20.
            q_max (int): Maximum lag value.
            D_max (int): Maximum time difference