from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
sc = SparkContext(appName="Market-Basket-Analyzer")
support_ratio = 0.3
def fx(x):
    return list(x[0])
def find_candidates(input_list, length):
    candidates = []
    input_len = len(input_list)
    for i in range(input_len):
        for j in range(i + 1, input_len):
            combined_set = set(input_list[i]).union(set(input_list[j]))
            if len(combined_set) == length:
                candidate_tuple = tuple(combined_set)
                if candidate_tuple not in candidates:
                    candidates.append(candidate_tuple)
    return candidates
def partition_apriori(iterator):
    transactions = list(iterator)
    support = support_ratio * len(transactions)
    item_count = defaultdict(int)
    output_list = []
    all_items = set()
    for transaction in transactions:
        for item in transaction:
            all_items.add(item)
            item_count[item] += 1
    frequent_items = {item for item, count in item_count.items() if count >= support}
    output_list.extend(frequent_items)
    length = 2
    while frequent_items:
        candidates = find_candidates(list(frequent_items), length)
        candidate_count = defaultdict(int)
        for candidate in candidates:
            for transaction in transactions:
                if set(candidate).issubset(transaction):
                    candidate_count[candidate] += 1
        frequent_items = {candidate for candidate, count in candidate_count.items() if count >= support}
        output_list.extend(frequent_items)
        length += 1
    return output_list
def main():
    input_rdd = sc.textFile(sys.argv[1], 2)
    transactions_rdd = input_rdd.map(lambda x: x.split("\n"))
    candidate_itemsets = transactions_rdd.mapPartitions(partition_apriori)
    result = candidate_itemsets.collect()
    print(result)
    print(f"Number of partitions: {transactions_rdd.getNumPartitions()}")
if __name__ == "__main__":
    main()