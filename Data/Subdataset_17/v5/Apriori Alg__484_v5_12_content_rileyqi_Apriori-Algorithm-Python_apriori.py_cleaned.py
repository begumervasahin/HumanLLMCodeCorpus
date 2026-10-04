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
def apriori_gen(previous_level_itemsets, k):
    candidate_itemsets = []
    for itemset1 in previous_level_itemsets:
        for itemset2 in previous_level_itemsets:
            candidate = itemset1.union(itemset2)
            if len(candidate) == k and not has_infrequent_subset(candidate, previous_level_itemsets):
                candidate_itemsets.append(candidate)
    return list(set(candidate_itemsets))
def find_frequent_1_itemsets(database, min_support):
    item_count = defaultdict(int)
    for transaction in database:
        for item in transaction:
            item_count[item] += 1
    num_transactions = len(database)
    frequent_1_itemsets = [
        frozenset([item])
        for item, count in item_count.items()
        if float(count) / num_transactions >= min_support
    ]
    return frequent_1_itemsets
def apriori(database, min_support):
    database = [frozenset(transaction) for transaction in database]
    L = [None, find_frequent_1_itemsets(database, min_support)]
    k = 2
    while L[k-1]:
        candidate_itemsets = apriori_gen(L[k-1], k)
        itemset_counts = defaultdict(int)
        for transaction in database:
            for candidate in candidate_itemsets:
                if candidate.issubset(transaction):
                    itemset_counts[candidate] += 1
        num_transactions = len(database)
        L.append([
            itemset
            for itemset, count in itemset_counts.items()
            if float(count) / num_transactions >= min_support
        ])
        k += 1
    return L
def main():
    opt_parser = OptionParser()
    opt_parser.add_option('-f', '--inputFile', dest='input', help='filename containing CSV', default=None)
    opt_parser.add_option('-s', '--minSupport', dest='min_support', help='minimum support value', default=0.15, type='float')
    options, _ = opt_parser.parse_args()
    if not options.input:
        print("Please provide an input file using the -f option.")
        sys.exit(1)
    with open(options.input, 'r') as infile:
        csv_reader = csv.reader(infile)
        database = list(csv_reader)
    min_support = options.min_support
    frequent_itemsets = apriori(database, min_support)
    for level in frequent_itemsets:
        if level:
            for itemset in level:
                print(itemset)
if __name__ == '__main__':
    main()