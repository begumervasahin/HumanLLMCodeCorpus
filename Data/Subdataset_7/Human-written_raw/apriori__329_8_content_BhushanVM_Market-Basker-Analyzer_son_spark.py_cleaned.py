8. Repository: BhushanVM/Market-Basker-Analyzer
   File: son_spark.py
   URL: https:
   Code Content:
from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
b1 = SparkContext(appName="inf553")
a1 = 0.3
def fonk1(x):
    b2 = list(x[0])
    return b2
def fonk2(b7, length):
    b3 = []
    for i in xrange(0,len(b7)):
        for j in xrange(i+1,len(b7)):
            if(len(set(b7[i]).union(set(b7[j])))==length):
                if not b3.__contains__(tuple(set(b7[i]).union(set(b7[j])))):
                    b3.append(tuple(set(b7[i]).union(set(b7[j]))))
    return b3
def fonk3(x):
    b4 = list(x)
    b5 = []
    b6 = a1*len(b4)
    a2 = 0
    b7 = []
    for i in xrange(0, len(b4)):
        b7 = set(b7).union(set(b4[i]))
        if a2 < len(b4[i]):
            a2 = len(b4[i])
    b7 = list(b7)
    for i in xrange(0,len(b7)):
        a3 = 0
        for j in xrange(0,len(b4)):
            if set(b4[j]).__contains__(b7[i]):
                a3 += 1
        if a3 >= b6:
            b5.append(b7[i])
    b8 = []
    b7 = list(combinations(list(b7),2))
    for i in xrange(0,len(b7)):
        a3 = 0;
        for j in xrange(0, len(b4)):
            if len(set(combinations(list(b7[i]), 2)).intersection(set(combinations(b4[j], 2))))==1:
                a3 = a3+1
        if a3 >= b6:
            b5.append(b7[i])
            b8.append(b7[i])
    b7 = b8
    b8 = []
    a4 = 3
    while (a4 <= a2 and len(b7) > 1):
        b9 = fonk2(b7, a4)
        b7 = b9
        b8 = []
        print a4
        print b7
        for i in xrange(0, len(b7)):
            a3 = 0;
            for j in xrange(0, len(b4)):
                if len(set(combinations(list(b7[i]), a4)).intersection(set(combinations(b4[j], a4)))) == 1:
                    a3 = a3 + 1
            if a3 >= b6:
                b8.append(b7[i])
                b5.append(b7[i])
        a4 += 1
        b7 = b8
        print b7
    return b5
def fonk4():
	b10 = b1.textFile(sys.argv[1],2)
	b9 = b10.map(lambda x:x.split("\n"))
	b11 = b9.mapPartition(partitionApriori)
	print b9.collect()
	print b9.getNumPartitions()
if b12 = = "__main__":
	fonk4()
   README Content:
Apriori Algorithm using SON
