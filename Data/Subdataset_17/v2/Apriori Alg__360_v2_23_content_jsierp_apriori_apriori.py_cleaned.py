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
        return f"{list(self.A)} -> {list(self.C)} - support: {self.supp:.4f}, confidence: {self.conf:.4f}, lift: {self.lift:.4f}, leverage: {self.leverage:.4f}"
def apriori(T, min_supp=0.01, min_conf=0.1):
    N = len(T)
    supp_count = min_supp * N
    d = max(x for t in T for x in t)
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
    for t in T:
        for x in t:
            count[x - 1] += 1
    l = {frozenset({x}): n / N for x, n in zip(range(1, d + 1), count) if n >= supp_count}
    while l:
        L.update(l)
        C = {}
        for x1 in l:
            for x2 in l:
                if len(x1 - x2) == len(x2 - x1) == 1:
                    C[x1 | x2] = 0
        for t in T:
            for c in C:
                if c <= t:
                    C[c] += 1
        l = {c: C[c] / N for c in C if C[c] >= supp_count}
    s = [Rule(l, frozenset(), supp(l), 1.0, 1.0, 0.0) for l in L]
    S = []
    while s:
        S.extend(s)
        s_next = []
        for rule in s:
            for x in rule.A:
                A = rule.A - {x}
                C = rule.C | {x}
                if conf(A, C) >= min_conf:
                    s_next.append(Rule(A, C, supp(A | C), conf(A, C), lift(A, C), leverage(A, C)))
        s = s_next
    return S
def load(path='retail.dat'):
    T = []
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            T.append({int(x) for x in row if x})
    return T
if __name__ == "__main__":
    T = load('retail.dat')
    rules = apriori(T)
    for rule in rules:
        print(rule)