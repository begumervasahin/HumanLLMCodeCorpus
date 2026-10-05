import sys
import csv
from collections import defaultdict
from optparse import OptionParser
def has_infrequent_subset(candidate, frequent_itemsets):
    for item in candidate:
        subset = candidate - frozenset([item])
        if subset not in frequent_itemsets:
            return True
    return False
def generate_candidate_itemsets(Lk_1, k):
    Ck = []
    for i in range(len(Lk_1)):
        for j in range(i + 1, len(Lk_1)):
            candidate = Lk_1[i].union(Lk_1[j])
            if len(candidate) == k and not has_infrequent_subset(candidate, Lk_1):
                Ck.append(candidate)
    return Ck
def find_frequent_1_itemsets(database, min_support):
    item_count = defaultdict(int)
    for row in database:
        for item in set(row):
            item_count[item] += 1
    num_transactions = len(database)
    frequent_itemsets = [frozenset([key]) for key, value in item_count.items()
                         if value / num_transactions >= min_support]
    return frequent_itemsets
def apriori(database, min_support):
    transactions = list(database)
    S = [frozenset(row) for row in transactions]
    L = [frozenset()]
    L.append(find_frequent_1_itemsets(transactions, min_support))
    k = 2
    C = [frozenset(), frozenset()]
    num_transactions = len(S)
    while len(L[k - 1]) != 0:
        C.append(generate_candidate_itemsets(L[k - 1], k))
        itemset_count = defaultdict(int)
        for candidate in C[k]:
            for transaction in S:
                if candidate.issubset(transaction):
                    itemset_count[candidate] += 1
        frequent_k_itemsets = [key for key, value in itemset_count.items()
                               if value / num_transactions >= min_support]
        L.append(frequent_k_itemsets)
        k += 1
    return L
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
    with open(options.input, 'r') as infile:
        min_sup = options.minS
        csv_infile = csv.reader(infile)
        frequent_itemsets = apriori(csv_infile, min_sup)
        print(frequent_itemsets)
if __name__ == '__main__':
    main()