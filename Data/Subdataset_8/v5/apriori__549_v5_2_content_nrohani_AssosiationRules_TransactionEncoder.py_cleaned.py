from scipy.sparse import csr_matrix
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
class TransactionEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.columns_ = None
        self.columns_mapping_ = None
    def fit(self, X):
        unique_items = set(item for transaction in X for item in transaction)
        self.columns_ = sorted(unique_items)
        self.columns_mapping_ = {item: idx for idx, item in enumerate(self.columns_)}
        return self
    def transform(self, X, sparse=False):
        if sparse:
            indptr = [0]
            indices = []
            for transaction in X:
                for item in set(transaction):
                    col_idx = self.columns_mapping_[item]
                    indices.append(col_idx)
                indptr.append(len(indices))
            non_sparse_values = [True]*len(indices)
            array = csr_matrix((non_sparse_values, indices, indptr), dtype=bool)
        else:
            array = np.zeros((len(X), len(self.columns_)), dtype=bool)
            for row_idx, transaction in enumerate(X):
                for item in transaction:
                    col_idx = self.columns_mapping_[item]
                    array[row_idx, col_idx] = True
        return array
    def inverse_transform(self, array):
        return [[self.columns_[idx] for idx, cell in enumerate(row) if cell] for row in array]
    def fit_transform(self, X, sparse=False):
        return self.fit(X).transform(X, sparse=sparse)