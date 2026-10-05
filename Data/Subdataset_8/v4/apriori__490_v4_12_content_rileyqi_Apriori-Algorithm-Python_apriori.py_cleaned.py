import sys
import csv
from collections import defaultdict
from optparse import OptionParser
def has_infrequent_subset(candidate, frequent_itemsets):
    for item in candidate:
        k_1_set = candidate - frozenset([item])
        if k_1_set not in frequent_itemsets:
            return True
    return False
def generate_candidate_itemsets(Lk_1, k):
    Ck = []
    for i in range(len(Lk_1)):
        for j in range(i + 1, len(Lk_1)):
            c = Lk_1[i].union(Lk_1[j])
            if len(c) == k and not has_infrequent_subset(c, Lk_1):
                Ck.append(c)
    return Ck
def find_frequent_1_itemsets(database, min_support):
    S = [set(row) for row in database]
    item_count = defaultdict(int)
    for row in S:
        for item in row:
            item_count[item] += 1
    length = len(database)
    L = []
    for key, value in item_count.items():
        if float(value) / length >= min_support:
            L.append(frozenset([key]))
    return L
def apriori(database, min_support):
    D = list(database)
    S = [frozenset(row) for row in D]
    L = [frozenset()]
    L.append(find_frequent_1_itemsets(D, min_support))
    k = 2
    C = [frozenset(), frozenset()]
    number_of_transactions = len(S)
    while len(L[k - 1]) != 0:
        C.append(generate_candidate_itemsets(L[k - 1], k))
        c_count = defaultdict(int)
        for c in C[k]:
            for s in S:
                if c.issubset(s):
                    c_count[c] += 1
        I = []
        for key, value in c_count.items():
            if float(value) / number_of_transactions >= min_support:
                I.append(key)
        L.append(frozenset(I))
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
    infile = open(options.input, 'r')
    min_sup = options.minS
    csv_infile = csv.reader(infile)
    frequent_itemsets = apriori(csv_infile, min_sup)
    print(frequent_itemsets)
if __name__ == '__main__':
    main()