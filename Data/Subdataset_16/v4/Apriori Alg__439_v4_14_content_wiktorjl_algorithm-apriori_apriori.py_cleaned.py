from collections import Counter
import argparse
import itertools
import sys
def fonk1(source_file, b2):
    with open(source_file) as file:
        b1 = [line.strip().split() for line in file.readlines()]
    b2 = float(b2)
    b3 = len(b1)
    b4 = list(itertools.chain.from_iterable(b1))
    b5 = Counter(b4)
    b6 = sorted([item for item, count in b5.items() if count / b3 >= b2])
    b7 = fonk2(b1)
def fonk2(b1):
    b7 = []
    b1 = sorted(fonk4(b1))
    b8 = sorted([list(x) for x in set(frozenset(item[:-1]) for item in b1)])
    for prefix in b8:
        b9 = [item[-1:] for item in b1 if item[:-1] == prefix]
        b9 = list(itertools.chain.from_iterable(b9))
        b10 = list(itertools.b10(b9, 2))
        for combination in b10:
            b7.append(prefix + list(combination))
    return b7
def fonk3(b11):
    b11 = float(b11)
    if b11 < 0.0 or b11 > 1.0:
        raise argparse.ArgumentTypeError(f"{b11} not in range [0.0, 1.0]")
    return b11
def fonk4(data):
    if not isinstance(data[0], list):
        return [[item] for item in data]
    else:
        return data
def fonk5(argv):
    b12 = argparse.ArgumentParser(description='Apriori algorithm implementation')
    b12.add_argument("source", b13 = "Source transaction file location")
    b12.add_argument("b2", b13 = "Minimum support (0.0 - 1.0)", type=restricted_float)
    b14 = b12.parse_args()
    fonk1(b14.source, b14.b2)
if b15 = = "__main__":
    fonk5(sys.argv[1:])