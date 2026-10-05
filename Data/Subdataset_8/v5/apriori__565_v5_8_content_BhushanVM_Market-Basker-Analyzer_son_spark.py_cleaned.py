from pyspark import SparkContext
from itertools import combinations
import sys
sc = SparkContext(appName="Market_Basker_Analyzer")
SUPPORT_RATIO = 0.3
def find_candidates(inp, length):
    candidates = []
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            union_set = set(inp[i]).union(set(inp[j]))
            if len(union_set) == length:
                if tuple(union_set) not in candidates:
                    candidates.append(tuple(union_set))
    return candidates
def partition_apriori(x):
    transactions = list(x)
    output_list = []
    support = SUPPORT_RATIO * len(transactions)
    max_transaction_length = 0
    items = set()
    for transaction in transactions:
        items = items.union(set(transaction))
        if max_transaction_length < len(transaction):
            max_transaction_length = len(transaction)
    items = list(items)
    for item in items:
        count = sum(1 for transaction in transactions if item in set(transaction))
        if count >= support:
            output_list.append(item)
    temp_list = []
    item_pairs = list(combinations(items, 2))
    for pair in item_pairs:
        count = sum(1 for transaction in transactions if set(pair) in set(combinations(transaction, 2)))
        if count >= support:
            output_list.append(pair)
            temp_list.append(pair)
    candidate_items = temp_list
    temp_list = []
    length = 3
    while length <= max_transaction_length and len(candidate_items) > 1:
        candidate_items = find_candidates(candidate_items, length)
        temp_list = []
        for candidate in candidate_items:
            count = sum(1 for transaction in transactions if set(candidate) in set(combinations(transaction, length)))
            if count >= support:
                temp_list.append(candidate)
                output_list.append(candidate)
        length += 1
        candidate_items = temp_list
    return output_list
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    input_rdd = sc.textFile(input_file, 2)
    output_rdd = input_rdd.map(lambda x: x.split("\n"))
    frequent_itemsets_rdd = output_rdd.mapPartition(partition_apriori)
    print(output_rdd.collect())
    print(output_rdd.getNumPartitions())
if __name__ == "__main__":
    main()