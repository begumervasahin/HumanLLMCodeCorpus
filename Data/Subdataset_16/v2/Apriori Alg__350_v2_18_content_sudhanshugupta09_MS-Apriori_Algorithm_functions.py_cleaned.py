import re
from collections import defaultdict
from operator import itemgetter
import itertools
def fonk1(b6):
    return sorted(b6.items(), b1 = itemgetter(1))
def fonk2(b6):
    return list(b6.keys())
def fonk3(b14, b15, b6, b13):
    b2 = True
    b3 = None
    for item, mis_val in b14:
        if b13[item] >= b6[item] and b2:
            b15.append(item)
            b3 = b6[item]
            b2 = False
        elif not b2 and b13[item] >= b3:
            b15.append(item)
def fonk4(b16, b7):
    b4 = []
    for k_itemsets in b16:
        b5 = []
        for itemset in k_itemsets:
            if not any(set(cannot_set).issubset(itemset) for cannot_set in b7):
                b5.append(itemset)
        b4.append(b5)
    return b4
def fonk5(b16, b8):
    b4 = []
    for k_itemsets in b16:
        b5 = []
        for itemset in k_itemsets:
            if any(item in itemset for item in b8):
                b5.append(itemset)
        b4.append(b5)
    return b4
def fonk6(b21):
    b6 = {}
    b7 = []
    b8 = []
    b9 = None
    with open(b21, 'r') as file:
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
def fonk7(b22):
    b12 = []
    with open(b22, 'r') as file:
        for line in file:
            b12.append(list(map(int, re.findall(r'\d+', line))))
    return b12
def fonk8(b12, b6, b7, b8, a2):
    b13 = defaultdict(int)
    for transaction in b12:
        for item in transaction:
            b13[item] += 1
    b14 = fonk1(b6)
    b15 = []
    fonk3(b14, b15, b6, b13)
    b16 = []
    a1 = 1
    b17 = [frozenset([item]) for item in b15]
    while b17:
        b18 = [c for c in b17 if b13[c] >= a2]
        b16.append(b18)
        b17 = [frozenset(x) for x in itertools.combinations(b15, a1 + 1)]
        a1 += 1
    b16 = fonk4(b16, b7)
    b16 = fonk5(b16, b8)
    return b16
def fonk9(b16, b13):
    for i, b19 in enumerate(b16):
        if b19:
            print(f"Frequent {i+1}-b19")
            for itemset in b19:
                print(f"    {b13[itemset]} : {set(itemset)}")
            print(f"    Total number of frequent {i+1}-b19 = {len(b19)}\n")
if b20 = = "__main__":
    b21 = "parameters.txt"
    b22 = "b12.txt"
    b6, b9, b7, b8 = fonk6(b21)
    b12 = fonk7(b22)
    a2 = 2
    b16 = fonk8(b12, b6, b7, b8, a2)
    b13 = defaultdict(int)
    for transaction in b12:
        for item in transaction:
            b13[frozenset([item])] += 1
    fonk9(b16, b13)