from pyspark import SparkContext
from itertools import combinations
import sys
b1 = SparkContext(appName="Market_Basker_Analyzer")
a1 = 0.3
def fonk1(b6, length):
    b2 = []
    for i in range(len(b6)):
        for j in range(i + 1, len(b6)):
            if len(set(b6[i]).union(set(b6[j]))) == length:
                if tuple(set(b6[i]).union(set(b6[j]))) not in b2:
                    b2.append(tuple(set(b6[i]).union(set(b6[j]))))
    return b2
def fonk2(x):
    b3 = list(x)
    b4 = []
    b5 = a1 * len(b3)
    a2 = 0
    b6 = []
    for i in range(len(b3)):
        b6 = set(b6).union(set(b3[i]))
        if a2 < len(b3[i]):
            a2 = len(b3[i])
    b6 = list(b6)
    for i in range(len(b6)):
        a3 = 0
        for j in range(len(b3)):
            if b6[i] in set(b3[j]):
                a3 += 1
        if a3 >= b5:
            b4.append(b6[i])
    b7 = []
    b6 = list(combinations(list(b6), 2))
    for i in range(len(b6)):
        a3 = 0
        for j in range(len(b3)):
            if len(set(combinations(list(b6[i]), 2)).intersection(set(combinations(b3[j], 2)))) == 1:
                a3 += 1
        if a3 >= b5:
            b4.append(b6[i])
            b7.append(b6[i])
    b6 = b7
    b7 = []
    a4 = 3
    while a4 <= a2 and len(b6) > 1:
        b8 = fonk1(b6, a4)
        b6 = b8
        b7 = []
        for i in range(len(b6)):
            a3 = 0
            for j in range(len(b3)):
                if len(set(combinations(list(b6[i]), a4)).intersection(set(combinations(b3[j], a4)))) == 1:
                    a3 += 1
            if a3 >= b5:
                b7.append(b6[i])
                b4.append(b6[i])
        a4 += 1
        b6 = b7
    return b4
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b9>")
        sys.exit(1)
    b9 = sys.argv[1]
    b10 = b1.textFile(b9, 2)
    b8 = b10.map(lambda x: x.split("\n"))
    b11 = b8.mapPartition(partitionApriori)
    print(b8.collect())
    print(b8.getNumPartitions())
if b12 = = "__main__":
    fonk3()