import csv
import numpy as np
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk2(self):
        return f"{list(self.b1)} -> {list(self.b2)} - support: {self.b3:.6f}, confidence: {self.b4:.6f}, b5: {self.b5:.6f}, b6: {self.b6:.6f}"
def fonk3(T, b7 = 0.01, min_conf=0.1):
    b8 = len(T)
    b9 = b7 * b8
    b10 = max(item for transaction in T for item in transaction)
    b11 = {frozenset(): 1}
    def fonk4(b1):
        return b11[b1]
    def fonk5(b1, b2):
        return fonk4(b1 | b2) / fonk4(b1)
    def fonk6(b1, b2):
        return fonk5(b1, b2) / fonk4(b2)
    def fonk7(b1, b2):
        return fonk4(b1 | b2) - fonk4(b1) * fonk4(b2)
    b12 = [0] * b10
    for transaction in T:
        for item in transaction:
            b12[item - 1] += 1
    b13 = {frozenset({x}): n / b8 for x, n in zip(range(1, b10 + 1), b12) if n >= b9}
    while b13:
        b11.update(b13)
        b2 = {x1 | x2: 0 for x1 in b13 for x2 in b13 if len(x1 - x2) == len(x2 - x1) == 1}
        for transaction in T:
            for candidate in b2:
                if candidate <= transaction:
                    b2[candidate] += 1
        b13 = {candidate: b12 / b8 for candidate, b12 in b2.items() if b12 >= b9}
    b14 = [class1(itemset, frozenset(), fonk4(itemset), 1.0, 1.0, 0.0) for itemset in b11]
    b15 = []
    while b14:
        b15.extend(b14)
        b16 = []
        for rule in b14:
            for x in rule.b1:
                b1 = rule.b1 - {x}
                b2 = rule.b2 | {x}
                if fonk5(b1, b2) >= min_conf:
                    b16.append(class1(b1, b2, fonk4(b1 | b2), fonk5(b1, b2), fonk6(b1, b2), fonk7(b1, b2)))
        b14 = b16
    return b15
def fonk8(b17 = 'retail.dat'):
    b18 = []
    with open(b17, 'r') as file:
        b19 = csv.b19(file, delimiter=' ')
        for row in b19:
            b18.append({int(x) for x in row if x})
    return b18
