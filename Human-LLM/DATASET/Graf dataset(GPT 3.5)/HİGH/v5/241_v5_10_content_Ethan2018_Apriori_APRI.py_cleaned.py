import itertools
from collections import defaultdict, Counter
def fonk1(b12, a1):
    b1 = defaultdict(set)
    b2 = set()
    b3 = []
    with open(b12, "r") as file:
        for line in file:
            b4 = set(line.split())
            b3 += b4
            b1[len(b1) + 1] = b4
            b2 |= b4
    b5 = Counter(b3)
    b2 = {item for item in b2 if b5[item] / len(b1) > a1}
    return b1, b2
def fonk2(b2, b7):
    b6 = set()
    if b7 = = 2:
        b6 = {(x, y) for x in b2 for y in b2 if x != y}
    else:
        for x in b2:
            for y in b2:
                if len(set(x).union(y)) == b7:
                    b6.add(tuple(set(x).union(y)))
        for candidate in list(b6):
            b8 = fonk3(candidate)
            if any(subset not in b2 for subset in b8):
                b6.remove(candidate)
    return b6
def fonk3(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def fonk4(b6, b1, a1):
    b9 = set()
    with open('pres.txt', 'a') as pref:
        for candidate in b6:
            b10 = sum(1 for basket in b1.values() if set(candidate).issubset(basket))
            b11 = b10 / len(b1)
            if b11 > a1:
                b9.add(candidate)
                print(candidate)
                pref.write(str(candidate))
    return b9
def fonk5():
    a1 = 0.08
    b12 = "browsing.txt"
    a2 = 4
    b1, b2 = fonk1(b12, a1)
    for b7 in range(2, a2 + 1):
        b6 = fonk2(b2, b7)
        b2 = fonk4(b6, b1, a1)
    return b2
if b13 = = '__main__':
    fonk5()