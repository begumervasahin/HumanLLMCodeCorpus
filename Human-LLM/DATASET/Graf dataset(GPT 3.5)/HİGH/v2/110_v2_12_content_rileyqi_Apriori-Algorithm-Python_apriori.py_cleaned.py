from collections import defaultdict
import csv
from optparse import OptionParser
def fonk1(b3, b6):
    for item in b3:
        b1 = b3 - frozenset([item])
        if b1 not in b6:
            return True
    return False
def fonk2(b6, a1):
    b2 = []
    for i in range(len(b6)):
        for j in range(i + 1, len(b6)):
            b3 = b6[i].union(b6[j])
            if len(b3) == a1 and not fonk1(b3, b6):
                b2.append(b3)
    return b2
def fonk3(database, b17):
    b4 = defaultdict(int)
    for transaction in database:
        for item in transaction:
            b4[item] += 1
    b5 = len(database)
    b6 = []
    for item, count in b4.items():
        b7 = float(count) / b5
        if b7 >= b17:
            b6.append(frozenset([item]))
    return b6
def fonk4(database, b17):
    b8 = list(database)
    b6 = [frozenset()]
    b6.append(fonk3(b8, b17))
    a1 = 2
    b2 = [frozenset(), frozenset()]
    b5 = len(b8)
    while len(b6[a1 - 1]) != 0:
        b2.append(fonk2(b6[a1 - 1], a1))
        b9 = defaultdict(int)
        for b3 in b2[a1]:
            for transaction in b8:
                if b3.issubset(transaction):
                    b9[b3] += 1
        b10 = []
        for itemset, count in b9.items():
            b7 = float(count) / b5
            if b7 >= b17:
                b10.append(itemset)
        b6.append(b10)
        a1 += 1
    return b6
def fonk5():
    b11 = OptionParser()
    b11.add_option(
        '-f',
        '--inputFile',
        b12 = 'input',
        b13 = 'filename containing csv',
        b14 = None)
    b11.add_option(
        '-s',
        '--minSupport',
        b12 = 'minS',
        b13 = 'minimum b7 value',
        b14 = 0.15,
        b15 = 'float')
    (options, args) = b11.parse_args()
    if not options.input:
        print('Please provide an input file using -f or --inputFile option')
        return
    b16 = open(options.input, 'r')
    b17 = options.minS
    b18 = csv.reader(b16)
    b6 = fonk4(b18, b17)
    print(b6)
if b19 = = '__main__':
    fonk5()