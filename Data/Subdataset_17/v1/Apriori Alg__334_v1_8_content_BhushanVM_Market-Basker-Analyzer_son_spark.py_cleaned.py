from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
sc = SparkContext(appName="Market-Basket-Analyzer")
support_ratio = 0.3
def findCandidates(inp, length):
    candidate = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            union_set = set(inp[i]).union(set(inp[j]))
            if len(union_set) == length and tuple(union_set) not in candidate:
                candidate.append(tuple(union_set))
    return candidate
def partitionApriori(x):
    test = list(x)
    outputlist = []
    support = support_ratio * len(test)
    stop = 0
    inp = []
    for i in range(len(test)):
        inp = set(inp).union(set(test[i]))
        if stop < len(test[i]):
            stop = len(test[i])
    inp = list(inp)
    for i in range(len(inp)):
        count = sum(1 for j in range(len(test)) if inp[i] in test[j])
        if count >= support:
            outputlist.append(inp[i])
    temp_list = []
    inp = list(combinations(inp, 2))
    for i in range(len(inp)):
        count = sum(1 for j in range(len(test)) if set(combinations(inp[i], 2)).intersection(set(combinations(test[j], 2))))
        if count >= support:
            outputlist.append(inp[i])
            temp_list.append(inp[i])
    inp = temp_list
    temp_list = []
    l = 3
    while l <= stop and len(inp) > 1:
        output = findCandidates(inp, l)
        inp = output
        temp_list = []
        for i in range(len(inp)):
            count = sum(1 for j in range(len(test)) if set(combinations(inp[i], l)).intersection(set(combinations(test[j], l))))
            if count >= support:
                temp_list.append(inp[i])
                outputlist.append(inp[i])
        l += 1
        inp = temp_list
    return outputlist
def main():
    inpRDD = sc.textFile(sys.argv[1], 2)
    output = inpRDD.map(lambda x: x.split(",")).mapPartitions(partitionApriori)
    results = output.collect()
    print("Frequent itemsets:", results)
    print("Number of partitions:", output.getNumPartitions())
if __name__ == "__main__":
    main()