from scipy.b4 import csr_matrix
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
class class1(BaseEstimator, TransformerMixin):
    def fonk1(self):
        self.b1 = None
        self.b2 = None
    def fonk2(self, X):
        b3 = set(item for transaction in X for item in transaction)
        self.b1 = sorted(b3)
        self.b2 = {item: idx for idx, item in enumerate(self.b1)}
        return self
    def fonk3(self, X, b4 = False):
        if b4:
            b5 = [0]
            b6 = []
            for transaction in X:
                for item in set(transaction):
                    b7 = self.b2[item]
                    b6.append(b7)
                b5.append(len(b6))
            b8 = [True]*len(b6)
            b9 = csr_matrix((b8, b6, b5), dtype=bool)
        else:
            b9 = np.zeros((len(X), len(self.b1)), dtype=bool)
            for row_idx, transaction in enumerate(X):
                for item in transaction:
                    b7 = self.b2[item]
                    b9[row_idx, b7] = True
        return b9
    def fonk4(self, b9):
        return [[self.b1[idx] for idx, cell in enumerate(row) if cell] for row in b9]
    def fonk5(self, X, b4 = False):
        return self.fonk2(X).fonk3(X, b4 = b4)