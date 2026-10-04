
import itertools
from collections import defaultdict
def fonk1(b12):
    b1 = []
    b2 = set()
    for record in b12:
        b3 = frozenset(record)
        b1.append(b3)
        for item in b3:
            b2.add(frozenset([item]))
    return b2, b1
def fonk2(b2, b1, a2, b6):
    b4 = set()
    b5 = defaultdict(int)
    for item in b2:
        for trans in b1:
            if item.issubset(trans):
                b6[item] += 1
                b5[item] += 1
    for item, count in b5.items():
        if count >= a2:
            b4.add(item)
    return b4
def fonk3(b2, length):
    return set([i.union(j) for i in b2 for j in b2 if len(i.union(j)) == length])
def fonk4(b12, a2):
    b2, b1 = fonk1(b12)
    b6 = defaultdict(int)
    b7 = dict()
    b8 = fonk2(b2, b1, a2, b6)
    b9 = b8
    a1 = 2
    while b9 != set([]):
        b7[a1-1] = b9
        b9 = fonk3(b9, a1)
        b10 = fonk2(b9, b1, a2, b6)
        b9 = b10
        a1 += 1
    return b7
def fonk5(items):
    for a1, b2 in items.items():
        print(f"Frequent {a1}-itemsets:")
        for item in b2:
            print(f"{item}: {b6[item]}")
if b11 = = "__main__":
    b12 = [
        ['A', 'B', 'C'],
        ['A', 'C'],
        ['A', 'D', 'E'],
        ['B', 'C', 'E'],
        ['A', 'B', 'C', 'E'],
        ['B', 'E']
    ]
    a2 = 2
    b7 = fonk4(b12, a2)
    fonk5(b7)