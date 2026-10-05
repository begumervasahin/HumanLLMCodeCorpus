from collections import defaultdict
import csv
from optparse import OptionParser
def fonk1(b3, b5):
    for item in b3:
        b1 = b3 - frozenset([item])
        if b1 not in b5:
            return True
    return False
def fonk2(b5, a2):
    b2 = []
    for i, freq_itemset1 in enumerate(b5):
        for freq_itemset2 in b5[i + 1:]:
            b3 = freq_itemset1.union(freq_itemset2)
            if len(b3) == a2 and not fonk1(b3, b5):
                b2.append(b3)
    return b2
def fonk3(database, b14):
    b4 = defaultdict(int)
    a1 = 0
    for transaction in database:
        a1 += 1
        for item in transaction:
            b4[item] += 1
    b5 = [frozenset([item]) for item, count in b4.items()
                         if count / a1 >= b14]
    return b5
def fonk4(database, b14):
    b6 = list(database)
    b5 = [frozenset()]
    b5.append(fonk3(b6, b14))
    a2 = 2
    a1 = len(b6)
    b2 = [frozenset(), frozenset()]
    while len(b5[a2 - 1]) != 0:
        b2.append(fonk2(b5[a2 - 1], a2))
        b7 = defaultdict(int)
        for b3 in b2[a2]:
            for transaction in b6:
                if b3.issubset(transaction):
                    b7[b3] += 1
        b8 = [itemset for itemset, count in b7.items()
                               if count / a1 >= b14]
        b5.append(b8)
        a2 += 1
    return b5
def fonk5():
    b9 = OptionParser()
    b9.add_option(
        '-f',
        '--inputFile',
        b10 = 'input',
        b11 = 'filename containing csv',
        b12 = None)
    b9.add_option(
        '-s',
        '--minSupport',
        b10 = 'minS',
        b11 = 'minimum support value',
        b12 = 0.15,
        b13 = 'float')
    (options, args) = b9.parse_args()
    if not options.input:
        print('Please provide an input file using -f or --inputFile option')
        return
    with open(options.input, 'r') as infile:
        b14 = options.minS
        b15 = csv.reader(infile)
        b5 = fonk4(b15, b14)
        print(b5)
if b16 = = '__main__':
    fonk5()