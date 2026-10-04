from pyspark import SparkContext
from collections import defaultdict
from operator import add
from itertools import combinations
import sys
sc = SparkContext(appName="Market-Basket-Analyzer")
support_ratio = 0.3
def find_candidates(itemsets, length):
    candidates = []
    for i in range(len(itemsets)):
        for j in range(i + 1, len(itemsets)):
            union_set = set(itemsets[i]).union(set(itemsets[j]))
            if len(union_set) == length and tuple(union_set) not in candidates:
                candidates.append(tuple(union_set))
    return candidates
def partition_apriori(partition):
    transactions = list(partition)
    frequent_itemsets = []
    support_threshold = support_ratio * len(transactions)
    stop_length = 0
    single_items = []
    for transaction in transactions:
        single_items = list(set(single_items).union(set(transaction)))
        stop_length = max(stop_length, len(transaction))
    for item in single_items:
        count = sum(1 for transaction in transactions if item in transaction)
        if count >= support_threshold:
            frequent_itemsets.append(item)
    candidates = list(combinations(single_items, 2))
    temp_frequent_pairs = []
    for candidate in candidates:
        count = sum(1 for transaction in transactions if set(candidate).issubset(set(transaction)))
        if count >= support_threshold:
            frequent_itemsets.append(candidate)
            temp_frequent_pairs.append(candidate)
    current_length = 3
    while current_length <= stop_length and len(temp_frequent_pairs) > 1:
        candidates = find_candidates(temp_frequent_pairs, current_length)
        temp_frequent_pairs = []
        for candidate in candidates:
            count = sum(1 for transaction in transactions if set(candidate).issubset(set(transaction)))
            if count >= support_threshold:
                frequent_itemsets.append(candidate)
                temp_frequent_pairs.append(candidate)
        current_length += 1
    return frequent_itemsets
def main():
    input_file = sys.argv[1]
    transactions_rdd = sc.textFile(input_file, 2).map(lambda x: x.split(",")).mapPartitions(partition_apriori)
    results = transactions_rdd.collect()
    print("Frequent itemsets:", results)
    print("Number of partitions:", transactions_rdd.getNumPartitions())
if __name__ == "__main__":
    main()