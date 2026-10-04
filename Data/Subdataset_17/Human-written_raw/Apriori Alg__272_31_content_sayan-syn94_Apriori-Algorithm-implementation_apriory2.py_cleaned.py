31. Repository: sayan-syn94/Apriori-Algorithm-implementation
   File: apriory2.py
   URL: https:
   Code Content:
import sys
import csv
from collections import defaultdict
from itertools import chain, combinations
import time
s=time.time()
freqSet = defaultdict(int)
def data_gen(fname):
        file_iter = open(fname, 'rU')
        for line in file_iter:
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
def min_support(itemlist,transaction,m_supp):
    s=defaultdict(int)
    itemSet=set()
    for i in itemlist:
        for t in transaction:
            if i.issubset(t):
                s[i]+=1
    for i,v in s.items():
        support=float(v)/len(transaction)
        if support>=m_supp:
            itemSet.add(i)
            freqSet[i]=support
    return itemSet
def subsets(items):
    return chain(*[combinations(items, i + 1) for i, a in enumerate(items)])
def run_apriori(data_iter,minSupport,minConfidence):
    itemSet, transactionList = transactions(data_iter)
    l=len(transactionList)
    largeSet = dict()
    oneCSet = min_support(itemSet,transactionList,minSupport)
    currentLSet = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = min_support(currentLSet,transactionList,minSupport)
        print k
        print currentCSet
        currentLSet = currentCSet
        k = k + 1
    for key, value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = freqSet[item]/freqSet[element]
                    if confidence >= minConfidence:
                        print element,",",remain,"=>",confidence
if __name__ == "__main__":
    minSupport =0.01
    minConfidence = 0.01
    inFile=data_gen('T10I4D100k-copy.txt')
    run_apriori(inFile, minSupport, minConfidence)
    print (s-time.time())
   README Content:
My implementation of apriori algorithm
