25. Repository: aravindkanna/Implementation-of-Apriori-Algorithm
   File: project.py
   URL: https:
   Code Content:
from Trie import *
from math import *
from otherMethods import *
import sys
import itertools
import sets
import fileinput
import time
b1 = time.time()
b2 = open('config.csv')
b3 = {}
for b30 in b2:
	b4 = b30.split(",")
	b4[1] = b4[1][:-1]
	b3[b4[0]] = b4[1]
b5 = b3["input"]
b6 = b3["output"]
b7 = int(b3["b7"])
b8 = float(b3["support"])
b9 = float(b3["confidence"])
sys.b10 = open(b6, 'w')
b11 = {}
b12 = 0;
b13 = open(b5)
for b4 in b13:
	b4 = b4.strip()
	b14 = b4.split(",")
	for i in b14:
		if i in b11:
			b11[i] = b11[i] + 1
		else:
			b11[i] = 1
	b12 += 1
b15 = []
b16 = []
print "FreqCount"
for i in b11:
	b17 = ceil(b12 * b8)
	if b11[i] >= b17:
		b4 = [i]
		print i
		b15.append(b4)
		b16.append(b11[i])
b15.sort()
b18 = trieNode()
b18.insertAll(b15, b16)
b19 = b15;
b20 = b15;
b21 = len(b20)
while True:
	b22 = generate(b20)
	b23 = prune(b18, b22)
	if len(b23) == 0:
		break
	b24 = itemSetsCount(b5, b23)
	b25 = []
	b26 = []
	b27 = len(b23)
	for i in range(b27):
		if b24[i] >= b17:
			print (",").join(b23[i])
			b25.append(b23[i])
			b26.append(b24[i])
	if len(b26) == 0:
		break
	b18.insertAll(b25, b26)
	b20 = b25
	b21 += len(b20)
if b7 = = 1:
	print "RulesCount"
	b28 = printAssociateRules(b18, b9)
sys.b10.close()
for b30 in fileinput.input(b6,b29 = 1):
    if "RulesCount" in b30 and b7 = = 1:
        b30 = b30.replace(b30,str(b28) + "\n")
    elif "FreqCount" in b30:
    	b30 = b30.replace(b30,str(b21) + "\n")
    print b30,
   README Content:
This is the Implementation of Apriori Algorithm which is b4 famous Frequent Set Mining Algorithm.
