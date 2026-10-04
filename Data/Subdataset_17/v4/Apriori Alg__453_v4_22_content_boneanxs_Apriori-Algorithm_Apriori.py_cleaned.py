import itertools
def get_subsets(S):
    subset_length = len(S) - 1
    return [list(i) for i in itertools.combinations(S, subset_length)]
def is_subset_exist(tar, subsets):
    subset_sets = [set(subset) for subset in subsets]
    for transaction in tar:
        transaction_set = set(transaction)
        if all(subset <= transaction_set for subset in subset_sets):
            return 1
    return 0
def apriori(transactions, threshold, max_length):
    item_support = {}
    for items in transactions.values():
        for item in items:
            if item in item_support:
                item_support[item] += 1
            else:
                item_support[item] = 1
    transaction_count = len(transactions)
    frequent_items = {item: support / transaction_count for item, support in item_support.items() if support / transaction_count >= threshold}
    frequent_itemsets = [[item, support] for item, support in frequent_items.items()]
    if max_length == 1:
        return frequent_itemsets
    current_length = 2
    while current_length <= max_length:
        candidate_itemsets = []
        for i in range(len(frequent_itemsets)):
            for j in range(i + 1, len(frequent_itemsets)):
                candidate = list(set(frequent_itemsets[i][0]) | set(frequent_itemsets[j][0]))
                if len(candidate) != current_length:
                    continue
                candidate.sort()
                if is_subset_exist(frequent_itemsets, get_subsets(candidate)):
                    if candidate not in candidate_itemsets:
                        candidate_itemsets.append(candidate)
        frequent_itemsets = []
        for candidate in candidate_itemsets:
            support_count = sum(1 for items in transactions.values() if set(candidate) <= set(items))
            support = support_count / transaction_count
            if support >= threshold:
                frequent_itemsets.append([candidate, support])
        current_length += 1
    return frequent_itemsets
