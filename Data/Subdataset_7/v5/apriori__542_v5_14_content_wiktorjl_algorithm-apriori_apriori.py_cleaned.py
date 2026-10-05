from collections import Counter
import argparse
import itertools
import sys
def fonk1(source_file, b2):
    with open(source_file) as file:
        b1 = [line.strip().split() for line in file.readlines()]
    b2 = float(b2)
    b3 = len(b1)
    b4 = fonk2(b1, b2, b3)
    b5 = fonk3(b1)
def fonk2(b1, b2, b3):
    b6 = Counter(list(itertools.chain.from_iterable(b1)))
    b4 = sorted([item for item, count in b6.items() if count / b3 > b2])
    return b4
def fonk3(b7):
    b5 = []
    b7 = sorted(fonk5(b7))
    b8 = sorted([list(x) for x in set(frozenset(i) for i in (set(i[:-1]) for i in b7))])
    for prefix in b8:
        b9 = [p[-1:] for p in b7 if p[:-1] == prefix]
        b9 = list(itertools.chain.from_iterable(b9))
        b10 = list(itertools.combinations(b9, 2))
        for c in b10:
            b5.append(prefix + list(c))
    return b5
def fonk4(b11):
    b11 = float(b11)
    if b11 < 0.0 or b11 > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (b11,))
    return b11
def fonk5(F):
    if not isinstance(F[0], list):
        return [[x] for x in F]
    else:
        return F
def fonk6(argv):
    b12 = argparse.ArgumentParser(description='Apriori algorithm')
    b12.add_argument("source", b13 = "Source transaction file location")
    b12.add_argument("b2", b13 = "Minimum support", type=restricted_float)
    b14 = b12.parse_args()
    fonk1(b14.source, b14.b2)
if b15 = = "__main__":
    fonk6(sys.argv[1:])