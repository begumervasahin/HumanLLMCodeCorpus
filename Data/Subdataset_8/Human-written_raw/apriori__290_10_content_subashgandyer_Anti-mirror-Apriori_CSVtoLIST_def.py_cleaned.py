10. Repository: subashgandyer/Anti-mirror-Apriori
   File: CSVtoLIST_def.py
   URL: https:
   Code Content:
import csv
import itertools
n_itemlist = []
a = []
result = []
Mapper_list =[]
Transaction_list = []
ReverseList = []
test_dict = {}
def readCSV(filename):
	reader = csv.reader(open(filename, "rb"), dialect="excel")
	count = 0
	for row in reader:
		n_itemlist.append(row)
		count += 1
	print "CREATED LIST ITEMS WITH DUPLICATES: \n", count, len(n_itemlist), n_itemlist
	return n_itemlist, count
def computeMinimumSupportCount(count):
	minsup = 0
	supcount = 0
	import math
	minsup = math.exp(-0.4*count - 0.2) + 0.2
	supcount = minsup * count / 100
	return minsup, supcount
def manyToOne(n_itemlist):
	for i in range(len(n_itemlist)):
		a.extend(n_itemlist[i])
	print "ONLY ONE LIST with duplicates: \n", len(a),a
	return a
def removeDuplicates(seq, idfun=None):
	if idfun is None:
	   def idfun(x): return x
	seen = {}
	for item in seq:
	   marker = idfun(item)
	   if marker in seen: continue
	   seen[marker] = 1
	   result.append(item)
	print "DUPLICATES REMOVED LIST :\n", len(result), result
	return result
def createDictionary(result):
	test_dict = dict(zip(result,range(1,len(result)+1)))
	print 'DICTIONARY = ',test_dict
	for key in sorted(test_dict.iterkeys()):
	    print "%s: %s" % (key, test_dict[key])
	return test_dict
def mapper(n_itemlist,test_dict):
	for i in range(len(n_itemlist)):
		tem_list = []
		for j in range(len(n_itemlist[i])):
			print n_itemlist[i][j]
			print test_dict[n_itemlist[i][j]]
			tem_list.append(test_dict[n_itemlist[i][j]])
		Mapper_list.append(tem_list)
	print "MAPPER LIST:\n",Mapper_list
	return Mapper_list
def binaryTransactionListBuilder(Mapper_list, result):
	for i in range(len(Mapper_list)):
		t_list = [0 for k in range(len(result))]
		for j in range(len(Mapper_list[i])):
			for k in range(len(result)):
				if Mapper_list[i][j] == k+1:
					t_list.pop(Mapper_list[i][j]-1)
					t_list.insert(Mapper_list[i][j]-1,1)
		Transaction_list.append(t_list)
	print "Transaction_list:\n",Transaction_list
	return Transaction_list
def reverseMapper(item, dict_list):
	mapper_key = 'Null'
	for itemset in dict_list:
		if item in itemset:
			mapper_key = itemset[0]
			break
	return mapper_key
   README Content:
Shopping cart analysis with a new Apriori algorithm called Anti-mirror-Apriori or AMpriori for short.
The objective of this project is to build a novel apriori algorithm to do Market Basket Analysis(MBA) to recommend and up-sell items or groceries to a customer while shopping.
A new technique of Anti-Mirroring is introduced to Apriori algorithm and results are compared and tabulated with respect to Time and Space complexity.
Input:  Market Basket items from customer purchases over a period of time
Output: Best Pairs or groups of items to purchase
Python
Experiments were done on both Mac OS X (Mountain Lion) & Windows 8 laptops running on Intel i5 Core processor with 4 GB RAM. Python, a high level programming language, is used for implementing the proposed Anti-mirror algorithm and its parent Apriori algorithm. The dataset used for comparing the performance of the proposed algorithm with Apriori algorithm is Groceries dataset. This dataset contains about 10,000 transactions of customers' buying behavior. This Groceries dataset comes in the form of a simple csv file 'groceries.csv'. This csv file contains 10,000 lines, each line represents a single transaction. In each transaction, the products that are bought during that transaction is listed by comma separated values. For example, if one line in the csv file states cereals,whole milk,yolk,cheese, then it means that during one transaction an anonymous customer(as this is not important for us) bought these products. Similarly, 10,000 of those transactions are recorded and forms our dataset for doing Market Basket Analysis. This helps us in finding both the frequent itemsets and then association rules between these products. This paper proposes to find a better Market Basket Analysis algorithm than an apriori algorithm.
The dataset contains 175 distinct items and 10,000 transactions. To benchmark the proposed algorithm, we need to create various sub-datasets from this mother dataset based on parameters like Number of distinct items and Number of Transactions. Each sub-dataset takes a form as "
Once the original dataset is split into varied sized datasets, each dataset needs to be tested with the Apriori algorithm and then with the proposed Anti-Mirror algorithm. Their Execution time and Memory Consumption are noted for each run. Each dataset is run for 10 times and their Average Execution Time and Average Memory Consumption parameters are noted and tabulated as shown below. ![here](https:
