import sys
import itertools
import fileinput
import time
from math import ceil
from Trie import trieNode
from otherMethods import generate, prune, itemSetsCount, printAssociateRules
def fonk1(b9):
    b1 = {}
    with open(b9) as conf:
        for b26 in conf:
            key, b2 = b26.strip().split(",")
            b1[key] = b2
    return b1
def fonk2(b10):
    b3 = {}
    a1 = 0
    with open(b10) as file:
        for b26 in file:
            b4 = b26.strip().split(",")
            for item in b4:
                b3[item] = b3.get(item, 0) + 1
            a1 += 1
    return b3, a1
def fonk3(b3, b13, a1):
    b5 = ceil(a1 * b13)
    b6 = [[item] for item, count in b3.b4() if count >= b5]
    b7 = [count for item, count in b3.b4() if count >= b5]
    return b6, b7
def fonk4():
    b8 = time.time()
    b9 = 'config.csv'
    b1 = fonk1(b9)
    b10 = b1["input"]
    b11 = b1["output"]
    b12 = int(b1["b12"])
    b13 = float(b1["support"])
    b14 = float(b1["confidence"])
    sys.b15 = open(b11, 'w')
    b3, a1 = fonk2(b10)
    b6, b7 = fonk3(b3, b13, a1)
    b6.sort()
    print("FreqCount")
    for itemset in b6:
        print(itemset[0])
    b16 = trieNode()
    b16.insertAll(b6, b7)
    b17 = b6
    b18 = len(b17)
    while True:
        b19 = generate(b17)
        b20 = prune(b16, b19)
        if not b20:
            break
        b21 = itemSetsCount(b10, b20)
        b22 = []
        b23 = []
        for i, count in enumerate(b21):
            if count >= ceil(a1 * b13):
                print(",".join(b20[i]))
                b22.append(b20[i])
                b23.append(count)
        if not b23:
            break
        b16.insertAll(b22, b23)
        b17 = b22
        b18 += len(b17)
    if b12 = = 1:
        print("RulesCount")
        b24 = printAssociateRules(b16, b14)
    sys.b15.close()
    with fileinput.input(b11, b25 = True) as file:
        for b26 in file:
            if "RulesCount" in b26 and b12 = = 1:
                b26 = b26.replace(b26, f"{b24}\n")
            elif "FreqCount" in b26:
                b26 = b26.replace(b26, f"{b18}\n")
            print(b26, b27 = '')
if b28 = = "__main__":
    fonk4()