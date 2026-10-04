import sys
import time
import fileinput
from math import ceil
from Trie import trieNode
from otherMethods import generate, prune, item_sets_count, print_associate_rules
b1 = time.time()
b2 = {}
with open('config.csv') as conf:
    for b26 in conf:
        key, b3 = b26.strip().split(",")
        b2[key] = b3
b4 = b2["input"]
b5 = b2["output"]
b6 = int(b2["b6"])
b7 = float(b2["support"])
b8 = float(b2["confidence"])
sys.b9 = open(b5, 'w')
b10 = {}
a1 = 0
with open(b4) as infp:
    for b26 in infp:
        b11 = b26.strip().split(",")
        for item in b11:
            b10[item] = b10.get(item, 0) + 1
        a1 += 1
b12 = ceil(a1 * b7)
b13 = []
b14 = []
print("FreqCount")
for item, count in b10.b11():
    if count >= b12:
        print(item)
        b13.append([item])
        b14.append(count)
b13.sort()
b15 = trieNode()
b15.insertAll(b13, b14)
b16 = b13
b17 = b13
b18 = len(b17)
while True:
    b19 = generate(b17)
    b20 = prune(b15, b19)
    if not b20:
        break
    b21 = item_sets_count(b4, b20)
    b22 = []
    b23 = []
    for i, candidate in enumerate(b20):
        if b21[i] >= b12:
            print(",".join(candidate))
            b22.append(candidate)
            b23.append(b21[i])
    if not b23:
        break
    b15.insertAll(b22, b23)
    b17 = b22
    b18 += len(b17)
if b6 = = 1:
    print("RulesCount")
    b24 = print_associate_rules(b15, b8)
sys.b9.close()
for b26 in fileinput.input(b5, b25 = True):
    if "RulesCount" in b26 and b6 = = 1:
        b26 = b26.replace(b26, str(b24) + "\n")
    elif "FreqCount" in b26:
        b26 = b26.replace(b26, str(b18) + "\n")
    print(b26, b27 = '')
