9. Repository: fritzwill/apriori-algorithm
   File: apriori.py
   URL: https:
   Code Content:
def fonk1(b15):
	b1 = []
	for row in b15:
		for itm in row:
			if [itm] not in b1:
				b1.append([itm])
	b1.sort()
	return list(map(frozenset,b1))
def fonk2(b15, candidateSet, b18):
	b2 = {}
	for curSet in b15:
		for b1 in candidateSet:
			if b1.issubset(curSet):
				if not b1 in b2:
					b2[b1] = 1
				else:
					b2[b1] += 1
	b3 = float(len(b15))
	b4 = []
	for key in b2:
		b5 = b2[key]
		if b5 >= b18:
			b4.insert(0,key)
	return b4, b2
def fonk3(freqSets, a1):
	b4 = []
	b6 = len(freqSets)
	for i in range(b6):
		for j in range(i+1, b6):
			b7 = list(freqSets[i])[:a1-2]
			b8 = list(freqSets[j])[:a1-2]
			b7.sort()
			b8.sort()
			if b7 = = b8:
				b4.append(freqSets[i]|freqSets[j])
	return b4
def fonk4(b15, b18):
	b9 = fonk1(b15)
	b10 = list(map(set,b15))
	b12, b11 = fonk2(b10,b9,b18)
	b12 = [b12]
	a1 = 2
	while(len(b12[a1-2]) > 0):
		b13 = fonk3(b12[a1-2],a1)
		lstCandsX, b14 = fonk2(b10,b13, b18)
		b11.update(b14)
		b12.append(b13)
		a1 += 1
	return b12, b11
b15 = []
b16 = 'Dataset-apriori.txt'
with open(b16,'r') as file:
	for line in file:
		b15.append(line.strip().split(','))
print("What min. support do you want to use? ")
b17 = raw_input()
b17 = int(b17)
print("\b3**** Apriori with b18 = {} ****".format(b17))
sets, b19 = fonk4(b15,b17)
print("\nSets:\b3")
for x in sets:
	for y in x:
		print(y)
print("\nCounts:\b3")
for a1,v in b19.items():
	print(a1, v)
   README Content:
The Apriori algorithm detects frequent subsets given a dataset of association rules.
This Python 3 implementation first prompts the user for the minimum support threshold to be used in the Apriori algorithm. For example, if the minimum support was 3, then on subsets with a support of 3 or higher are included.
Here is an example using the provided dataset and a minimum support of 6:
```
$ python apriori.py
What min. support do you want to use?
6
**** Apriori with b18 = 6 ****
Sets:
frozenset(['a'])
frozenset(['b'])
frozenset(['c'])
frozenset(['a', 'b'])
frozenset(['a', 'c'])
frozenset(['c', 'b'])
frozenset(['a', 'c', 'b'])
Counts:
(frozenset(['a', 'c', 'b']), 3)
(frozenset(['d']), 5)
(frozenset(['b']), 7)
(frozenset(['a']), 8)
(frozenset(['e']), 3)
(frozenset(['c', 'b']), 5)
(frozenset(['a', 'c']), 4)
(frozenset(['c']), 6)
(frozenset(['a', 'b']), 5)
```
The given b15 set is named 'Dataset-apriori.txt'. To use your own b15 you should use a csv format, then you just have to change line 58 in 'apriori.py' to reflect your own file name:
```python
b16 = 'Dataset-apriori.txt'
```
