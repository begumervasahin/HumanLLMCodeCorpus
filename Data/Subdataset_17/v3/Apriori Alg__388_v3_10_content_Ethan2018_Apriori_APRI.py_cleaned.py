import time
from collections import defaultdict, Counter
import itertools
def predata(filename, minSup):
    items = defaultdict(set)
    total_item = []
    num_baskets = 0
    with open(filename, "r") as f:
        for line in f:
            num_baskets += 1
            basket = set(line.split())
            total_item += basket
            items[num_baskets] = basket
    itemset = set(total_item)
    total_counts = Counter(total_item)
    frequent_items = {item for item in itemset if float(total_counts[item]) / num_baskets > minSup}
    return items, frequent_items
def gencandidate(frequent_items, k):
    if k == 2:
        return {(x, y) for x in frequent_items for y in frequent_items if x != y}
    candidates = {tuple(set(x).union(y)) for x in frequent_items for y in frequent_items if len(set(x).union(y)) == k}
    return {c for c in candidates if all(subset in frequent_items for subset in getsubsets(c))}
def getsubsets(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def genfreitems(candidate, items, minSup):
    frequent_items = set()
    total_baskets = len(items)
    with open('pres.txt', 'a') as pref:
        for c in candidate:
            count = sum(1 for basket in items.values() if set(c).issubset(basket))
            support = float(count) / total_baskets
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