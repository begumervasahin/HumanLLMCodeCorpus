import sys
import csv
from collections import defaultdict
from optparse import OptionParser
def fonk1(candidate, b21):
    for item in candidate:
        b1 = candidate - frozenset([item])
        if b1 not in b21:
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
    b4 = [set(row) for row in database]
    b5 = defaultdict(int)
    for row in b4:
        for item in row:
            b5[item] += 1
    b6 = len(database)
    b7 = []
    for key, value in b5.items():
        if float(value) / b6 >= min_support:
            b7.append(frozenset([key]))
    return b7
def fonk4(database, min_support):
    b8 = list(database)
    b4 = [frozenset(row) for row in b8]
    b7 = [frozenset()]
    b7.append(fonk3(b8, min_support))
    a1 = 2
    b9 = [frozenset(), frozenset()]
    b10 = len(b4)
    while len(b7[a1 - 1]) != 0:
        b9.append(fonk2(b7[a1 - 1], a1))
        b11 = defaultdict(int)
        for b3 in b9[a1]:
            for s in b4:
                if b3.issubset(s):
                    b11[b3] += 1
        b12 = []
        for key, value in b11.items():
            if float(value) / b10 >= min_support:
                b12.append(key)
        b7.append(frozenset(b12))
        a1 += 1
    return b7
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
    b18 = open(options.input, 'r')
    b19 = options.minS
    b20 = csv.reader(b18)
    b21 = fonk4(b20, b19)
    print(b21)
if b22 = = '__main__':
    fonk5()