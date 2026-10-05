import itertools
from collections import defaultdict, Counter
def fonk1(b12, a2):
    b1 = defaultdict(set)
    b2 = set()
    b3 = set()
    b4 = []
    a1 = 0
    with open(b12, "r") as file:
        for line in file:
            a1 += 1
            b5 = set(line.split())
            b4 += b5
            b1[a1] = b5
            b2 |= b5
    b6 = Counter(b4)
    for item, b10 in b6.items():
        if b10 / a1 > a2:
            b3.add(item)
    return b1, b3
def fonk2(b3, b8):
    b7 = set()
    if b8 = = 2:
        b7 = {(x, y) for x in b3 for y in b3 if x != y}
    else:
        for x in b3:
            for y in b3:
                if len(set(x).union(y)) == b8:
                    b7.add(tuple(set(x).union(y)))
        b7 = [c for c in b7 if all(subset in b3 for subset in fonk3(c))]
    return b7
def fonk3(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def fonk4(b7, b1, a2):
    b9 = set()
    with open('pres.txt', 'a') as file:
        for candidate in b7:
            b10 = sum(1 for basket in b1.values() if set(candidate).issubset(basket))
            b11 = b10 / len(b1)
            if b11 > a2:
                b9.add(candidate)
                print(candidate)
                file.write(str(candidate))
    return b9
def fonk5():
    a2 = 0.08
    b12 = "browsing.txt"
    b1, b9 = fonk1(b12, a2)
    for b8 in range(2, 5):
        b7 = fonk2(b9, b8)
        b9 = fonk4(b7, b1, a2)
    return b9
if b13 = = '__main__':
    fonk5()