from pyspark import SparkContext
from collections import defaultdict
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
    b5 = a1 * len(b4)
    b6 = set()
    a2 = 0
    for transaction in b4:
        b6.update(transaction)
        a2 = max(a2, len(transaction))
    b7 = defaultdict(int)
    for transaction in b4:
        for item in transaction:
            b7[item] += 1
    b8 = [
        item for item, count in b7.items() if count >= b5
    ]
    a3 = 2
    b9 = b8
    while a3 <= a2 and b9:
        b2 = fonk1(b9, a3)
        b10 = defaultdict(int)
        for candidate in b2:
            for transaction in b4:
                if set(candidate).issubset(transaction):
                    b10[candidate] += 1
        b9 = [
            candidate for candidate, count in b10.items() if count >= b5
        ]
        b8.extend(b9)
        a3 += 1
    return b8
def fonk3():
    b11 = sys.argv[1]
    b12 = b1.textFile(b11, 2).map(lambda x: x.split(",")).mapPartitions(partition_apriori)
    b13 = b12.collect()
    print("Frequent itemsets:", b13)
    print("Number of partitions:", b12.getNumPartitions())
if b14 = = "__main__":
    fonk3()