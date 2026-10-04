29. Repository: ikravche/Apriori
   File: Apriori.py
   URL: https:
   Code Content:
import numpy as np
import itertools as it
a1 = 3
a2 = 0.7
a3 = 1
b1 = {}
b2 = {}
b3 = [['a', 'b'],
                    ['a', 'c', 'd', 'e'],
                    ['a', 'b', 'c', 'e'],
                    ['c', 'd'],
                    ['b', 'c', 'd', 'e'],
                    ['a', 'd', 'e'],
                    ['c', 'd', 'e']]
b4 = set([item for sublist in b3 for item in
                    sublist])
def fonk1():
    a4 = 0
    for key, value in b1.iteritems():
        if len(key) == a3 - 1:
            if value > a4:
                a4 = value
    if np.logical_and(a4 < a1, a3 > 1):
        return False
    else:
        return True
def fonk2():
    if fonk1():
        b5 = list(it.b5(b4, a3))
        fonk3(b5)
    else:
        print(b1)
        for key, value in b1.iteritems():
            if value >= a1:
                print('Elements: ' + str(key) + ' support ' + str(value))
def fonk3(comb):
    global a3
    b6 = set(comb)
    print(b6)
    for b7 in comb:
        for b8 in b3:
            fonk4(b7, b8)
    a3 += 1
    fonk2()
def fonk4(el, ro):
    b7 = ''.join(sorted(el))
    b8 = ''.join(sorted(ro))
    b8 = fonk5(b7, b8)
    if np.logical_and(b7 in b8, b7 in b1):
        b1[b7] += 1
    elif b7 in b8:
        b1[b7] = 1
def fonk5(el, ro):
    b8 = ro[:]
    for row_char in ro:
        if row_char not in el:
            b8 = b8.replace(row_char, '')
    return b8
fonk2()
   README Content:
Implementation of Apriori Algorithm
Apriori is an algorithm for frequent item set mining and association rule learning over transactional databases.
It proceeds by identifying the frequent individual items in the database and extending them to larger and larger
item sets as long as those item sets appear sufficiently often in the database.
The frequent item sets determined by Apriori can be used to determine association rules
which highlight general trends in the database:
this has applications in domains such as market basket analysis.
