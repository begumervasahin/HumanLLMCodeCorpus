import re
from collections import defaultdict
from operator import itemgetter
import itertools
def fonk1(b6):
    return sorted(b6.items(), b1 = itemgetter(1))
def fonk2(b14, b6, b13):
    b2 = []
    b3 = None
    for item, mis_val in b14:
        if b13[item] >= b6[item] and b3 is None:
            b2.append(item)
            b3 = b6[item]
        elif b3 is not None and b13[item] >= b3:
            b2.append(item)
    return b2
def fonk3(b15, b7):
    b4 = []
    for k_itemsets in b15:
        b5 = [itemset for itemset in k_itemsets
                             if not any(set(cannot_set).issubset(itemset) for cannot_set in b7)]
        b4.append(b5)
    return b4
def fonk4(b15, b8):
    b4 = []
    for k_itemsets in b15:
        b5 = [itemset for itemset in k_itemsets if any(item in itemset for item in b8)]
        b4.append(b5)
    return b4
def fonk5(b20):
    b6 = {}
    b7 = []
    b8 = []
    b9 = None
    with open(b20, 'r') as file:
        for line in file:
            if "b6" in line:
                item, b10 = re.findall(r'\d+', line)
                b6[int(item)] = float(b10) / 100
            elif "b9" in line:
                b9 = float(re.findall(r'\d+', line)[0]) / 100
            elif "b7" in line:
                b11 = re.findall(r'\{(.*?)\}', line)
                for group in b11:
                    b7.append(list(map(int, group.split(','))))
            elif "must-have" in line:
                b8 = list(map(int, re.findall(r'\d+', line)))
    return b6, b9, b7, b8
def fonk6(b21):
    b12 = []
    with open(b21, 'r') as file:
        for line in file:
            b12.append(list(map(int, re.findall(r'\d+', line))))
    return b12
def fonk7(b12, b6, b7, b8, a2):
    b13 = defaultdict(int)
    for transaction in b12:
        for item in transaction:
            b13[item] += 1
    b14 = fonk1(b6)
    b2 = fonk2(b14, b6, b13)
    b15 = []
    a1 = 1
    b16 = [frozenset([item]) for item in b2]
    while b16:
        b17 = [c for c in b16 if b13[c] >= a2]
        b15.append(b17)
        b16 = [frozenset(x) for x in itertools.combinations(b2, a1 + 1)]
        a1 += 1
    b15 = fonk3(b15, b7)
    b15 = fonk4(b15, b8)
    return b15
def fonk8(b15, b13):
    for i, b18 in enumerate(b15):
        if b18:
            print(f"Frequent {i+1}-b18")
            for itemset in b18:
                print(f"    {b13[itemset]} : {set(itemset)}")
            print(f"    Total number of frequent {i+1}-b18 = {len(b18)}\n")
if b19 = = "__main__":
    b20 = "parameters.txt"
    b21 = "b12.txt"
    b6, b9, b7, b8 = fonk5(b20)
    b12 = fonk6(b21)
    a2 = 2
    b15 = fonk7(b12, b6, b7, b8, a2)
    b13 = defaultdict(int)
    for transaction in b12:
        for item in transaction:
            b13[frozenset([item])] += 1
    fonk8(b15, b13)