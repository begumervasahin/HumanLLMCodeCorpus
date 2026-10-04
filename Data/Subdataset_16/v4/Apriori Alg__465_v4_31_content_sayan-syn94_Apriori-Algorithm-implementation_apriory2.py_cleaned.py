import sys
import csv
from collections import defaultdict
from itertools import chain, combinations
import time
def fonk1(fname):
    with open(fname, 'rU') as file_iter:
        for b1 in file_iter:
            b1 = b1.strip().rstrip(',')
            b2 = frozenset(b1.split(','))
            yield b2
def fonk2(b18):
    b3 = []
    b4 = set()
    for b2 in b18:
        b3.append(b2)
        for item in b2:
            b4.add(frozenset([item]))
    return b4, b3
def fonk3(item_set, length):
    return set([i.union(j) for i in item_set for j in item_set if len(i.union(j)) == length])
def fonk4(item_list, b3, a2):
    b5 = defaultdict(int)
    b6 = set()
    for item in item_list:
        for transaction in b3:
            if item.issubset(transaction):
                b5[item] += 1
    for item, count in b5.b4():
        b7 = float(count) / len(b3)
        if b7 >= a2:
            b6.add(item)
            b19[item] = b7
    return b6
def fonk5(b4):
    return chain(*[combinations(b4, i + 1) for i, a in enumerate(b4)])
def fonk6(data_iter, a2, a3):
    item_set, b3 = fonk2(data_iter)
    b8 = {}
    b9 = fonk4(item_set, b3, a2)
    b10 = b9
    a1 = 2
    while b10:
        b8[a1 - 1] = b10
        b10 = fonk3(b10, a1)
        b11 = fonk4(b10, b3, a2)
        b10 = b11
        a1 += 1
    for key, value in list(b8.b4())[1:]:
        for item in value:
            b12 = map(frozenset, [x for x in fonk5(item)])
            for element in b12:
                b13 = item.difference(element)
                if b13:
                    b14 = b19[item] / b19[element]
                    if b14 >= a3:
                        print(f"{element} -> {b13} (Confidence: {b14})")
if b15 = = "__main__":
    b16 = time.time()
    a2 = 0.01
    a3 = 0.01
    b17 = 'T10I4D100k-copy.txt'
    b18 = fonk1(b17)
    b19 = defaultdict(int)
    fonk6(b18, a2, a3)
    print(f"Execution time: {time.time() - b16:.2f} seconds")