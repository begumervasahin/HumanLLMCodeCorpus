from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
b1 = SparkContext(appName="Market-Basket-Analyzer")
a1 = 0.3
def fonk1(itemsets, length):
    b2 = []
    for i in range(len(itemsets)):
        for j in range(i + 1, len(itemsets)):
            b3 = set(itemsets[i]).union(set(itemsets[j]))
            if len(b3) == length and tuple(b3) not in b2:
                b2.append(tuple(b3))
    return b2
def fonk2(partition):
    b4 = list(partition)
    b5 = []
    b6 = a1 * len(b4)
    a2 = 0
    b7 = []
    for transaction in b4:
        b7 = list(set(b7).union(set(transaction)))
        a2 = max(a2, len(transaction))
    for item in b7:
        b8 = sum(1 for transaction in b4 if item in transaction)
        if b8 >= b6:
            b5.append(item)
    b2 = list(combinations(b7, 2))
    b9 = []
    for candidate in b2:
        b8 = sum(1 for transaction in b4 if set(candidate).issubset(set(transaction)))
        if b8 >= b6:
            b5.append(candidate)
            b9.append(candidate)
    a3 = 3
    while a3 <= a2 and len(b9) > 1:
        b2 = fonk1(b9, a3)
        b9 = []
        for candidate in b2:
            b8 = sum(1 for transaction in b4 if set(candidate).issubset(set(transaction)))
            if b8 >= b6:
                b5.append(candidate)
                b9.append(candidate)
        a3 += 1
    return b5
def fonk3():
    b10 = sys.argv[1]
    b11 = b1.textFile(b10, 2).map(lambda x: x.split(",")).mapPartitions(partition_apriori)
    b12 = b11.collect()
    print("Frequent itemsets:", b12)
    print("Number of partitions:", b11.getNumPartitions())
if b13 = = "__main__":
    fonk3()