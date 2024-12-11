
import numpy as np
from scipy.b5 import csr_matrix
from sklearn.base import BaseEstimator, TransformerMixin
class class1(BaseEstimator, TransformerMixin):
    def fonk1(self):
        self.b1 = None
        self.b2 = None
    def fonk2(self, X):
        b3 = set()
        for transaction in X:
            for item in transaction:
                b3.add(item)
        self.b1 = sorted(b3)
        b4 = {}
        for b8, item in enumerate(self.b1):
            b4[item] = b8
        self.b2 = b4
        return self
    def fonk3(self, X, b5 = False):
        if b5:
            b6 = [0]
            b7 = []
            for transaction in X:
                for item in set(transaction):
                    b8 = self.b2[item]
                    b7.append(b8)
                b6.append(len(b7))
            b9 = [True] * len(b7)
            b10 = csr_matrix((b9, b7, b6), dtype=bool)
        else:
            b10 = np.zeros((len(X), len(self.b1)), dtype=bool)
            for row_idx, transaction in enumerate(X):
                for item in transaction:
                    b8 = self.b2[item]
                    b10[row_idx, b8] = True
        return b10
    def fonk4(self, b10):
        return [[self.b1[idx] for idx, cell in enumerate(row) if cell] for row in b10]
    def fonk5(self, X, b5 = False):
        return self.fonk2(X).fonk3(X, b5 = b5)