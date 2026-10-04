import time
from collections import defaultdict, Counter
import itertools
def predata(filename, minSup):
    items = defaultdict(set)
    itemset = set()
    frequent_items = set()
    total_item = []
    num_baskets = 0
    with open(filename, "r") as f:
        for line in f:
            num_baskets += 1
            basket = set(line.split())
            total_item += basket
            items[num_baskets] = basket
            itemset = itemset.union(basket)
    total = Counter(total_item)
    for item in itemset:
        num = total[item]
        if float(num) / num_baskets > minSup:
            frequent_items.add(item)
    return items, frequent_items
def gencandidate(frequent_items, k):
    candidate = set()
    if k == 2:
        for x in frequent_items:
            for y in frequent_items:
                if x != y:
                    candidate.add((x, y))
    else:
        for x in frequent_items:
            for y in frequent_items:
                if len(set(x).union(y)) == k:
                    candidate.add(tuple(set(x).union(y)))
        candidate = list(candidate)
        for c in candidate:
            subsets = getsubsets(c)
            if any(subset not in frequent_items for subset in subsets):
                candidate.remove(c)
    return set(candidate)
def getsubsets(candidate):
    subsets = list(itertools.combinations(candidate, len(candidate) - 1))
    return subsets
def genfreitems(candidate, items, minSup):
    frequent_items = set()
    with open('pres.txt', 'a') as pref:
        for c in candidate:
            count = sum(1 for k in items if set(c).issubset(items[k]))
            support = float(count) / len(items)
            if support > minSup:
                frequent_items.add(c)
                print(c)
                pref.write(str(c) + '\n')
    return frequent_items
def main():
    k = 4
    minSup = 0.08
    filename = "browsing.txt"
    items, frequent_items = predata(filename, minSup)
    for i in range(2, k + 1):
        candidate = gencandidate(frequent_items, i)
        frequent_items = genfreitems(candidate, items, minSup)
    return frequent_items
if __name__ == '__main__':
    main()