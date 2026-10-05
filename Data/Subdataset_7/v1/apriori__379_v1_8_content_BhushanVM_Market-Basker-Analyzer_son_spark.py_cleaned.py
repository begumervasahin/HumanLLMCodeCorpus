from pyspark import SparkContext
from itertools import combinations
import sys
b1 = SparkContext(appName="Market_Basker_Analyzer")
a1 = 0.3
def fonk1(transaction):
    return transaction.split()
def fonk2(itemset, a3):
    b2 = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            b3 = set(itemset[i]).union(itemset[j])
            if len(b3) == a3:
                if b3 not in b2:
                    b2.append(b3)
    return b2
def fonk3(transactions, candidate):
    a2 = 0
    for transaction in transactions:
        if candidate.issubset(set(transaction)):
            a2 += 1
    return a2
def fonk4(itemsets, support):
    b4 = []
    for itemset in itemsets:
        if itemset[1] >= support:
            b4.append(itemset[0])
    return b4
def fonk5(transactions, support):
    b2 = []
    for transaction in transactions:
        for item in transaction:
            if [item] not in b2:
                b2.append([item])
    b2.sort()
    a3 = 2
    while True:
        b5 = fonk2(b2, a3)
        b6 = []
        for candidate in b5:
            a2 = fonk3(transactions, set(candidate))
            b6.append((candidate, a2))
        b7 = fonk4(b6, support)
        if not b7:
            break
        b2 = b7
        a3 += 1
    return b2
def fonk6():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b8>")
        sys.exit(1)
    b8 = sys.argv[1]
    b9 = b1.textFile(b8)
    b10 = b9.map(extract_items)
    b4 = b10.mapPartitions(lambda x: fonk5(list(x), a1 * x.getNumPartitions()))
    b11 = b4.collect()
    print("Frequent Itemsets:")
    for itemset in b11:
        print(itemset)
if b12 = = "__main__":
    fonk6()