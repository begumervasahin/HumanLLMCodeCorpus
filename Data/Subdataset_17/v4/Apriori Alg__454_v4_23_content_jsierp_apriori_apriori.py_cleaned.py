import csv
import numpy as np
class Rule:
    def __init__(self, A, C, supp, conf, lift, leverage):
        self.A = A
        self.C = C
        self.supp = supp
        self.conf = conf
        self.lift = lift
        self.leverage = leverage
    def __str__(self):
        return f"{list(self.A)} -> {list(self.C)} - support: {self.supp:.6f}, confidence: {self.conf:.6f}, lift: {self.lift:.6f}, leverage: {self.leverage:.6f}"
def apriori(T, min_supp=0.01, min_conf=0.1):
    N = len(T)
    supp_count = min_supp * N
    d = max(item for transaction in T for item in transaction)
    L = {frozenset(): 1}
    def supp(A):
        return L[A]
    def conf(A, C):
        return supp(A | C) / supp(A)
    def lift(A, C):
        return conf(A, C) / supp(C)
    def leverage(A, C):
        return supp(A | C) - supp(A) * supp(C)
    count = [0] * d
    for transaction in T:
        for item in transaction:
            count[item - 1] += 1
    l = {frozenset({x}): n / N for x, n in zip(range(1, d + 1), count) if n >= supp_count}
    while l:
        L.update(l)
        C = {x1 | x2: 0 for x1 in l for x2 in l if len(x1 - x2) == len(x2 - x1) == 1}
        for transaction in T:
            for candidate in C:
                if candidate <= transaction:
                    C[candidate] += 1
        l = {candidate: count / N for candidate, count in C.items() if count >= supp_count}
    rules = [Rule(itemset, frozenset(), supp(itemset), 1.0, 1.0, 0.0) for itemset in L]
    final_rules = []
    while rules:
        final_rules.extend(rules)
        next_rules = []
        for rule in rules:
            for x in rule.A:
                A = rule.A - {x}
                C = rule.C | {x}
                if conf(A, C) >= min_conf:
                    next_rules.append(Rule(A, C, supp(A | C), conf(A, C), lift(A, C), leverage(A, C)))
        rules = next_rules
    return final_rules
def load(path='retail.dat'):
    transactions = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            transactions.append({int(x) for x in row if x})
    return transactions
