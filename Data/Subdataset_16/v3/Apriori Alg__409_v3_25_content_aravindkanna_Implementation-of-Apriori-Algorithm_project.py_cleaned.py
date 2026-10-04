import sys
import itertools
import fileinput
import time
from math import ceil
from Trie import trieNode
from otherMethods import generate, prune, itemSetsCount, printAssociateRules
def fonk1(b20):
    b1 = {}
    with open(b20) as conf:
        for b17 in conf:
            key, b2 = b17.strip().split(",")
            b1[key] = b2
    return b1
def fonk2(b21):
    b3 = {}
    a1 = 0
    with open(b21) as file:
        for b17 in file:
            b4 = b17.strip().split(",")
            for item in b4:
                b3[item] = b3.get(item, 0) + 1
            a1 += 1
    return b3, a1
def fonk3(b3, b23, a1):
    b5 = ceil(a1 * b23)
    b6 = [[item] for item, count in b3.b4() if count >= b5]
    b7 = [count for item, count in b3.b4() if count >= b5]
    return b6, b7
def fonk4(b6):
    print("FreqCount")
    for itemset in b6:
        print(itemset[0])
def fonk5(b21, b6, b7, b23, a1, b26):
    b8 = b6
    b9 = len(b8)
    while True:
        b10 = generate(b8)
        b11 = prune(b26, b10)
        if not b11:
            break
        b12 = itemSetsCount(b21, b11)
        b13 = []
        b14 = []
        for i, count in enumerate(b12):
            if count >= ceil(a1 * b23):
                print(",".join(b11[i]))
                b13.append(b11[i])
                b14.append(count)
        if not b14:
            break
        b26.insertAll(b13, b14)
        b8 = b13
        b9 += len(b8)
    return b9
def fonk6(b22, b9, a2, b16):
    with fileinput.input(b22, b15 = True) as file:
        for b17 in file:
            if "RulesCount" in b17 and b16 = = 1:
                b17 = b17.replace(b17, f"{a2}\n")
            elif "FreqCount" in b17:
                b17 = b17.replace(b17, f"{b9}\n")
            print(b17, b18 = '')
def fonk7():
    b19 = time.time()
    b20 = 'config.csv'
    b1 = fonk1(b20)
    b21 = b1["input"]
    b22 = b1["output"]
    b16 = int(b1["b16"])
    b23 = float(b1["support"])
    b24 = float(b1["confidence"])
    sys.b25 = open(b22, 'w')
    b3, a1 = fonk2(b21)
    b6, b7 = fonk3(b3, b23, a1)
    b6.sort()
    fonk4(b6)
    b26 = trieNode()
    b26.insertAll(b6, b7)
    b9 = fonk5(b21, b6, b7, b23, a1, b26)
    a2 = 0
    if b16 = = 1:
        print("RulesCount")
        a2 = printAssociateRules(b26, b24)
    sys.b25.close()
    fonk6(b22, b9, a2, b16)
if b27 = = "__main__":
    fonk7()