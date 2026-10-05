from collections import defaultdict
import csv
from optparse import OptionParser
def has_infrequent_subset(candidate, frequent_itemsets):
    for item in candidate:
        subset = candidate - frozenset([item])
        if subset not in frequent_itemsets:
            return True
    return False
def generate_candidates(frequent_itemsets, k):
    candidates = []
    for i in range(len(frequent_itemsets)):
        for j in range(i + 1, len(frequent_itemsets)):
            candidate = frequent_itemsets[i].union(frequent_itemsets[j])
            if len(candidate) == k and not has_infrequent_subset(candidate, frequent_itemsets):
                candidates.append(candidate)
    return candidates
def find_frequent_1_itemsets(database, min_support):
    item_count = defaultdict(int)
    for transaction in database:
        for item in transaction:
            item_count[item] += 1
    num_transactions = len(database)
    frequent_itemsets = []
    for item, count in item_count.items():
        support = float(count) / num_transactions
        if support >= min_support:
            frequent_itemsets.append(frozenset([item]))
    return frequent_itemsets
def apriori_algorithm(database, min_support):
    transactions = list(database)
    frequent_itemsets = [frozenset()]
    frequent_itemsets.append(find_frequent_1_itemsets(transactions, min_support))
    k = 2
    candidates = [frozenset(), frozenset()]
    num_transactions = len(transactions)
    while len(frequent_itemsets[k - 1]) != 0:
        candidates.append(generate_candidates(frequent_itemsets[k - 1], k))
        itemset_count = defaultdict(int)
        for candidate in candidates[k]:
            for transaction in transactions:
                if candidate.issubset(transaction):
                    itemset_count[candidate] += 1
        frequent_k_itemsets = []
        for itemset, count in itemset_count.items():
            support = float(count) / num_transactions
            if support >= min_support:
                frequent_k_itemsets.append(itemset)
        frequent_itemsets.append(frequent_k_itemsets)
        k += 1
    return frequent_itemsets
def main():
    opt_parser = OptionParser()
    opt_parser.add_option(
        '-f',
        '--inputFile',
        dest='input',
        help='filename containing csv',
        default=None)
    opt_parser.add_option(
        '-s',
        '--minSupport',
        dest='minS',
        help='minimum support value',
        default=0.15,
        type='float')
    (options, args) = opt_parser.parse_args()
    if not options.input:
        print('Please provide an input file using -f or --inputFile option')
        return
    infile = open(options.input, 'r')
    min_support = options.minS
    csv_infile = csv.reader(infile)
    frequent_itemsets = apriori_algorithm(csv_infile, min_support)
    print(frequent_itemsets)
if __name__ == '__main__':
    main()