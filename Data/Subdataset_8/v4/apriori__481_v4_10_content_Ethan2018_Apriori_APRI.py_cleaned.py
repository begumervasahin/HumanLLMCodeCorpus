import time
from collections import defaultdict, Counter
import itertools
def preprocess_data(filename, min_support):
    items = defaultdict(set)
    itemset = set()
    frequent_items = set()
    total_items = []
    with open(filename, "r") as file:
        for line in file:
            basket_items = set(line.split())
            total_items += basket_items
            items[len(items) + 1] = basket_items
            itemset |= basket_items
    total = Counter(total_items)
    for item in itemset:
        if total[item] / len(items) > min_support:
            frequent_items.add(item)
    return items, frequent_items
def generate_candidate_itemsets(frequent_items, k):
    candidates = set()
    if k == 2:
        for x in frequent_items:
            for y in frequent_items:
                if x != y:
                    candidates.add((x, y))
    else:
        for x in frequent_items:
            for y in frequent_items:
                if len(set(x).union(y)) == k:
                    candidates.add(tuple(set(x).union(y)))
        candidates = list(candidates)
        for candidate in candidates:
            subsets = get_subsets(candidate)
            if any([x not in frequent_items for x in subsets]):
                candidates.remove(candidate)
    return set(candidates)
def get_subsets(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def generate_frequent_itemsets(candidate, items, min_support):
    frequent_items = set()
    count = 0
    with open('pres.txt', 'a') as pref:
        for c in candidate:
            for k in items:
                if set(c).issubset(items[k]):
                    count += 1
            support = float(count) / len(items)
            if support > min_support:
                frequent_items.add(c)
                print(c)
                pref.write(str(c))
    return frequent_items
def main():
    min_support = 0.08
    filename = "browsing.txt"
    k = 4
    items, frequent_items = preprocess_data(filename, min_support)
    for i in range(2, k + 1):
        candidate = generate_candidate_itemsets(frequent_items, i)
        frequent_items = generate_frequent_itemsets(candidate, items, min_support)
    return frequent_items
if __name__ == '__main__':
    main()