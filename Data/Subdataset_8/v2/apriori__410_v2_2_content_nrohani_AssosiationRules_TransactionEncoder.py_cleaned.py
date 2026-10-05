from scipy.sparse import csr_matrix
import numpy as np
class TransactionEncoder:
    def __init__(self):
        self.columns_ = None
        self.columns_mapping_ = None
    def fit(self, X):
        unique_items = set()
        for transaction in X:
            for item in transaction:
                unique_items.add(item)
        self.columns_ = sorted(unique_items)
        columns_mapping = {}
        for col_idx, item in enumerate(self.columns_):
            columns_mapping[item] = col_idx
        self.columns_mapping_ = columns_mapping
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
rules_data = [
    ["['dishes', 'bottled beer'] -> ['liquor (appetizer)']", 0.00061, 0.428571, 54.03846],
    ["['herbs', 'citrus fruit'] -> ['turkey']", 0.000712, 0.241379, 29.67457],
    ["['fruit/vegetable juice', 'root vegetables', 'other vegetables', 'tropical fruit'] -> ['turkey']", 0.00061, 0.24, 29.505],
    ["['ham', 'other vegetables', 'sliced cheese'] -> ['soft cheese']", 0.00061, 0.5, 29.27083],
]
print("Rules Data:")
for idx, rule in enumerate(rules_data):
    print(f"{idx + 1}. {rule[0]}    {rule[1]}    {rule[2]}    {rule[3]}")