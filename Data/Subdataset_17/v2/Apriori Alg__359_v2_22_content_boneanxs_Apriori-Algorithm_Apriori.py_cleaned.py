import itertools
def get_subsets(S):
    subset_length = len(S) - 1
    return [list(subset) for subset in itertools.combinations(S, subset_length)]
def is_subset_exist(target_sets, subsets):
    target_sets = [set(item[0]) for item in target_sets]
    for subset in subsets:
        if not any(set(subset) < target_set for target_set in target_sets):
            return 0
    return 1
def apriori(transactions, threshold, max_length):
    item_frequency = {}
    for items in transactions.values():
        for item in items:
            item_frequency[item] = item_frequency.get(item, 0) + 1
    transaction_count = len(transactions)
    item_frequency = {item: freq / transaction_count for item, freq in item_frequency.items() if freq / transaction_count >= threshold}
    frequent_itemsets = [[item, support] for item, support in item_frequency.items()]
    if max_length == 1:
        return frequent_itemsets
    current_length = 2
    while current_length <= max_length:
        candidate_itemsets = []
        for i in range(len(frequent_itemsets)):
            for j in range(i + 1, len(frequent_itemsets)):
                if current_length == 2:
                    candidate = [frequent_itemsets[i][0], frequent_itemsets[j][0]]
                else:
                    candidate = list(set(frequent_itemsets[i][0]) | set(frequent_itemsets[j][0]))
                if len(candidate) != current_length:
                    continue
                candidate.sort()
                if is_subset_exist(frequent_itemsets, get_subsets(candidate)) and candidate not in candidate_itemsets:
                    candidate_itemsets.append(candidate)
        new_frequent_itemsets = []
        for candidate in candidate_itemsets:
            support = sum(1 for items in transactions.values() if set(candidate) <= set(items)) / transaction_count
            if support >= threshold:
                new_frequent_itemsets.append([candidate, support])
        frequent_itemsets = new_frequent_itemsets
        current_length += 1
    return frequent_itemsets
if __name__ == "__main__":
    transactions = {
        0: ['A', 'B', 'C'],
        1: ['A', 'C'],
        2: ['A', 'D'],
        3: ['B', 'C'],
        4: ['A', 'B', 'C', 'D']
    }
    threshold = 0.5
    max_length = 3
    frequent_itemsets = apriori(transactions, threshold, max_length)
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(f"Itemset: {itemset[0]}, Support: {itemset[1]:.2f}")