import itertools
from collections import defaultdict, Counter
def fonk1(b13, a2):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    a1 = 0
    with open(b13, "r") as file:
        for line in file:
            a1 += 1
            b5 = set(line.split())
            b4 += b5
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
            if any([x not in b3 for x in b10]):
                b8.remove(candidate)
    return set(b8)
def fonk3(candidate):
    b10 = []
    b10.extend(itertools.combinations(candidate, len(candidate) - 1))
    return b10
def fonk4(b8, b1, a2):
    b11 = set()
    with open('pres.txt', 'a') as file:
        for candidate in b8:
            b7 = 0
            for basket in b1.values():
                if set(candidate).issubset(basket):
                    b7 += 1
            b12 = b7 / len(b1)
            if b12 > a2:
                b11.add(candidate)
                print(candidate)
                file.write(str(candidate))
    return b11
def fonk5():
    a2 = 0.08
    b13 = "browsing.txt"
    b1 = defaultdict(set)
    b11 = set()
    b1, b11 = fonk1(b13, a2)
    for b9 in range(2, 5):
        b8 = fonk2(b11, b9)
        b11 = fonk4(b8, b1, a2)
    return b11
if b14 = = '__main__':
    fonk5()