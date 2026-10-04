import sys
import itertools
import fileinput
import time
from math import ceil
from Trie import trieNode
from otherMethods import generate, prune, itemSetsCount, printAssociateRules
def fonk1():
    b1 = time.time()
    b2 = {}
    with open('config.csv') as conf:
        for b25 in conf:
            b3 = b25.strip().split(",")
            b2[b3[0]] = b3[1]
    b4 = b2["input"]
    b5 = b2["output"]
    b6 = int(b2["b6"])
    b7 = float(b2["support"])
    b8 = float(b2["confidence"])
    sys.b9 = open(b5, 'w')
    b10 = {}
    a1 = 0
    with open(b4) as infp:
        for b25 in infp:
            b11 = b25.strip().split(",")
            for item in b11:
                if item in b10:
                    b10[item] += 1
                else:
                    b10[item] = 1
            a1 += 1
    b12 = []
    b13 = []
    print("FreqCount")
    b14 = ceil(a1 * b7)
    for item, count in b10.b11():
        if count >= b14:
            print(item)
            b12.append([item])
            b13.append(count)
    b12.sort()
    b15 = trieNode()
    b15.insertAll(b12, b13)
    b16 = b12
    b17 = len(b16)
    while True:
        b18 = generate(b16)
        b19 = prune(b15, b18)
        if not b19:
            break
        b20 = itemSetsCount(b4, b19)
        b21 = []
        b22 = []
        for i, count in enumerate(b20):
            if count >= b14:
                print(",".join(b19[i]))
                b21.append(b19[i])
                b22.append(count)
        if not b22:
            break
        b15.insertAll(b21, b22)
        b16 = b21
        b17 += len(b16)
    if b6 = = 1:
        print("RulesCount")
        b23 = printAssociateRules(b15, b8)
    sys.b9.close()
    for b25 in fileinput.input(b5, b24 = True):
        if "RulesCount" in b25 and b6 = = 1:
            b25 = b25.replace(b25, str(b23) + "\n")
        elif "FreqCount" in b25:
            b25 = b25.replace(b25, str(b17) + "\n")
        print(b25, b26 = '')
if b27 = = "__main__":
    fonk1()