from pyspark import SparkContext
from collections import defaultdict
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
    support_threshold = support_ratio * len(transactions)
    single_items = set()
    max_transaction_length = 0
    for transaction in transactions:
        single_items.update(transaction)
        max_transaction_length = max(max_transaction_length, len(transaction))
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1
    frequent_itemsets = [
        item for item, count in item_counts.items() if count >= support_threshold
    ]
    current_length = 2
    current_frequent_itemsets = frequent_itemsets
    while current_length <= max_transaction_length and current_frequent_itemsets:
        candidates = find_candidates(current_frequent_itemsets, current_length)
        candidate_counts = defaultdict(int)
        for candidate in candidates:
            for transaction in transactions:
                if set(candidate).issubset(transaction):
                    candidate_counts[candidate] += 1
        current_frequent_itemsets = [
            candidate for candidate, count in candidate_counts.items() if count >= support_threshold
        ]
        frequent_itemsets.extend(current_frequent_itemsets)
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