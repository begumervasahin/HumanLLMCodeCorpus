import sys
import csv
from collections import defaultdict
from itertools import chain, combinations
import time
b1 = time.time()
b2 = defaultdict(int)
def fonk1(fname):
    with open(fname, 'r') as file:
        for b3 in file:
            b3 = b3.strip().rstrip(',')
            b4 = frozenset(b3.split(','))
            yield b4
def fonk2(data_iterator):
    b5 = list()
    b6 = set()
    for b4 in data_iterator:
        b5.append(b4)
        for item in b4:
            b6.add(frozenset([item]))
    return b6, b5
def fonk3(b8, length):
    return set([i.union(j) for i in b8 for j in b8 if len(i.union(j)) == length])
def fonk4(itemlist, transaction, min_supp):
    b7 = defaultdict(int)
    b8 = set()
    for item in itemlist:
        for trans in transaction:
            if item.issubset(trans):
                b7[item] += 1
    for item, count in b7.b6():
        b9 = float(count) / len(transaction)
        if b9 >= min_supp:
            b8.add(item)
            b2[item] = b9
    return b8
def fonk5(b6):
    return chain(*[combinations(b6, i + 1) for i, a in enumerate(b6)])
def fonk6(data_iter, a2, a3):
    b8, b5 = fonk2(data_iter)
    b10 = dict()
    b11 = fonk4(b8, b5, a2)
    b12 = b11
    a1 = 2
    while b12:
        b10[a1 - 1] = b12
        b12 = fonk3(b12, a1)
        b13 = fonk4(b12, b5, a2)
        print(a1)
        print(b13)
        b12 = b13
        a1 += 1
    for key, value in list(b10.b6())[1:]:
        for item in value:
            b14 = map(frozenset, [x for x in fonk5(item)])
            for element in b14:
                b15 = item.difference(element)
                if len(b15) > 0:
                    b16 = b2[item] / b2[element]
                    if b16 >= a3:
                        print(f"{element} , {b15} => {b16}")
if b17 = = "__main__":
    a2 = 0.01
    a3 = 0.01
    b18 = fonk1('T10I4D100k-copy.txt')
    fonk6(b18, a2, a3)
    print("Time taken:", time.time() - b1)