import argparse
import itertools
import sys
from collections import Counter
def fonk1(source_file, minsup):
    b1 = fonk2(source_file)
    b2 = len(b1)
    b3 = fonk3(b1, minsup, b2)
    b4 = fonk4(b1)
def fonk2(source_file):
    with open(source_file) as file:
        return [line.strip().split() for line in file.readlines()]
def fonk3(b1, minsup, b2):
    b5 = list(itertools.chain.from_iterable(b1))
    b6 = Counter(b5)
    return sorted([item for item, count in b6.items() if count / b2 >= minsup])
def fonk4(b1):
    b4 = []
    b1 = sorted(fonk5(b1))
    b7 = sorted([list(x) for x in set(frozenset(item[:-1]) for item in b1)])
    for prefix in b7:
        b8 = [item[-1:] for item in b1 if item[:-1] == prefix]
        b8 = list(itertools.chain.from_iterable(b8))
        b9 = list(itertools.b9(b8, 2))
        for combination in b9:
            b4.append(prefix + list(combination))
    return b4
def fonk5(data):
    if not isinstance(data[0], list):
        return [[item] for item in data]
    return data
def fonk6(b10):
    b10 = float(b10)
    if b10 < 0.0 or b10 > 1.0:
        raise argparse.ArgumentTypeError(f"{b10} not in range [0.0, 1.0]")
    return b10
def fonk7(argv):
    b11 = argparse.ArgumentParser(description='Apriori algorithm implementation')
    b11.add_argument("source", b12 = "Source transaction file location")
    b11.add_argument("minsup", b12 = "Minimum support (0.0 - 1.0)", type=restricted_float)
    return b11.parse_args(argv)
def fonk8(argv):
    b13 = fonk7(argv)
    fonk1(b13.source, b13.minsup)
if b14 = = "__main__":
    fonk8(sys.argv[1:])