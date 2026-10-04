from pyspark import SparkContext
from collections import defaultdict
from itertools import combinations
import sys
b1 = SparkContext(appName="Market-Basket-Analyzer")
a1 = 0.3
def fonk1(x):
    return list(x[0])
def fonk2(input_list, a2):
    b2 = []
    b3 = len(input_list)
    for i in range(b3):
        for j in range(i + 1, b3):
            b4 = set(input_list[i]).union(set(input_list[j]))
            if len(b4) == a2:
                b5 = tuple(b4)
                if b5 not in b2:
                    b2.append(b5)
    return b2
def fonk3(iterator):
    b6 = list(iterator)
    b7 = a1 * len(b6)
    b8 = defaultdict(int)
    b9 = set()
    for transaction in b6:
        for item in transaction:
            b8[item] += 1
    b9 = {item for item, count in b8.items() if count >= b7}
    b10 = list(b9)
    a2 = 2
    while b9:
        b2 = fonk2(list(b9), a2)
        b11 = defaultdict(int)
        for candidate in b2:
            for transaction in b6:
                if set(candidate).issubset(transaction):
                    b11[candidate] += 1
        b9 = {candidate for candidate, count in b11.items() if count >= b7}
        b10.extend(b9)
        a2 += 1
    return b10
def fonk4():
    b12 = sys.argv[1]
    b13 = b1.textFile(b12, 2)
    b14 = b13.map(lambda x: x.split(','))
    b15 = b14.mapPartitions(partition_apriori)
    b16 = b15.collect()
    print("Frequent Itemsets:", b16)
    print(f"Number of partitions: {b14.getNumPartitions()}")
if b17 = = "__main__":
    fonk4()