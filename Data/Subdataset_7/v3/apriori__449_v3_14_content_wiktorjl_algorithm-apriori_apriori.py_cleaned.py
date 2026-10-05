from collections import Counter
import argparse
import itertools
def fonk1(source_file, b2):
    b1 = fonk2(source_file)
    b2 = float(b2)
    b3 = len(b1)
    b4 = fonk3(b1, b2)
    b5 = fonk4(b1)
def fonk2(source_file):
    with open(source_file) as file:
        return [line.strip().split() for line in file.readlines()]
def fonk3(b1, b2):
    b6 = list(itertools.chain.from_iterable(b1))
    b7 = Counter(b6)
    b8 = len(b1)
    b4 = [item for item, count in b7.items() if count / b8 > b2]
    return sorted(b4)
def fonk4(b1):
    b5 = []
    b1 = sorted(fonk6(b1))
    b9 = sorted([list(x) for x in set(frozenset(i) for i in (set(i[:-1]) for i in b1))])
    for prefix in b9:
        b10 = [p[-1:] for p in b1 if p[:-1] == prefix]
        b10 = list(itertools.chain.from_iterable(b10))
        b11 = list(itertools.combinations(b10, 2))
        for c in b11:
            b5.append(prefix + list(c))
    return b5
def fonk5(b12):
    b12 = float(b12)
    if b12 < 0.0 or b12 > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (b12,))
    return b12
def fonk6(F):
    if not isinstance(F[0], list):
        return [[x] for x in F]
    else:
        return F
def fonk7():
    b13 = argparse.ArgumentParser(description='Apriori algorithm')
    b13.add_argument("source", b14 = "Source transaction file location")
    b13.add_argument("b2", b14 = "Minimum support", type=restricted_float)
    b15 = b13.parse_args()
    fonk1(b15.source, b15.b2)
if b16 = = "__main__":
    fonk7()