import time
from collections import defaultdict, Counter
import itertools
def fonk1(b12, a2):
    b1 = defaultdict(set)
    b2 = []
    a1 = 0
    with open(b12, "r") as f:
        for line in f:
            a1 += 1
            b3 = set(line.split())
            b2 += b3
            b1[a1] = b3
    b4 = set(b2)
    b5 = Counter(b2)
    b6 = {item for item in b4 if float(b5[item]) / a1 > a2}
    return b1, b6
def fonk2(b6, b7):
    if b7 = = 2:
        return {(x, y) for x in b6 for y in b6 if x != y}
    b8 = {tuple(set(x).union(y)) for x in b6 for y in b6 if len(set(x).union(y)) == b7}
    return {c for c in b8 if all(subset in b6 for subset in fonk3(c))}
def fonk3(b13):
    return list(itertools.combinations(b13, len(b13) - 1))
def fonk4(b13, b1, a2):
    b6 = set()
    b9 = len(b1)
    with open('pres.txt', 'a') as pref:
        for c in b13:
            b10 = sum(1 for b3 in b1.values() if set(c).issubset(b3))
            b11 = float(b10) / b9
            if b11 > a2:
                b6.add(c)
                print(c)
                pref.write(str(c) + '\n')
    return b6
def fonk5():
    b7 = 4
    a2 = 0.08
    b12 = "browsing.txt"
    b1, b6 = fonk1(b12, a2)
    for i in range(2, b7 + 1):
        b13 = fonk2(b6, i)
        b6 = fonk4(b13, b1, a2)
    return b6
if b14 = = '__main__':
    fonk5()