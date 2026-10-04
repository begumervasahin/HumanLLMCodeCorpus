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
    for itemset1 in previous_level_itemsets:
        for itemset2 in previous_level_itemsets:
            b3 = itemset1.union(itemset2)
            if len(b3) == a1 and not fonk1(b3, previous_level_itemsets):
                b2.append(b3)
    return list(set(b2))
def fonk3(b7, b14):
    b4 = defaultdict(int)
    for transaction in b7:
        for item in transaction:
            b4[item] += 1
    b5 = len(b7)
    b6 = [
        frozenset([item])
        for item, count in b4.items()
        if float(count) / b5 >= b14
    ]
    return b6
def fonk4(b7, b14):
    b7 = [frozenset(transaction) for transaction in b7]
    b8 = [None, fonk3(b7, b14)]
    a1 = 2
    while b8[a1-1]:
        b2 = fonk2(b8[a1-1], a1)
        b9 = defaultdict(int)
        for transaction in b7:
            for b3 in b2:
                if b3.issubset(transaction):
                    b9[b3] += 1
        b5 = len(b7)
        b8.append([
            itemset
            for itemset, count in b9.items()
            if float(count) / b5 >= b14
        ])
        a1 += 1
    return b8
def fonk5():
    b10 = OptionParser()
    b10.add_option('-f', '--inputFile', b11 = 'input', help='filename containing CSV', default=None)
    b10.add_option('-s', '--minSupport', b11 = 'b14', help='minimum support value', default=0.15, type='float')
    options, b12 = b10.parse_args()
    if not options.input:
        print("Please provide an input file using the -f option.")
        sys.exit(1)
    with open(options.input, 'r') as infile:
        b13 = csv.reader(infile)
        b7 = list(b13)
    b14 = options.b14
    b15 = fonk4(b7, b14)
    for level in b15:
        if level:
            for itemset in level:
                print(itemset)
if b16 = = '__main__':
    fonk5()