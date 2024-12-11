import sys
import csv
from collections import defaultdict
from optparse import OptionParser
def fonk1(b3, b6):
    for item in b3:
        b1 = b3 - frozenset([item])
        if b1 not in b6:
            return True
    return False
def fonk2(Lk_1, a1):
    b2 = []
    for i in range(len(Lk_1)):
        for j in range(i + 1, len(Lk_1)):
            b3 = Lk_1[i].union(Lk_1[j])
            if len(b3) == a1 and not fonk1(b3, Lk_1):
                b2.append(b3)
    return b2
def fonk3(database, min_support):
    b4 = defaultdict(int)
    for row in database:
        for item in set(row):
            b4[item] += 1
    b5 = len(database)
    b6 = [frozenset([key]) for key, value in b4.items()
                         if value / b5 >= min_support]
    return b6
def fonk4(database, min_support):
    b7 = list(database)
    b8 = [frozenset(row) for row in b7]
    b9 = [frozenset()]
    b9.append(fonk3(b7, min_support))
    a1 = 2
    b10 = [frozenset(), frozenset()]
    b5 = len(b8)
    while len(b9[a1 - 1]) != 0:
        b10.append(fonk2(b9[a1 - 1], a1))
        b11 = defaultdict(int)
        for b3 in b10[a1]:
            for transaction in b8:
                if b3.issubset(transaction):
                    b11[b3] += 1
        b12 = [key for key, value in b11.items()
                               if value / b5 >= min_support]
        b9.append(b12)
        a1 += 1
    return b9
def fonk5():
    b13 = OptionParser()
    b13.add_option(
        '-f',
        '--inputFile',
        b14 = 'input',
        b15 = 'filename containing csv',
        b16 = None)
    b13.add_option(
        '-s',
        '--minSupport',
        b14 = 'minS',
        b15 = 'minimum support value',
        b16 = 0.15,
        b17 = 'float')
    (options, args) = b13.parse_args()
    if not options.input:
        print('Please provide an input file using -f or --inputFile option')
        return
    with open(options.input, 'r') as infile:
        b18 = options.minS
        b19 = csv.reader(infile)
        b6 = fonk4(b19, b18)
        print(b6)
if b20 = = '__main__':
    fonk5()