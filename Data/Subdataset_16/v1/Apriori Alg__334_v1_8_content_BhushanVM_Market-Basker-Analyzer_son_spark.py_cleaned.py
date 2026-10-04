from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
b1 = SparkContext(appName="Market-Basket-Analyzer")
a1 = 0.3
def fonk1(b7, length):
    b2 = []
    for i in range(len(b7)):
        for j in range(i + 1, len(b7)):
            b3 = set(b7[i]).union(set(b7[j]))
            if len(b3) == length and tuple(b3) not in b2:
                b2.append(tuple(b3))
    return b2
def fonk2(x):
    b4 = list(x)
    b5 = []
    b6 = a1 * len(b4)
    a2 = 0
    b7 = []
    for i in range(len(b4)):
        b7 = set(b7).union(set(b4[i]))
        if a2 < len(b4[i]):
            a2 = len(b4[i])
    b7 = list(b7)
    for i in range(len(b7)):
        b8 = sum(1 for j in range(len(b4)) if b7[i] in b4[j])
        if b8 >= b6:
            b5.append(b7[i])
    b9 = []
    b7 = list(combinations(b7, 2))
    for i in range(len(b7)):
        b8 = sum(1 for j in range(len(b4)) if set(combinations(b7[i], 2)).intersection(set(combinations(b4[j], 2))))
        if b8 >= b6:
            b5.append(b7[i])
            b9.append(b7[i])
    b7 = b9
    b9 = []
    a3 = 3
    while a3 <= a2 and len(b7) > 1:
        b10 = fonk1(b7, a3)
        b7 = b10
        b9 = []
        for i in range(len(b7)):
            b8 = sum(1 for j in range(len(b4)) if set(combinations(b7[i], a3)).intersection(set(combinations(b4[j], a3))))
            if b8 >= b6:
                b9.append(b7[i])
                b5.append(b7[i])
        a3 += 1
        b7 = b9
    return b5
def fonk3():
    b11 = b1.textFile(sys.argv[1], 2)
    b10 = b11.map(lambda x: x.split(",")).mapPartitions(partitionApriori)
    b12 = b10.collect()
    print("Frequent itemsets:", b12)
    print("Number of partitions:", b10.getNumPartitions())
if b13 = = "__main__":
    fonk3()