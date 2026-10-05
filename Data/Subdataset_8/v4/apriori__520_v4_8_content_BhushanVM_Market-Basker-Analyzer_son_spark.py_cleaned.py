from pyspark import SparkContext
from itertools import combinations
import sys
sc = SparkContext(appName="Market_Basker_Analyzer")
support_ratio = 0.3
def findCandidates(inp, length):
    candidate = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if len(set(inp[i]).union(set(inp[j]))) == length:
                if tuple(set(inp[i]).union(set(inp[j]))) not in candidate:
                    candidate.append(tuple(set(inp[i]).union(set(inp[j]))))
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
        count = 0
        for j in range(len(test)):
            if inp[i] in set(test[j]):
                count += 1
        if count >= support:
            outputlist.append(inp[i])
    temp_list = []
    inp = list(combinations(list(inp), 2))
    for i in range(len(inp)):
        count = 0
        for j in range(len(test)):
            if len(set(combinations(list(inp[i]), 2)).intersection(set(combinations(test[j], 2)))) == 1:
                count += 1
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
            count = 0
            for j in range(len(test)):
                if len(set(combinations(list(inp[i]), l)).intersection(set(combinations(test[j], l)))) == 1:
                    count += 1
            if count >= support:
                temp_list.append(inp[i])
                outputlist.append(inp[i])
        l += 1
        inp = temp_list
    return outputlist
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    inpRDD = sc.textFile(input_file, 2)
    output = inpRDD.map(lambda x: x.split("\n"))
    getList = output.mapPartition(partitionApriori)
    print(output.collect())
    print(output.getNumPartitions())
if __name__ == "__main__":
    main()