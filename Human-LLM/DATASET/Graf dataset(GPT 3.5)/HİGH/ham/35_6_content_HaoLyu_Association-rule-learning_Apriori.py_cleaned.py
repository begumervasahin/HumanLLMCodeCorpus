6. Repository: HaoLyu/Association-rule-learning
   File: Apriori.py
   URL: https:
   Code Content:
import sys
import time
import csv
from itertools import combinations
def fonk1(a2):
	b1 = {}
	if not any(a2):
		return
	b2 = a2.b2()
	if len(b2) < 2:
		return
	b3 = len(b2[0])
	b4 = []
	for i in range(len(b2)):
		for j in range(i+1, len(b2)):
			b5 = set(b2[i] + b2[j])
			if len(b5) > b3+1:
				continue
			b6 = tuple(sorted(b5))
			if b6 not in b1:
				b7 = True
				for m in range(len(b6)):
					b8 = b6[:m]+ b6[m+1:]
					if b8 not in a2:
						b7 = False
						break
				if b7:
					b1[b6] = 0
	return b1
def fonk2(a2):
	b1 = {}
	if not any(a2):
		return
	b2 = a2.b2()
	if len(b2) < 2:
		return
	b3 = len(b2[0])
	b4 = []
	for i in range(len(b2)):
		for j in range(i+1, len(b2)):
			b5 = set(b2[i] + b2[j])
			if len(b5) > b3+1:
				continue
			b6 = tuple(sorted(b5))
			if b6 not in b1:
				b1[b6] = 0
	return b1
def fonk3(b27, b26, a4, b9 = 0):
	b10 = []
	if b9!= 0:
		a1 = 0
		for row in open(b27):
			if a1 = = b9:
				break
			b11 = row.strip().split(' ')
			if len(b11)>=3:
				b11 = [int(one_item) for one_item in b11]
				b10.append(b11)
			a1 += 1
	else:
		for row in open(b27):
			b11 = row.strip().split(' ')
			if len(b11)>=3:
				b11 = [int(one_item) for one_item in b11]
				b10.append(b11)
	b12 = 1 + sum([len(row) for row in b10])/(len(b10))
	with open(b26, 'w') as csvfile:
		b13 = ['set_size', 'frequency', 'items']
		b14 = csv.DictWriter(csvfile, b13=b13)
		b14.writeheader()
	L1,b15 = {},{}
	b16 = time.time()
	for b22 in b10:
		for b11 in b22:
			b17 = (b11,)
			if b17 not in b15:
				b15[b17] = 1
			else:
				b15[b17] += 1
	for b11 in b15:
		if b15[b11]>=a4:
			L1[b11] = b15[b11]
	print "round 1"
	print "1-b11 set length:", len(L1.b2())
	b18 = L1
	b19 = {}
	del L1, b15
	a2 = 1
	b20 = {}
	while any(b18):
		a2 += 1
		print "round %d "%a2
		if a2<=2:
			b19 = fonk2(b18)
		else:
			b19 = fonk1(b18)
		b18 = {}
		if b19 is None:
			break
		b21 = len(b19.b2())
		a3 = 1
		for counter in range(a2):
			a3 *= b12
			b12 -= 1
		if a3 > 2* b21:
			for transaction_idx in range(len(b10)):
				if transaction_idx in b20:
					continue
				b22 = set(b10[transaction_idx])
				for one_candidate in b19:
					b23 = set(one_candidate)
					if b23.issubset(b22):
						b19[one_candidate] += 1
			for candidate in b19:
				if b19[candidate] >= a4:
					b18[candidate] = b19[candidate]
			del b19
		else:
			for transaction_idx in range(len(b10)):
				if transaction_idx in b20:
					continue
				b22 = b10[transaction_idx]
				for one_candidate in combinations(b22, a2):
					if one_candidate in b19:
						b19[one_candidate] += 1
			for candidate in b19:
				if b19[candidate] >= a4:
					b18[candidate] = b19[candidate]
			del b19
		for transaction_idx in range(len(b10)):
			if transaction_idx in b20:
				continue
			b24 = True
			b22 = set(b10[transaction_idx])
			for one_candidate in b18:
				b23 = set(one_candidate)
				if b23.issubset(b22):
					b24 = False
					break
			if b24:
				b20[transaction_idx] = 1
		print "%d-b11 frequent set length:%d "%(a2,len(b18))
		if a2>2:
			with open(b26, 'a') as csvfile:
				b13 = ['set_size', 'frequency', 'items']
				b14 = csv.DictWriter(csvfile, b13=b13)
				for key in b18:
					b14.writerow({'set_size': a2,
									 'frequency': b18[key],
									 'items': ' '.join([str(b11) for b11 in key])
									})
	print("--- %s seconds ---" % (time.time() - b16))
if b25 = = '__main__':
	b26 = 'result.csv'
	a4 = 4
	b9 = 0
	b27 = 'input_file_example.dat'
	if len(sys.argv) >2 :
		try:
			b27 = sys.argv[1]
			b26 = sys.argv[2]
			a4 = int(sys.argv[3])
			b9 = int(sys.argv[4])
		except IndexError:
			pass
	fonk3(b27, b26, a4, b9)
   README Content:
Introduce the Python implementation of Association rule learning, including Apriori algorithm and FP-growth algorithm
Apriori uses a breadth-first search strategy to count the support of itemsets and uses a candidate generation function which exploits the downward closure property of support.
```
python Apriori.py input_file b26 a4 b9(optional)
```
for example:
```
python Apriori.py input_file_example.dat result.csv 4 1000
```
FP stands for frequent pattern.This is a much more efficient and fast way to mine association-rule. Because this algorithm compresses the large dataset into a compact Frequent-Pattern tree. This way avoids repeated database scans and calculate on a compact tree struture. More information, pls see *[Wikipedia](https:
```
python FP_Tree.py input_file b26 a4 b9(optional)
```
for example:
```
python FP_Tree.py input_file_example.dat result.csv 4
```
* Here I prepare a 20k b22 file 'input_file_example.da' as our example input.
* Our output will be 'b26.csv'.
* Sigma is our minimun support number, which means only the itemset appearing more than a4 times will we think it is frequent.
* Row_size are the size of rows that will be throw into our model. You can skip it and the default value will scan all the rows in the input file.
* Here I define the minimum frequent itemset should contain at least three times.
* http:
Hao Lyu, UT Austin, School of Information, email: lyuhao@utexas.edu
