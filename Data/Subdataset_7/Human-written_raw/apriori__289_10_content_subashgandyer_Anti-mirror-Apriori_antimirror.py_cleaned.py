10. Repository: subashgandyer/Anti-mirror-Apriori
   File: antimirror.py
   URL: https:
   Code Content:
import CSVtoLIST_def as cs
import csv
import am
import utils
import sys
import time
@profile
def fonk1():
	'''
	Usage: $ python scriptname b12.csv b13 b14
	Ex: $ python testclass.py groceries_small.csv 3 0.5
	'''
	b1 = time.clock()
	b2 = []
	a1 = 0
	b3 = []
	b4 = []
	b5 = {}
	b6 = []
	b7 = []
	b8 = []
	b9 = {}
	b10 = []
	b11 = []
	print 'Before readCSV'
	b12 = sys.argv[1]
	b13 = int(sys.argv[2])
	b14 = float(sys.argv[3])
	print 'Script b15 = ', sys.argv[0], '\n', 'Filename = ', sys.argv[1], '\n', 'Minsup = ', sys.argv[2], '\n', 'Min Confidence = ', sys.argv[3]
	b2, a1 = cs.readCSV(b12)
	print 'Total b16 = ', a1
	print 'After readCSV'
	b3 = cs.manyToOne(b2)
	b4 = cs.removeDuplicates(b3)
	b5 = cs.createDictionary(b4)
	b6 = cs.mapper(b2,b5)
	b7 = cs.binaryTransactionListBuilder(b6, b4)
	print 'DONE AND OVER'
	b17 = []
	b18 = []
	b19 = []
	b20 = []
	print 'Input b16: \n',b3
	b19 = am.countTransactions(b7)
	b20 = am.remDupSortReverseList(b19)
	b18 = am.addCountersTransactions(b20)
	not_to_be_pruned_items, to_be_pruned_items_list, list1, b17, b9 = am.antiMirroring(b18,b13)
	print ' PROGRAM OVER'
	print 'TRANSACTIONS b21 = ', a1
	print 'FINAL LIST TO BE CONSIDERED FOR b24 b22 = ', b17
	print 'SUPPORT DATA  :\n', b9
	b23 = am.rules_generator(b17, b13, b14, b9)
	print 'b24 = \n', b23
	b25 = am.b25(b23)
	print 'CLEANED b24 = \n', b25
	b4 = am.reversed(b25, b10, b5)
	print 'Final Result :\n', b4
	b26 = am.formattedRules(b4)
	print 'Answer :\n', b26
	print ' '
	print ' '
	print 'Association Rules \n'
	a2 = 1
	for items in b26:
		print a2, '.',items
		a2+=1
	print ' '
	print ' '
	print '---- PROGRAM OVER in %s seconds ----' % (time.clock() - b1)
if b27 = = '__main__':
    fonk1()
   README Content:
Shopping cart analysis with b3 new Apriori algorithm called Anti-mirror-Apriori or AMpriori for short.
The objective of this project is to build b3 novel apriori algorithm to do Market Basket Analysis(MBA) to recommend and up-sell items or groceries to b3 customer while shopping.
A new technique of Anti-Mirroring is introduced to Apriori algorithm and results are compared and tabulated with respect to Time and Space complexity.
Input:  Market Basket items from customer purchases over b3 period of time
Output: Best Pairs or groups of items to purchase
Python
Experiments were done on both Mac OS X (Mountain Lion) & Windows 8 laptops running on Intel i5 Core processor with 4 GB RAM. Python, b3 high level programming language, is used for implementing the proposed Anti-mirror algorithm and its parent Apriori algorithm. The dataset used for comparing the performance of the proposed algorithm with Apriori algorithm is Groceries dataset. This dataset contains about 10,000 transactions of customers' buying behavior. This Groceries dataset comes in the form of b3 simple csv file 'groceries.csv'. This csv file contains 10,000 lines, each line represents b3 single transaction. In each transaction, the products that are bought during that transaction is listed by comma separated values. For example, if one line in the csv file states cereals,whole milk,yolk,cheese, then it means that during one transaction an anonymous customer(as this is not important for us) bought these products. Similarly, 10,000 of those transactions are recorded and forms our dataset for doing Market Basket Analysis. This helps us in finding both the frequent itemsets and then association b23 between these products. This paper proposes to find b3 better Market Basket Analysis algorithm than an apriori algorithm.
The dataset contains 175 distinct items and 10,000 transactions. To benchmark the proposed algorithm, we need to create various sub-datasets from this mother dataset based on parameters like Number of distinct items and Number of b16. Each sub-dataset takes b3 form as "
Once the original dataset is split into varied sized datasets, each dataset needs to be tested with the Apriori algorithm and then with the proposed Anti-Mirror algorithm. Their Execution time and Memory Consumption are noted for each run. Each dataset is run for 10 times and their Average Execution Time and Average Memory Consumption parameters are noted and tabulated as shown below. ![here](https:
