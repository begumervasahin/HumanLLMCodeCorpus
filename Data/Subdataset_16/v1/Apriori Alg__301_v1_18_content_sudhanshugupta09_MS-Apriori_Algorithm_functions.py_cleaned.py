import re
from collections import defaultdict
from operator import itemgetter
def fonk1(b6):
    return sorted(b6.items(), b1 = itemgetter(1))
def fonk2(b6):
    return list(b6.keys())
def fonk3(b15, b16, b6, b14):
    b2 = True
    b3 = None
    for i, mis_val in b15:
        if b14[i] >= b6[i] and b2:
            b16.append(i)
            b3 = b6[i]
            b2 = False
        elif not b2 and b14[i] >= b3:
            b16.append(i)
def fonk4(b17, b7):
    b4 = [[], [], [], [], []]
    a1 = 0
    for f in b17:
        if len(f) > 0:
            for s in f:
                if a1 > 0:
                    for c in b7:
                        if set(c).issubset(s):
                            pass
                        else:
                            b4[a1].append(s)
                else:
                    b4[a1].append(s)
            a1 += 1
    return b4
def fonk5(b17, b8):
    b5 = [[], [], [], [], []]
    a1 = 0
    for f in b17:
        if len(f) > 0:
            b4 = set()
            for s in f:
                for must in b8:
                    if a1 > 1:
                        if must in s:
                            b4.add(s)
                            continue
                    else:
                        if s in b8:
                            b4.add(s)
            b5[a1 - 1].extend(list(b4))
        a1 += 1
    return b5
def fonk6(b22):
    b6 = {}
    b7 = []
    b8 = []
    b9 = None
    with open(b22, 'r') as file:
        b10 = file.readlines()
        for line in b10:
            if "b6" in line:
                item, b11 = re.findall(r'\d+', line)
                b6[int(item)] = float(b11) / 100
            elif "b9" in line:
                b9 = float(re.findall(r'\d+', line)[0]) / 100
            elif "b7" in line:
                b12 = re.findall(r'\{(.*?)\}', line)
                for group in b12:
                    b7.append(list(map(int, group.split(','))))
            elif "must-have" in line:
                b8 = list(map(int, re.findall(r'\d+', line)))
    return b6, b9, b7, b8
def fonk7(b23):
    b13 = []
    with open(b23, 'r') as file:
        b10 = file.readlines()
        for line in b10:
            b13.append(list(map(int, re.findall(r'\d+', line))))
    return b13
def fonk8(b13, b6, b7, b8, a3):
    b14 = defaultdict(int)
    for transaction in b13:
        for item in transaction:
            b14[item] += 1
    b15 = fonk1(b6)
    b16 = []
    fonk3(b15, b16, b6, b14)
    b17 = []
    a2 = 1
    b18 = [frozenset([item]) for item in b16]
    while b18:
        b19 = []
        for c in b18:
            if b14[c] >= a3:
                b19.append(c)
        b17.append(b19)
        b18 = [frozenset(x) for x in itertools.combinations(b16, a2 + 1)]
        a2 += 1
    b17 = fonk4(b17, b7)
    b17 = fonk5(b17, b8)
    return b17
def fonk9(b17):
    for i, b20 in enumerate(b17):
        if b20:
            print(f"Frequent {i+1}-b20")
            for itemset in b20:
                print(f"    {b14[itemset]} : {set(itemset)}")
            print(f"    Total number of frequent {i+1}-b20 = {len(b20)}\n")
if b21 = = "__main__":
    b22 = "parameters.txt"
    b23 = "b13.txt"
    b6, b9, b7, b8 = fonk6(b22)
    b13 = fonk7(b23)
    a3 = 2
    b17 = fonk8(b13, b6, b7, b8, a3)
    fonk9(b17)