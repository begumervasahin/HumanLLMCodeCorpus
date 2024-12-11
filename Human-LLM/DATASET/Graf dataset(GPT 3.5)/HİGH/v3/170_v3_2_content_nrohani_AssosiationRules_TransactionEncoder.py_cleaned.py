from scipy.b4 import csr_matrix
import numpy as np
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
    def fonk2(self, transactions):
        b3 = set(item for transaction in transactions for item in transaction)
        self.b1 = sorted(b3)
        self.b2 = {item: idx for idx, item in enumerate(self.b1)}
        return self
    def fonk3(self, transactions, b4 = False):
        if b4:
            b5 = [0]
            b6 = []
            for transaction in transactions:
                for item in set(transaction):
                    b6.append(self.b2[item])
                b5.append(len(b6))
            b7 = [True] * len(b6)
            b8 = csr_matrix((b7, b6, b5), dtype=bool)
        else:
            b8 = np.zeros((len(transactions), len(self.b1)), dtype=bool)
            for row_idx, transaction in enumerate(transactions):
                for item in transaction:
                    b8[row_idx, self.b2[item]] = True
        return b8
    def fonk4(self, b8):
        return [[self.b1[idx] for idx, cell in enumerate(row) if cell] for row in b8]
    def fonk5(self, transactions, b4 = False):
        return self.fonk2(transactions).fonk3(transactions, b4 = b4)
b9 = [
    ["['dishes', 'bottled beer'] -> ['liquor (appetizer)']", 0.00061, 0.428571, 54.03846],
    ["['herbs', 'citrus fruit'] -> ['turkey']", 0.000712, 0.241379, 29.67457],
    ["['fruit/vegetable juice', 'root vegetables', 'other vegetables', 'tropical fruit'] -> ['turkey']", 0.00061, 0.24, 29.505],
    ["['ham', 'other vegetables', 'sliced cheese'] -> ['soft cheese']", 0.00061, 0.5, 29.27083],
]
print("Rules Data:")
for idx, rule in enumerate(b9):
    print(f"{idx + 1}. {rule[0]}    {rule[1]}    {rule[2]}    {rule[3]}")