import itertools
from collections import defaultdict, Counter
def preprocess_data(filename, min_support):
    baskets = defaultdict(set)
    frequent_items = set()
    total_items = []
    with open(filename, "r") as file:
        for line in file:
            basket_items = set(line.split())
            total_items += basket_items
            baskets[len(baskets) + 1] = basket_items
            frequent_items |= basket_items
    item_counts = Counter(total_items)
    frequent_items = {item for item in frequent_items if item_counts[item] / len(baskets) > min_support}
    return baskets, frequent_items
def generate_candidate_itemsets(frequent_items, size):
    candidates = set()
    if size == 2:
        candidates = {(x, y) for x in frequent_items for y in frequent_items if x != y}
    else:
        for x in frequent_items:
            for y in frequent_items:
                if len(set(x).union(y)) == size:
                    candidates.add(tuple(set(x).union(y)))
        for candidate in list(candidates):
            subsets = get_subsets(candidate)
            if any(subset not in frequent_items for subset in subsets):
                candidates.remove(candidate)
    return candidates
def get_subsets(candidate):
    return list(itertools.combinations(candidate, len(candidate) - 1))
def generate_frequent_itemsets(candidates, baskets, min_support):
    frequent_itemsets = set()
    with open('pres.txt', 'a') as pref:
        for candidate in candidates:
            count = sum(1 for basket in baskets.values() if set(candidate).issubset(basket))
            support = count / len(baskets)
            if support > min_support:
                frequent_itemsets.add(candidate)
                print(candidate)
                pref.write(str(candidate))
    return frequent_itemsets
def main():
    min_support = 0.08
    filename = "browsing.txt"
    k = 4
    baskets, frequent_items = preprocess_data(filename, min_support)
    for size in range(2, k + 1):
        candidates = generate_candidate_itemsets(frequent_items, size)
        frequent_items = generate_frequent_itemsets(candidates, baskets, min_support)
    return frequent_items
if __name__ == '__main__':
    main()