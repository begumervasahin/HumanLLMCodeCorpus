from scipy.sparse import csr_matrix
import numpy as np
class TransactionEncoder:
    def __init__(self):
        self.columns_ = None
        self.columns_mapping_ = None
    def fit(self, transactions):
        unique_items = set(item for transaction in transactions for item in transaction)
        self.columns_ = sorted(unique_items)
        self.columns_mapping_ = {item: idx for idx, item in enumerate(self.columns_)}
        return self
    def transform(self, transactions, sparse=False):
        if sparse:
            indptr = [0]
            indices = []
            for transaction in transactions:
                for item in set(transaction):
                    indices.append(self.columns_mapping_[item])
                indptr.append(len(indices))
            data = [True] * len(indices)
            array = csr_matrix((data, indices, indptr), dtype=bool)
        else:
            array = np.zeros((len(transactions), len(self.columns_)), dtype=bool)
            for row_idx, transaction in enumerate(transactions):
                for item in transaction:
                    array[row_idx, self.columns_mapping_[item]] = True
        return array
    def inverse_transform(self, array):
        return [[self.columns_[idx] for idx, cell in enumerate(row) if cell] for row in array]
    def fit_transform(self, transactions, sparse=False):
        return self.fit(transactions).transform(transactions, sparse=sparse)
rules_data = [
    ["['dishes', 'bottled beer'] -> ['liquor (appetizer)']", 0.00061, 0.428571, 54.03846],
    ["['herbs', 'citrus fruit'] -> ['turkey']", 0.000712, 0.241379, 29.67457],
    ["['fruit/vegetable juice', 'root vegetables', 'other vegetables', 'tropical fruit'] -> ['turkey']", 0.00061, 0.24, 29.505],
    ["['ham', 'other vegetables', 'sliced cheese'] -> ['soft cheese']", 0.00061, 0.5, 29.27083],
]
print("Rules Data:")
for idx, rule in enumerate(rules_data):
    print(f"{idx + 1}. {rule[0]}    {rule[1]}    {rule[2]}    {rule[3]}")