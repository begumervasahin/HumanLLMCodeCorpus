import sys
import csv
import time
from collections import defaultdict
from itertools import chain, combinations
start_time = time.time()
freqSet = defaultdict(int)
def data_gen(fname):
    with open(fname, 'r') as file:
        for line in file:
            record = frozenset(line.strip().rstrip(',').split(','))
            yield record
def transactions(data_iterator):
    transaction_list = []
    item_set = set()
    for record in data_iterator:
        transaction_list.append(record)
        for item in record:
            item_set.add(frozenset([item]))
    return item_set, transaction_list
def join_set(item_set, length):
    return set([i.union(j) for i in item_set for j in item_set if len(i.union(j)) == length])
def min_support(item_list, transactions, min_supp):
    item_count = defaultdict(int)
    frequent_item_set = set()
    for item in item_list:
        for transaction in transactions:
            if item.issubset(transaction):
                item_count[item] += 1
    for item, count in item_count.items():
        support = float(count) / len(transactions)
        if support >= min_supp:
            frequent_item_set.add(item)
            freqSet[item] = support
    return frequent_item_set
def subsets(items):
    return chain(*[combinations(items, i + 1) for i, _ in enumerate(items)])
def run_apriori(data_iter, min_support, min_confidence):
    item_set, transaction_list = transactions(data_iter)
    large_set = {}
    current_l_set = min_support(item_set, transaction_list, min_support)
    k = 2
    while current_l_set:
        large_set[k - 1] = current_l_set
        current_l_set = join_set(current_l_set, k)
        current_c_set = min_support(current_l_set, transaction_list, min_support)
        current_l_set = current_c_set
        k += 1
    for key, value in list(large_set.items())[1:]:
        for item in value:
            item_subsets = map(frozenset, [x for x in subsets(item)])
            for element in item_subsets:
                remain = item.difference(element)
                if remain:
                    confidence = freqSet[item] / freqSet[element]
                    if confidence >= min_confidence:
                        print(f"{element} -> {remain} (Confidence: {confidence:.2f})")
if __name__ == "__main__":
    min_support = 0.01
    min_confidence = 0.01
    input_file = 'T10I4D100k-copy.txt'
    run_apriori(data_gen(input_file), min_support, min_confidence)
    print("Time taken:", time.time() - start_time)