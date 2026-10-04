import sys
import csv
from collections import defaultdict
from itertools import chain, combinations
import time
start_time = time.time()
freqSet = defaultdict(int)
def data_gen(fname):
    with open(fname, 'r') as file:
        for line in file:
            line = line.strip().rstrip(',')
            record = frozenset(line.split(','))
            yield record
def transactions(data_iterator):
    transactionList = list()
    items = set()
    for record in data_iterator:
        transactionList.append(record)
        for item in record:
            items.add(frozenset([item]))
    return items, transactionList
def joinSet(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
def min_support(itemlist, transaction, min_supp):
    s = defaultdict(int)
    itemSet = set()
    for item in itemlist:
        for trans in transaction:
            if item.issubset(trans):
                s[item] += 1
    for item, count in s.items():
        support = float(count) / len(transaction)
        if support >= min_supp:
            itemSet.add(item)
            freqSet[item] = support
    return itemSet
def subsets(items):
    return chain(*[combinations(items, i + 1) for i, _ in enumerate(items)])
def run_apriori(data_iter, minSupport, minConfidence):
    itemSet, transactionList = transactions(data_iter)
    largeSet = dict()
    oneCSet = min_support(itemSet, transactionList, minSupport)
    currentLSet = oneCSet
    k = 2
    while currentLSet:
        largeSet[k - 1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = min_support(currentLSet, transactionList, minSupport)
        currentLSet = currentCSet
        k += 1
    for key, value in list(largeSet.items())[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = freqSet[item] / freqSet[element]
                    if confidence >= minConfidence:
                        print(f"{element} -> {remain} (Confidence: {confidence:.2f})")
if __name__ == "__main__":
    minSupport = 0.01
    minConfidence = 0.01
    inFile = data_gen('T10I4D100k-copy.txt')
    run_apriori(inFile, minSupport, minConfidence)
    print("Time taken:", time.time() - start_time)