import time
from collections import defaultdict, Counter
import itertools
def fonk1(b14, a2):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    a1 = 0
    with open(b14, "r") as f:
        for line in f:
            a1 += 1
            b5 = set(line.split())
            b4 += b5
            b1[a1] = b5
            b2 = b2.union(b5)
    b6 = Counter(b4)
    for item in b2:
        b7 = b6[item]
        if float(b7) / a1 > a2:
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
    b10 = list(itertools.combinations(b8, len(b8) - 1))
    return b10
def fonk4(b8, b1, a2):
    b3 = set()
    b11 = open('pres.txt', 'a')
    for c in b8:
        b12 = sum(1 for b9 in b1 if set(c).issubset(b1[b9]))
        b13 = float(b12) / len(b1)
        if b13 > a2:
            b3.add(c)
            print(c)
            b11.write(str(c) + '\n')
    b11.close()
    return b3
def fonk5():
    b9 = 4
    a2 = 0.08
    b14 = "browsing.txt"
    b8 = set()
    b3 = set()
    b1, b3 = fonk1(b14, a2)
    for i in range(2, b9 + 1):
        b8 = fonk2(b3, i)
        b3 = fonk4(b8, b1, a2)
    return b3
if b15 = = '__main__':
    fonk5()