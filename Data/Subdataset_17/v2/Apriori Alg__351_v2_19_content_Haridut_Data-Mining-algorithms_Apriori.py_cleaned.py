
import itertools
from collections import defaultdict
def get_itemset_transaction_list(data):
    transaction_list = []
    item_set = set()
    for record in data:
        transaction = frozenset(record)
        transaction_list.append(transaction)
        for item in transaction:
            item_set.add(frozenset([item]))
    return item_set, transaction_list
def return_items_minsup(item_set, transaction_list, min_sup, freq_set):
    qualified_item_set = set()
    local_set = defaultdict(int)
    for item in item_set:
        for transaction in transaction_list:
            if item.issubset(transaction):
                freq_set[item] += 1
                local_set[item] += 1
    for item, count in local_set.items():
        if count >= min_sup:
            qualified_item_set.add(item)
    return qualified_item_set
def join_set(item_set, length):
    return set([i.union(j) for i in item_set for j in item_set if len(i.union(j)) == length])
def apriori(data, min_sup):
    item_set, transaction_list = get_itemset_transaction_list(data)
    freq_set = defaultdict(int)
    large_set = dict()
    one_c_set = return_items_minsup(item_set, transaction_list, min_sup, freq_set)
    current_l_set = one_c_set
    k = 2
    while current_l_set:
        large_set[k-1] = current_l_set
        current_l_set = join_set(current_l_set, k)
        current_c_set = return_items_minsup(current_l_set, transaction_list, min_sup, freq_set)
        current_l_set = current_c_set
        k += 1
    return large_set
def print_results(items, freq_set):
    for k, item_set in items.items():
        print(f"Frequent {k}-itemsets:")
        for item in item_set:
            print(f"{item}: {freq_set[item]}")
if __name__ == "__main__":
    data = [
        ['A', 'B', 'C'],
        ['A', 'C'],
        ['A', 'D', 'E'],
        ['B', 'C', 'E'],
        ['A', 'B', 'C', 'E'],
        ['B', 'E']
    ]
    min_sup = 2
    freq_set = defaultdict(int)
    large_set = apriori(data, min_sup)
    print_results(large_set, freq_set)