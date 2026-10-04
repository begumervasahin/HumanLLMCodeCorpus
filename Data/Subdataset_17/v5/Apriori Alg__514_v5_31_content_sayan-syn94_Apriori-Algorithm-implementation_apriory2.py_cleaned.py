import sys
import csv
import time
from collections import defaultdict
from itertools import chain, combinations
def data_gen(fname):
    with open(fname, 'r') as file_iter:
        for line in file_iter:
            line = line.strip().rstrip(',')
            record = frozenset(line.split(','))
            yield record
def transactions(data_iterator):
    transaction_list = []
    items = set()
    for record in data_iterator:
        transaction_list.append(record)
        for item in record:
            items.add(frozenset([item]))
    return items, transaction_list
def join_set(item_set, length):
    return set([i.union(j) for i in item_set for j in item_set if len(i.union(j)) == length])
def filter_by_support(item_list, transaction_list, min_support):
    item_count = defaultdict(int)
    frequent_item_set = set()
    for item in item_list:
        for transaction in transaction_list:
            if item.issubset(transaction):
                item_count[item] += 1
    for item, count in item_count.items():
        support = float(count) / len(transaction_list)
        if support >= min_support:
            frequent_item_set.add(item)
            freq_set[item] = support
    return frequent_item_set
def get_subsets(items):
    return chain(*[combinations(items, i + 1) for i in range(len(items))])
def run_apriori(data_iter, min_support, min_confidence):
    item_set, transaction_list = transactions(data_iter)
    large_set = {}
    one_c_set = filter_by_support(item_set, transaction_list, min_support)
    current_l_set = one_c_set
    k = 2
    while current_l_set:
        large_set[k - 1] = current_l_set
        current_l_set = join_set(current_l_set, k)
        current_c_set = filter_by_support(current_l_set, transaction_list, min_support)
        current_l_set = current_c_set
        k += 1
    for key, value in list(large_set.items())[1:]:
        for item in value:
            subsets = map(frozenset, [x for x in get_subsets(item)])
            for element in subsets:
                remain = item.difference(element)
                if remain:
                    confidence = freq_set[item] / freq_set[element]
                    if confidence >= min_confidence:
                        print(f"{element} -> {remain} (Confidence: {confidence:.2f})")
if __name__ == "__main__":
    start_time = time.time()
    min_support = 0.01
    min_confidence = 0.01
    input_file = 'T10I4D100k-copy.txt'
    data_iterator = data_gen(input_file)
    freq_set = defaultdict(int)
    run_apriori(data_iterator, min_support, min_confidence)
    print(f"Execution time: {time.time() - start_time:.2f} seconds")