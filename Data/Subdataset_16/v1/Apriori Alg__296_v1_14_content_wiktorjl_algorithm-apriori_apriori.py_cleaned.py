from collections import Counter
import argparse
import itertools
import sys
def fonk1(source_file, b2):
    with open(source_file) as file:
        b1 = [line.strip().split() for line in file.readlines()]
    b2 = float(b2)
    b3 = len(b1)
    b4 = sorted([k for k, v in Counter(itertools.chain.from_iterable(b1)).items() if float(v) / b3 > b2])
    b5 = fonk2(b1)
    print("Frequent itemsets:")
    for item in b4:
        print(item)
    print("\nCandidates:")
    for candidate in b5:
        print(candidate)
def fonk2(b6):
    b5 = []
    b6 = sorted(fonk4(b6))
    b7 = sorted([list(x) for x in set(frozenset(i) for i in (set(i[:-1]) for i in b6))])
    for prefix in b7:
        b8 = [p[-1:] for p in b6 if p[:-1] == prefix]
        b8 = list(itertools.chain.from_iterable(b8))
        b9 = list(itertools.combinations(b8, 2))
        for c in b9:
            b5.append(prefix + list(c))
    return b5
def fonk3(b10):
    b10 = float(b10)
    if b10 < 0.0 or b10 > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (b10,))
    return b10
def fonk4(b4):
    if not isinstance(b4[0], list):
        return [[x] for x in b4]
    else:
        return b4
def fonk5(argv):
    b11 = argparse.ArgumentParser(description='Apriori algorithm')
    b11.add_argument("source", b12 = "Source transaction file location")
    b11.add_argument("b2", b12 = "Minimum support", type=restricted_float)
    b13 = b11.parse_args()
    fonk1(b13.source, b13.b2)
if b14 = = "__main__":
    fonk5(sys.argv[1:])