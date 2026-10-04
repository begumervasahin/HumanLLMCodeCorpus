from collections import Counter
import argparse
import itertools
import sys
def fonk1(source_file, b2):
    with open(source_file) as file:
        b1 = [line.strip().split() for line in file.readlines()]
    b2 = float(b2)
    b3 = len(b1)
    b4 = sorted(
        [item for item, count in Counter(itertools.chain.from_iterable(b1)).items()
         if float(count) / b3 > b2]
    )
    b5 = fonk2(b1)
    print("Frequent itemsets:")
    for item in b4:
        print(item)
    print("\nCandidates:")
    for candidate in b5:
        print(candidate)
def fonk2(b1):
    b5 = []
    b1 = sorted(fonk4(b1))
    b6 = sorted(
        [list(prefix) for prefix in set(frozenset(item[:-1]) for item in b1)]
    )
    for prefix in b6:
        b7 = [item[-1:] for item in b1 if item[:-1] == prefix]
        b7 = list(itertools.chain.from_iterable(b7))
        b8 = list(itertools.b8(b7, 2))
        for combination in b8:
            b5.append(prefix + list(combination))
    return b5
def fonk3(b9):
    b9 = float(b9)
    if b9 < 0.0 or b9 > 1.0:
        raise argparse.ArgumentTypeError(f"{b9} not in range [0.0, 1.0]")
    return b9
def fonk4(itemsets):
    if not isinstance(itemsets[0], list):
        return [[item] for item in itemsets]
    return itemsets
def fonk5(argv):
    b10 = argparse.ArgumentParser(description='Apriori algorithm implementation')
    b10.add_argument("source", b11 = "Source transaction file location")
    b10.add_argument("b2", b11 = "Minimum support", type=restricted_float)
    b12 = b10.parse_args()
    fonk1(b12.source, b12.b2)
if b13 = = "__main__":
    fonk5(sys.argv[1:])