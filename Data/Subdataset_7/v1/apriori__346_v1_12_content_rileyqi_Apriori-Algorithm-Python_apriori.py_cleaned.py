from collections import defaultdict
import csv
from optparse import OptionParser
def fonk1(b3, Lk_1):
    for item in b3:
        b1 = b3 - frozenset([item])
        if b1 not in Lk_1:
            return True
    return False
def fonk2(Lk_1, a1):
    b2 = []
    for i in range(len(Lk_1)):
        for j in range(i + 1, len(Lk_1)):
            b3 = Lk_1[i].union(Lk_1[j])
            if len(b3) == a1:
                if not fonk1(b3, Lk_1):
                    b2.append(b3)
    return b2
def fonk3(b7, b19):
    b4 = defaultdict(int)
    for row in b7:
        for item in row:
            b4[item] += 1
    b5 = len(b7)
    b6 = []
    for key, value in b4.items():
        if float(value) / b5 >= b19:
            b6.append(frozenset([key]))
    return b6
def fonk4(database, b19):
    b7 = list(database)
    b8 = [set(row) for row in b7]
    b6 = [frozenset()]
    b6.append(fonk3(b7, b19))
    a1 = 2
    b9 = [frozenset(), frozenset()]
    b10 = len(b8)
    while len(b6[a1 - 1]) != 0:
        b9.append(fonk2(b6[a1 - 1], a1))
        b11 = defaultdict(int)
        for b3 in b9[a1]:
            for s in b8:
                if b3.issubset(s):
                    b11[b3] += 1
        b12 = []
        for key, value in b11.items():
            if float(value) / b10 >= b19:
                b12.append(key)
        b6.append(frozenset(b12))
        a1 += 1
    return b6
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
    b6 = fonk4(b20, b19)
    print(b6)
if b21 = = '__main__':
    fonk5()