10. Repository: subashgandyer/Anti-mirror-Apriori
   File: CSVtoLIST_def.py
   URL: https:
   Code Content:
import csv
import itertools
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = {}
def fonk1(filename):
	b8 = csv.b8(open(filename, "rb"), dialect="excel")
	a1 = 0
	for row in b8:
		b1.append(row)
		a1 += 1
	print "CREATED LIST ITEMS WITH DUPLICATES: \n", a1, len(b1), b1
	return b1, a1
def fonk2(a1):
	a2 = 0
	a3 = 0
	import math
	a2 = math.exp(-0.4*a1 - 0.2) + 0.2
	a3 = a2 * a1 / 100
	return a2, a3
def fonk3(b1):
	for i in range(len(b1)):
		b2.extend(b1[i])
	print "ONLY ONE LIST with duplicates: \n", len(b2),b2
	return b2
def fonk4(seq, b9 = None):
	if b9 is None:
	   def fonk5(x): return x
	b10 = {}
	for item in seq:
	   b11 = fonk5(item)
	   if b11 in b10: continue
	   b10[b11] = 1
	   b3.append(item)
	print "DUPLICATES REMOVED LIST :\n", len(b3), b3
	return b3
def fonk6(b3):
	b7 = dict(zip(b3,range(1,len(b3)+1)))
	print 'b12 = ',b7
	for key in sorted(b7.iterkeys()):
	    print "%s: %s" % (key, b7[key])
	return b7
def fonk7(b1,b7):
	for i in range(len(b1)):
		b13 = []
		for j in range(len(b1[i])):
			print b1[i][j]
			print b7[b1[i][j]]
			b13.append(b7[b1[i][j]])
		b4.append(b13)
	print "MAPPER LIST:\n",b4
	return b4
def fonk8(b4, b3):
	for i in range(len(b4)):
		b14 = [0 for k in range(len(b3))]
		for j in range(len(b4[i])):
			for k in range(len(b3)):
				if b4[i][j] == k+1:
					b14.pop(b4[i][j]-1)
					b14.insert(b4[i][j]-1,1)
		b5.append(b14)
	print "b5:\n",b5
	return b5
def fonk9(item, dict_list):
	b15 = 'Null'
	for itemset in dict_list:
		if item in itemset:
			b15 = itemset[0]
			break
	return b15
   README Content:
Shopping cart analysis with b2 new Apriori algorithm called Anti-mirror-Apriori or AMpriori for short.
The objective of this project is to build b2 novel apriori algorithm to do Market Basket Analysis(MBA) to recommend and up-sell items or groceries to b2 customer while shopping.
A new technique of Anti-Mirroring is introduced to Apriori algorithm and results are compared and tabulated with respect to Time and Space complexity.
Input:  Market Basket items from customer purchases over b2 period of time
Output: Best Pairs or groups of items to purchase
Python
Experiments were done on both Mac OS X (Mountain Lion) & Windows 8 laptops running on Intel i5 Core processor with 4 GB RAM. Python, b2 high level programming language, is used for implementing the proposed Anti-mirror algorithm and its parent Apriori algorithm. The dataset used for comparing the performance of the proposed algorithm with Apriori algorithm is Groceries dataset. This dataset contains about 10,000 transactions of customers' buying behavior. This Groceries dataset comes in the form of b2 simple csv file 'groceries.csv'. This csv file contains 10,000 lines, each line represents b2 single transaction. In each transaction, the products that are bought during that transaction is listed by comma separated values. For example, if one line in the csv file states cereals,whole milk,yolk,cheese, then it means that during one transaction an anonymous customer(as this is not important for us) bought these products. Similarly, 10,000 of those transactions are recorded and forms our dataset for doing Market Basket Analysis. This helps us in finding both the frequent itemsets and then association rules between these products. This paper proposes to find b2 better Market Basket Analysis algorithm than an apriori algorithm.
The dataset contains 175 distinct items and 10,000 transactions. To benchmark the proposed algorithm, we need to create various sub-datasets from this mother dataset based on parameters like Number of distinct items and Number of Transactions. Each sub-dataset takes b2 form as "
Once the original dataset is split into varied sized datasets, each dataset needs to be tested with the Apriori algorithm and then with the proposed Anti-Mirror algorithm. Their Execution time and Memory Consumption are noted for each run. Each dataset is run for 10 times and their Average Execution Time and Average Memory Consumption parameters are noted and tabulated as shown below. ![here](https:
