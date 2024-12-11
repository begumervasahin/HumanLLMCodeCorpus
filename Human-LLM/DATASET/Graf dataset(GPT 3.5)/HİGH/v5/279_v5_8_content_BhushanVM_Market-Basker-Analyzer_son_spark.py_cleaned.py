from pyspark import SparkContext
from itertools import combinations
import sys
b1 = SparkContext(appName="Market_Basker_Analyzer")
a1 = 0.3
def fonk1(inp, a3):
    b2 = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            b3 = set(inp[i]).union(set(inp[j]))
            if len(b3) == a3:
                if tuple(b3) not in b2:
                    b2.append(tuple(b3))
    return b2
def fonk2(x):
    b4 = list(x)
    b5 = []
    b6 = a1 * len(b4)
    a2 = 0
    b7 = set()
    for transaction in b4:
        b7 = b7.union(set(transaction))
        if a2 < len(transaction):
            a2 = len(transaction)
    b7 = list(b7)
    for item in b7:
        b8 = sum(1 for transaction in b4 if item in set(transaction))
        if b8 >= b6:
            b5.append(item)
    b9 = []
    b10 = list(combinations(b7, 2))
    for pair in b10:
        b8 = sum(1 for transaction in b4 if set(pair) in set(combinations(transaction, 2)))
        if b8 >= b6:
            b5.append(pair)
            b9.append(pair)
    b11 = b9
    b9 = []
    a3 = 3
    while a3 <= a2 and len(b11) > 1:
        b11 = fonk1(b11, a3)
        b9 = []
        for candidate in b11:
            b8 = sum(1 for transaction in b4 if set(candidate) in set(combinations(transaction, a3)))
            if b8 >= b6:
                b9.append(candidate)
                b5.append(candidate)
        a3 += 1
        b11 = b9
    return b5
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b12>")
        sys.exit(1)
    b12 = sys.argv[1]
    b13 = b1.textFile(b12, 2)
    b14 = b13.map(lambda x: x.split("\n"))
    b15 = b14.mapPartition(partition_apriori)
    print(b14.collect())
    print(b14.getNumPartitions())
if b16 = = "__main__":
    fonk3()