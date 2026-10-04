import sys
from collections import defaultdict
from optparse import OptionParser
import csv
def fonk1(b3, Lk_1):
    for item in b3:
        b1 = b3 - frozenset([item])
        if (b1 not in Lk_1):
            return True
    return False
def fonk2(Lk_1, a1):
    b2 = []
    for i in Lk_1:
        for j in Lk_1:
            b3 = i.union(j)
            if len(b3) == a1 and not fonk1(b3, Lk_1):
                b2.append(b3)
    b4 = set(b2)
    return list(b4)
def fonk3(b9, b19):
    b5 = [set(row) for row in b9]
    b6 = defaultdict(int)
    for row in b5:
        for item in row:
            b6[item] += 1
    b7 = len(b9)
    b8 = [frozenset([key]) for key, value in b6.items() if float(value) / b7 >= b19]
    return b8
def fonk4(database, b19):
    b9 = [row for row in database]
    b5 = [frozenset(row) for row in b9]
    b8 = [frozenset()]
    b8.append(fonk3(b9, b19))
    a1 = 2
    b10 = [frozenset()] * 2
    b11 = len(b5)
    while len(b8[a1-1]) != 0:
        b10.append(fonk2(b8[a1-1], a1))
        b12 = defaultdict(int)
        for b3 in b10[a1]:
            for s in b5:
                if b3.issubset(s):
                    b12[b3] += 1
        b13 = [key for key, value in b12.items() if float(value) / b11 >= b19]
        b8.append(frozenset(b13))
        a1 += 1
    return b8
def fonk5():
    b14 = OptionParser()
    b14.add_option(
        '-f',
        '--inputFile',
        b15 = 'input',
        b16 = 'filename containing csv',
        b17 = None)
    b14.add_option(
        '-s',
        '--minSupport',
        b15 = 'minS',
        b16 = 'minimum support value',
        b17 = 0.15,
        b18 = 'float')
    (options, args) = b14.parse_args()
    if options.input is None:
        print("Please specify an input file using the -f option.")
        sys.exit(1)
    b19 = options.minS
    with open(options.input, 'r') as infile:
        b20 = csv.reader(infile)
        b8 = fonk4(b20, b19)
        for i, level in enumerate(b8):
            print(f"Frequent itemsets of size {i}:")
            for itemset in level:
                print(itemset)
if b21 = = '__main__':
    fonk5()