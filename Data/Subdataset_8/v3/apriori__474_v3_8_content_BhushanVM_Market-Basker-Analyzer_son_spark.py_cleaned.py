from pyspark import SparkContext
import sys
sc = SparkContext(appName="Market_Basker_Analyzer")
support_ratio = 0.3
def extract_items(transaction):
    return transaction.split()
def generate_candidates(itemset, k):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            union_set = set(itemset[i]).union(itemset[j])
            if len(union_set) == k and union_set not in candidates:
                candidates.append(union_set)
    return candidates
def count_support(transactions, candidate):
    count = 0
    for transaction in transactions:
        if candidate.issubset(set(transaction)):
            count += 1
    return count
def filter_frequent(itemsets, support):
    frequent_itemsets = []
    for itemset, count in itemsets:
        if count >= support:
            frequent_itemsets.append(itemset)
    return frequent_itemsets
def son_algorithm(transactions, support):
    candidates = []
    for transaction in transactions:
        for item in transaction:
            if [item] not in candidates:
                candidates.append([item])
    candidates.sort()
    k = 2
    while True:
        candidate_sets = generate_candidates(candidates, k)
        candidate_counts = [(candidate, count_support(transactions, set(candidate))) for candidate in candidate_sets]
        frequent_candidates = filter_frequent(candidate_counts, support)
        if not frequent_candidates:
            break
        candidates = frequent_candidates
        k += 1
    return candidates
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    input_rdd = sc.textFile(input_file)
    transactions_rdd = input_rdd.map(extract_items)
    frequent_itemsets = transactions_rdd.mapPartitions(lambda x: son_algorithm(list(x), support_ratio * x.getNumPartitions()))
    frequent_itemsets_collected = frequent_itemsets.collect()
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets_collected:
        print(itemset)
if __name__ == "__main__":
    main()