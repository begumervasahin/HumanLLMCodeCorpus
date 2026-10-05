import time
from collections import defaultdict, Counter
import itertools
def fonk1(b12, a3):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    a1 = 0
    with open(b12, "r") as f:
        for line in f:
            a1 += 1
            b5 = line.split()
            b5 = set(b5)
            b4 += b5
            b1[a1] = b5
            b2 = b2.union(b5)
    b6 = Counter(b4)
    for item in b2:
        b7 = b6[item]
        if float(b7) / a1 > a3:
            b3.add(item)
    return b1, b3
def fonk2(b3, b9):
    b8 = set()
    if b9 = = 2:
        for x in b3:
            for y in b3:
                if x != y:
                    b8.add((x, y))
    else:
        for x in b3:
            for y in b3:
                if len(set(x).union(y)) == b9:
                    b8.add(tuple(set(x).union(y)))
        b8 = list(b8)
        for c in b8:
            b10 = fonk3(c)
            if any([x not in b3 for x in b10]):
                b8.remove(c)
    return set(b8)
def fonk3(b8):
    b10 = []
    b10.extend(itertools.combinations(b8, len(b8) - 1))
    return b10
def fonk4(b8, b1, a3):
    b3 = set()
    a2 = 0
    with open('pres.txt', 'a') as pref:
        for c in b8:
            for b9 in b1:
                if set(c).issubset(b1[b9]):
                    a2 += 1
            b11 = float(a2) / len(b1)
            if b11 > a3:
                b3.add(c)
                print(c)
                pref.write(str(c))
    return b3
def fonk5():
    b9 = 4
    a3 = 0.08
    b12 = "browsing.txt"
    b8 = set()
    b3 = set()
    b1, b3 = fonk1(b12, a3)
    for i in range(2, b9 + 1):
        b8 = fonk2(b3, i)
        b3 = fonk4(b8, b1, a3)
    return b3
if b13 = = '__main__':
    fonk5()