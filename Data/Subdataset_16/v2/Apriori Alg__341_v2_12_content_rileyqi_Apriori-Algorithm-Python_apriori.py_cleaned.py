import sys
from collections import defaultdict
from optparse import OptionParser
import csv
def fonk1(b3, previous_level_itemsets):
    for item in b3:
        b1 = b3 - frozenset([item])
        if b1 not in previous_level_itemsets:
            return True
    return False
def fonk2(previous_level_itemsets, a1):
    b2 = []
    for i in previous_level_itemsets:
        for j in previous_level_itemsets:
            b3 = i.union(j)
            if len(b3) == a1 and not fonk1(b3, previous_level_itemsets):
                b2.append(b3)
    return list(set(b2))
def fonk3(b6, b15):
    b4 = defaultdict(int)
    for transaction in b6:
        for item in transaction:
            b4[item] += 1
    b5 = len(b6)
    return [frozenset([item]) for item, count in b4.items() if count / b5 >= b15]
def fonk4(b6, b15):
    b6 = [frozenset(transaction) for transaction in b6]
    b7 = [frozenset()]
    b7.append(fonk3(b6, b15))
    a1 = 2
    while b7[a1-1]:
        b2 = fonk2(b7[a1-1], a1)
        b8 = defaultdict(int)
        for b3 in b2:
            for transaction in b6:
                if b3.issubset(transaction):
                    b8[b3] += 1
        b5 = len(b6)
        b9 = [itemset for itemset, count in b8.items() if count / b5 >= b15]
        b7.append(frozenset(b9))
        a1 += 1
    return b7
def fonk5():
    b10 = OptionParser()
    b10.add_option(
        '-f',
        '--inputFile',
        b11 = 'input',
        b12 = 'Filename containing CSV data',
        b13 = None
    )
    b10.add_option(
        '-s',
        '--minSupport',
        b11 = 'b15',
        b12 = 'Minimum support value',
        b13 = 0.15,
        b14 = 'float'
    )
    (options, args) = b10.parse_args()
    if options.input is None:
        print("Please specify an input file using the -f option.")
        sys.exit(1)
    b15 = options.b15
    with open(options.input, 'r') as infile:
        b16 = csv.reader(infile)
        b6 = [row for row in b16]
    b7 = fonk4(b6, b15)
    for i, level in enumerate(b7):
        print(f"Frequent itemsets of size {i}:")
        for itemset in level:
            print(itemset)
if b17 = = '__main__':
    fonk5()