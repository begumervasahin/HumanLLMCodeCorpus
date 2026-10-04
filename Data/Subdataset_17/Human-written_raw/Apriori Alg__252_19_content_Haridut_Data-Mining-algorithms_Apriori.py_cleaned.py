19. Repository: Haridut/Data-Mining-algorithms
   File: Apriori.py
   URL: https:
   Code Content:
import itertools
'''lines=sys.stdin.readlines()
a=[]
for i in lines:
    a.append(i.rstrip('\n'))
min_sup = int(a[0])
data=[]
for trans in a[1:]:
    data.append(trans)'''
def getItemSetTransactionList(data):
    transactionList=[]
    itemSet=set()
    for record in data:
        transaction=frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))
    return itemSet, transactionList
def return_items_minsup(itemSet, transactionList,min_sup,freqSet):
    item_set=set()
    localSet=defaultdict(int)
    for item in itemSet:
        for trans in transactionList:
            if item.issubset(trans):
                freqSet[item]+=1
                localSet[item]+=1
    for item, count in localSet.items():
        if count>=min_sup:
            item_set.add(item)
    return item_set
def joinSet(itemSet, length):
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
def Apriori(data,min_sup):
    itemSet, TransactionList = getItemSetTransactionList(data)
    freqSet = defaultdict(int)
    largeSet = dict()
    oneCSet=return_items_minsup(itemSet,transactionList,min_sup, freqSet)
    currentLset=oneCset
    k=2
    while (currentLSet != set([])):
        largeSet[k-1]=currentLset
        currentLSet=joinSet(currentLSet, k)
        currentCset=return_items_minsup(currentLset, transactionList, min_sup, freqSet)
        currentLset=currentCset
        k=k+1
   README Content:
This repository contains codes for Apriori algorithm, online query computation using shell-fragments.
