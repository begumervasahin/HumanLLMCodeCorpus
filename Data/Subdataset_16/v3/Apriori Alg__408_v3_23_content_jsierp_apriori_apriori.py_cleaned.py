import csv
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk2(self):
        return f"{list(self.b1)} -> {list(self.b2)} - support: {self.b3:.4f}, confidence: {self.b4:.4f}, b5: {self.b5:.4f}, b6: {self.b6:.4f}"
def fonk3(b21, b7 = 0.01, min_conf=0.1):
    b8 = len(b21)
    b9 = b7 * b8
    b10 = max(item for transaction in b21 for item in transaction)
    b11 = {frozenset(): 1}
    def fonk4(itemset):
        return b11[itemset]
    def fonk5(b18, b19):
        return fonk4(b18 | b19) / fonk4(b18)
    def fonk6(b18, b19):
        return fonk5(b18, b19) / fonk4(b19)
    def fonk7(b18, b19):
        return fonk4(b18 | b19) - fonk4(b18) * fonk4(b19)
    b12 = [0] * b10
    for transaction in b21:
        for item in transaction:
            b12[item - 1] += 1
    b13 = {frozenset({item}): count / b8 for item, count in zip(range(1, b10 + 1), b12) if count >= b9}
    while b13:
        b11.update(b13)
        b14 = {}
        for itemset1 in b13:
            for itemset2 in b13:
                if len(itemset1 - itemset2) == len(itemset2 - itemset1) == 1:
                    b14[itemset1 | itemset2] = 0
        for transaction in b21:
            for candidate in b14:
                if candidate <= transaction:
                    b14[candidate] += 1
        b13 = {candidate: count / b8 for candidate, count in b14.items() if count >= b9}
    b15 = [class1(itemset, frozenset(), fonk4(itemset), 1.0, 1.0, 0.0) for itemset in b11]
    b16 = []
    while b15:
        b16.extend(b15)
        b17 = []
        for rule in b15:
            for item in rule.b1:
                b18 = rule.b1 - {item}
                b19 = rule.b2 | {item}
                if fonk5(b18, b19) >= min_conf:
                    b17.append(class1(b18, b19, fonk4(b18 | b19), fonk5(b18, b19), fonk6(b18, b19), fonk7(b18, b19)))
        b15 = b17
    return b16
def fonk8(b20 = 'retail.dat'):
    b21 = []
    with open(b20, 'r') as file:
        b22 = csv.b22(file, delimiter=' ')
        for row in b22:
            b21.append({int(item) for item in row if item})
    return b21
if b23 = = "__main__":
    b21 = fonk8('retail.dat')
    b24 = fonk3(b21)
    for rule in b24:
        print(rule)