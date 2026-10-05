import time
from collections import defaultdict, Counter
import itertools
def fonk1(b11, a2):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    with open(b11, "r") as file:
        for line in file:
            b5 = set(line.split())
            b4 += b5
            b1[len(b1) + 1] = b5
            b2 |= b5
    b6 = Counter(b4)
    for item in b2:
        if b6[item] / len(b1) > a2:
            b3.add(item)
    return b1, b3
def fonk2(b3, b8):
    b7 = set()
    if b8 = = 2:
        for x in b3:
            for y in b3:
                if x != y:
                    b7.add((x, y))
    else:
        for x in b3:
            for y in b3:
                if len(set(x).union(y)) == b8:
                    b7.add(tuple(set(x).union(y)))
        b7 = list(b7)
        for b12 in b7:
            b9 = fonk3(b12)
            if any([x not in b3 for x in b9]):
                b7.remove(b12)
    return set(b7)
def fonk3(b12):
    return list(itertools.combinations(b12, len(b12) - 1))
def fonk4(b12, b1, a2):
    b3 = set()
    a1 = 0
    with open('pres.txt', 'a') as pref:
        for c in b12:
            for b8 in b1:
                if set(c).issubset(b1[b8]):
                    a1 += 1
            b10 = float(a1) / len(b1)
            if b10 > a2:
                b3.add(c)
                print(c)
                pref.write(str(c))
    return b3
def fonk5():
    a2 = 0.08
    b11 = "browsing.txt"
    b8 = 4
    b1, b3 = fonk1(b11, a2)
    for i in range(2, b8 + 1):
        b12 = fonk2(b3, i)
        b3 = fonk4(b12, b1, a2)
    return b3
if b13 = = '__main__':
    fonk5()