import sys
import csv
import time
from collections import defaultdict
from itertools import chain, combinations
b1 = time.time()
b2 = defaultdict(int)
def fonk1(fname):
    with open(fname, 'r') as file:
        for line in file:
            b3 = frozenset(line.strip().rstrip(',').split(','))
            yield b3
def fonk2(data_iterator):
    b4 = []
    b5 = set()
    for b3 in data_iterator:
        b4.append(b3)
        for item in b3:
            b5.add(frozenset([item]))
    return b5, b4
def fonk3(b5, length):
    return set([i.union(j) for i in b5 for j in b5 if len(i.union(j)) == length])
def fonk4(item_list, transactions, min_supp):
    b6 = defaultdict(int)
    b7 = set()
    for item in item_list:
        for transaction in transactions:
            if item.issubset(transaction):
                b6[item] += 1
    for item, count in b6.items():
        b8 = float(count) / len(transactions)
        if b8 >= min_supp:
            b7.add(item)
            b2[item] = b8
    return b7
def fonk5(items):
    return chain(*[combinations(items, i + 1) for i, _ in enumerate(items)])
def fonk6(data_iter, a2, a3):
    b5, b4 = fonk2(data_iter)
    b9 = {}
    b10 = fonk4(b5, b4, a2)
    a1 = 2
    while b10:
        b9[a1 - 1] = b10
        b10 = fonk3(b10, a1)
        b11 = fonk4(b10, b4, a2)
        b10 = b11
        a1 += 1
    for key, value in list(b9.items())[1:]:
        for item in value:
            b12 = map(frozenset, [x for x in fonk5(item)])
            for element in b12:
                b13 = item.difference(element)
                if b13:
                    b14 = b2[item] / b2[element]
                    if b14 >= a3:
                        print(f"{element} -> {b13} (Confidence: {b14:.2f})")
if b15 = = "__main__":
    a2 = 0.01
    a3 = 0.01
    b16 = 'T10I4D100k-copy.txt'
    fonk6(fonk1(b16), a2, a3)
    print("Time taken:", time.time() - b1)