from scipy.b5 import csr_matrix
import numpy as np
class class1:
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
            b9 = [True]*len(b7)
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
b11 = [
    ["['dishes', 'bottled beer'] -> ['liquor (appetizer)']", 0.00061, 0.428571, 54.03846],
    ["['herbs', 'citrus fruit'] -> ['turkey']", 0.000712, 0.241379, 29.67457],
    ["['fruit/vegetable juice', 'root vegetables', 'other vegetables', 'tropical fruit'] -> ['turkey']", 0.00061, 0.24, 29.505],
    ["['ham', 'other vegetables', 'sliced cheese'] -> ['soft cheese']", 0.00061, 0.5, 29.27083],
]
print("Rules Data:")
for idx, rule in enumerate(b11):
    print(f"{idx + 1}. {rule[0]}    {rule[1]}    {rule[2]}    {rule[3]}")