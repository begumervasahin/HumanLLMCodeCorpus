25. Repository: aravindkanna/Implementation-of-Apriori-Algorithm
   File: otherMethods.py
   URL: https:
   Code Content:
from sets import Set
import itertools
def fonk1(currentSizeList):
	b1 = len(currentSizeList)
	a1 = 0
	a2 = 1
	print len(currentSizeList)
	b2 = []
	while a1 < b1:
		a2 = a1 + 1
		while a2 < b1:
			b3 = []
			if currentSizeList[a1][:-1] == currentSizeList[a2][:-1]:
				b3 = currentSizeList[a1][:]
				b3.append(currentSizeList[a2][-1])
				b2.append(b3)
				a2 += 1
			else :
				break
		a1 += 1
	print len(b2)
	return b2
def fonk2(itemset):
	b4 = []
	b1 = len(itemset)
	for a1 in range(b1):
		b5 = itemset[:a1] + itemset[a1+1:]
		b4.append(b5)
	return b4
def fonk3(FreqsTrie, currList):
	b6 = []
	for a1 in currList:
		b4 = fonk2(a1)
		b7 = True
		for a2 in b4:
			if not FreqsTrie.hasNode(a2):
				b7 = False
				break
		if b7:
			b6.append(a1)
	return b6
def fonk4(inFile, currList):
	b8 = open(inFile)
	b9 = []
	b1 = len(currList)
	for a1 in range(b1):
		b9.append(0)
	for b10 in b8:
		b10 = b10.strip()
		b11 = b10.split(",")
		b12 = Set(b11)
		b13 = len(b12)
		for a1 in range(b1):
			b3 = currList[a1][:]
			b14 = len(b3)
			if b13 < b14:
				continue
			b15 = Set(b3)
			if b12.issuperset(b15):
				b9[a1] += 1
	return b9
def fonk5(FreqsTrie, mincon):
	a3 = 0
	for a1 in FreqsTrie.getItemSets([]):
		for a2 in range(1, len(a1)):
			for k in itertools.combinations(a1, a2):
				if float(FreqsTrie.getCount(a1)) / float(FreqsTrie.getCount(k)) >= mincon:
					print (',').join(k) + "=>" + (',').join(set(a1) - set(k))
					a3 += 1
	return a3
   README Content:
This is the Implementation of Apriori Algorithm which is b3 famous Frequent Set Mining Algorithm.
