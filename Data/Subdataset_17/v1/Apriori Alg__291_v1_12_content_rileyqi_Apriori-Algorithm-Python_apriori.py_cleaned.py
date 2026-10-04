import sys
from collections import defaultdict
from optparse import OptionParser
import csv
def has_infreq_subset(c, Lk_1):
    for item in c:
        k_1_set = c - frozenset([item])
        if (k_1_set not in Lk_1):
            return True
    return False
def apriori_gen(Lk_1, k):
    Ck = []
    for i in Lk_1:
        for j in Lk_1:
            c = i.union(j)
            if len(c) == k and not has_infreq_subset(c, Lk_1):
                Ck.append(c)
    remove_duplicate = set(Ck)
    return list(remove_duplicate)
def find_freq_1_itemsets(D, min_sup):
    S = [set(row) for row in D]
    item_count = defaultdict(int)
    for row in S:
        for item in row:
            item_count[item] += 1
    length = len(D)
    L = [frozenset([key]) for key, value in item_count.items() if float(value) / length >= min_sup]
    return L
def apriori(database, min_sup):
    D = [row for row in database]
    S = [frozenset(row) for row in D]
    L = [frozenset()]
    L.append(find_freq_1_itemsets(D, min_sup))
    k = 2
    C = [frozenset()] * 2
    number_of_transaction = len(S)
    while len(L[k-1]) != 0:
        C.append(apriori_gen(L[k-1], k))
        c_count = defaultdict(int)
        for c in C[k]:
            for s in S:
                if c.issubset(s):
                    c_count[c] += 1
        Lk = [key for key, value in c_count.items() if float(value) / number_of_transaction >= min_sup]
        L.append(frozenset(Lk))
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
    if options.input is None:
        print("Please specify an input file using the -f option.")
        sys.exit(1)
    min_sup = options.minS
    with open(options.input, 'r') as infile:
        csv_infile = csv.reader(infile)
        L = apriori(csv_infile, min_sup)
        for i, level in enumerate(L):
            print(f"Frequent itemsets of size {i}:")
            for itemset in level:
                print(itemset)
if __name__ == '__main__':
    main()