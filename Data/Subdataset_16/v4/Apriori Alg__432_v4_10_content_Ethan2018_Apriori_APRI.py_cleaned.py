import time
from collections import defaultdict, Counter
import itertools
def fonk1(filename, a2):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    a1 = 0
    with open(filename, "r") as file:
        for line in file:
            a1 += 1
            b5 = set(line.split())
            b4.extend(b5)
            b1[a1] = b5
            b2 = b2.union(b5)
    b6 = Counter(b4)
    for item in b2:
        b7 = b6[item]
        if b7 / a1 > a2:
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
        for candidate in b8:
            b10 = fonk3(candidate)
            if any(subset not in b3 for subset in b10):
                b8.remove(candidate)
    return set(b8)
def fonk3(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def fonk4(b8, b1, a2):
    b3 = set()
    b7 = 0
    with open('pres.txt', 'a') as pref:
        for candidate in b8:
            for b5 in b1.values():
                if set(candidate).issubset(b5):
                    b7 += 1
            b11 = b7 / len(b1)
            if b11 > a2:
                b3.add(candidate)
                print(candidate)
                pref.write(str(candidate) + '\n')
    return b3
def fonk5():
    b9 = 4
    a2 = 0.08
    b12 = "browsing.txt"
    b1, b3 = fonk1(b12, a2)
    for i in range(2, b9 + 1):
        b8 = fonk2(b3, i)
        b3 = fonk4(b8, b1, a2)
    return b3
if b13 = = '__main__':
    fonk5()