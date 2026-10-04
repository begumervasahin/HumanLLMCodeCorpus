import sys
from collections import defaultdict
from optparse import OptionParser
import csv
def has_infrequent_subset(candidate, previous_level_itemsets):
    for item in candidate:
        subset = candidate - frozenset([item])
        if subset not in previous_level_itemsets:
            return True
    return False
def generate_candidate_itemsets(previous_level_itemsets, k):
    candidates = []
    for i in previous_level_itemsets:
        for j in previous_level_itemsets:
            candidate = i.union(j)
            if len(candidate) == k and not has_infrequent_subset(candidate, previous_level_itemsets):
                candidates.append(candidate)
    return list(set(candidates))
def find_frequent_1_itemsets(transactions, min_support):
    item_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_count[item] += 1
    num_transactions = len(transactions)
    return [frozenset([item]) for item, count in item_count.items() if count / num_transactions >= min_support]
def apriori(transactions, min_support):
    transactions = [frozenset(transaction) for transaction in transactions]
    frequent_itemsets = [frozenset()]
    frequent_itemsets.append(find_frequent_1_itemsets(transactions, min_support))
    k = 2
    while frequent_itemsets[k-1]:
        candidates = generate_candidate_itemsets(frequent_itemsets[k-1], k)
        candidate_count = defaultdict(int)
        for candidate in candidates:
            for transaction in transactions:
                if candidate.issubset(transaction):
                    candidate_count[candidate] += 1
        num_transactions = len(transactions)
        frequent_k_itemsets = [itemset for itemset, count in candidate_count.items() if count / num_transactions >= min_support]
        frequent_itemsets.append(frozenset(frequent_k_itemsets))
        k += 1
    return frequent_itemsets
def main():
    parser = OptionParser()
    parser.add_option(
        '-f',
        '--inputFile',
        dest='input',
        help='Filename containing CSV data',
        default=None
    )
    parser.add_option(
        '-s',
        '--minSupport',
        dest='min_support',
        help='Minimum support value',
        default=0.15,
        type='float'
    )
    (options, args) = parser.parse_args()
    if options.input is None:
        print("Please specify an input file using the -f option.")
        sys.exit(1)
    min_support = options.min_support
    with open(options.input, 'r') as infile:
        csv_reader = csv.reader(infile)
        transactions = [row for row in csv_reader]
    frequent_itemsets = apriori(transactions, min_support)
    for i, level in enumerate(frequent_itemsets):
        print(f"Frequent itemsets of size {i}:")
        for itemset in level:
            print(itemset)
if __name__ == '__main__':
    main()