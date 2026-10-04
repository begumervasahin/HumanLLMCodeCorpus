import time
from collections import defaultdict, Counter
import itertools
def predata(filename, minSup):
    items = defaultdict(set)
    itemset = set()
    freitems = set()
    total_item = []
    num_basket = 0
    with open(filename, "r") as f:
        for line in f:
            num_basket += 1
            basket = set(line.split())
            total_item += basket
            items[num_basket] = basket
            itemset = itemset.union(basket)
    total = Counter(total_item)
    for item in itemset:
        num = total[item]
        if float(num) / num_basket > minSup:
            freitems.add(item)
    return items, freitems
def gencandidate(freitems, k):
    candidate = set()
    if k == 2:
        for x in freitems:
            for y in freitems:
                if x != y:
                    candidate.add((x, y))
    else:
        for x in freitems:
            for y in freitems:
                if len(set(x).union(y)) == k:
                    candidate.add(tuple(set(x).union(y)))
        candidate = list(candidate)
        for c in candidate:
            subsets = getsubsets(c)
            if any([x not in freitems for x in subsets]):
                candidate.remove(c)
    return set(candidate)
def getsubsets(candidate):
    subsets = list(itertools.combinations(candidate, len(candidate) - 1))
    return subsets
def genfreitems(candidate, items, minSup):
    freitems = set()
    pref = open('pres.txt', 'a')
    for c in candidate:
        count = sum(1 for k in items if set(c).issubset(items[k]))
        sup = float(count) / len(items)
        if sup > minSup:
            freitems.add(c)
            print(c)
            pref.write(str(c) + '\n')
    pref.close()
    return freitems
def main():
    k = 4
    minSup = 0.08
    filename = "browsing.txt"
    candidate = set()
    freitems = set()
    items, freitems = predata(filename, minSup)
    for i in range(2, k + 1):
        candidate = gencandidate(freitems, i)
        freitems = genfreitems(candidate, items, minSup)
    return freitems
if __name__ == '__main__':
    main()