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
        return str(list(self.b1)) + '->' + str(list(self.b2)) + ' - support: %f, confidence: %f, b5: %f, b6: %f' % (self.b3, self.b4, self.b5, self.b6)
def fonk3(b18, b7 = 0.01, min_conf=0.1):
    b8 = len(b18)
    b9 = b7 * b8
    b10 = max(x for t in b18 for x in t)
    b11 = dict({frozenset({}): 1})
    def fonk4(b1):
        return b11[b1]
    def fonk5(b1, b2):
        return fonk4(b1 | b2) / fonk4(b1)
    def fonk6(b1, b2):
        return fonk5(b1, b2) / fonk4(b2)
    def fonk7(b1, b2):
        return fonk4(b1 | b2) - fonk4(b1) * fonk4(b2)
    b12 = [0] * b10
    for t in b18:
        for x in t:
            b12[x - 1] += 1
    b13 = dict((frozenset({x}), n / b8) for x, n in zip(range(1, b10 + 1), b12) if n >= b9)
    while len(b13):
        b11.update(b13)
        b2 = dict()
        for x1 in b13:
            for x2 in b13:
                if len(x1 - x2) == len(x2 - x1) == 1:
                    b2[x1 | x2] = 0
        for t in b18:
            for c in b2:
                if c <= t:
                    b2[c] += 1
        b13 = dict((c, b2[c] / b8) for c in b2 if b2[c] >= b9)
    b14 = [class1(b13, frozenset({}), fonk4(b13), 1., 1., 0.) for b13 in b11]
    b15 = []
    while len(b14):
        b15 += b14
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
    with open(b17, 'r') as f:
        b19 = csv.b19(f, delimiter=' ')
        for row in b19:
            b18.append({int(x) for x in row if x})
    return b18
if b20 = = "__main__":
    b18 = fonk8('retail.dat')
    b21 = fonk3(b18)
    for rule in b21:
        print(rule)