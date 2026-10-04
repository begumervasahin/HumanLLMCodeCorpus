import re
from collections import defaultdict
from operator import itemgetter
import itertools
def calculate_mis_ordered_items(MIS):
    return sorted(MIS.items(), key=itemgetter(1))
def initialize_pass(M, MIS, support_count):
    L = []
    min_mis_required = None
    for item, mis_val in M:
        if support_count[item] >= MIS[item] and min_mis_required is None:
            L.append(item)
            min_mis_required = MIS[item]
        elif min_mis_required is not None and support_count[item] >= min_mis_required:
            L.append(item)
    return L
def filter_itemsets_by_cannot_be_together(F, cannot_be_together):
    filtered_F = []
    for k_itemsets in F:
        filtered_itemsets = [itemset for itemset in k_itemsets
                             if not any(set(cannot_set).issubset(itemset) for cannot_set in cannot_be_together)]
        filtered_F.append(filtered_itemsets)
    return filtered_F
def filter_itemsets_by_must_have(F, must_have):
    filtered_F = []
    for k_itemsets in F:
        filtered_itemsets = [itemset for itemset in k_itemsets if any(item in itemset for item in must_have)]
        filtered_F.append(filtered_itemsets)
    return filtered_F
def parse_parameters(parameter_file):
    MIS = {}
    cannot_be_together = []
    must_have = []
    SDC = None
    with open(parameter_file, 'r') as file:
        for line in file:
            if "MIS" in line:
                item, mis = re.findall(r'\d+', line)
                MIS[int(item)] = float(mis) / 100
            elif "SDC" in line:
                SDC = float(re.findall(r'\d+', line)[0]) / 100
            elif "cannot_be_together" in line:
                groups = re.findall(r'\{(.*?)\}', line)
                for group in groups:
                    cannot_be_together.append(list(map(int, group.split(','))))
            elif "must-have" in line:
                must_have = list(map(int, re.findall(r'\d+', line)))
    return MIS, SDC, cannot_be_together, must_have
def parse_transaction_data(transaction_file):
    transactions = []
    with open(transaction_file, 'r') as file:
        for line in file:
            transactions.append(list(map(int, re.findall(r'\d+', line))))
    return transactions
def ms_apriori(transactions, MIS, cannot_be_together, must_have, min_sup):
    support_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            support_count[item] += 1
    M = calculate_mis_ordered_items(MIS)
    L = initialize_pass(M, MIS, support_count)
    F = []
    k = 1
    Ck = [frozenset([item]) for item in L]
    while Ck:
        Fk = [c for c in Ck if support_count[c] >= min_sup]
        F.append(Fk)
        Ck = [frozenset(x) for x in itertools.combinations(L, k + 1)]
        k += 1
    F = filter_itemsets_by_cannot_be_together(F, cannot_be_together)
    F = filter_itemsets_by_must_have(F, must_have)
    return F
def print_frequent_itemsets(F, support_count):
    for i, itemsets in enumerate(F):
        if itemsets:
            print(f"Frequent {i+1}-itemsets")
            for itemset in itemsets:
                print(f"    {support_count[itemset]} : {set(itemset)}")
            print(f"    Total number of frequent {i+1}-itemsets = {len(itemsets)}\n")
if __name__ == "__main__":
    parameter_file = "parameters.txt"
    transaction_file = "transactions.txt"
    MIS, SDC, cannot_be_together, must_have = parse_parameters(parameter_file)
    transactions = parse_transaction_data(transaction_file)
    min_sup = 2
    F = ms_apriori(transactions, MIS, cannot_be_together, must_have, min_sup)
    support_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            support_count[frozenset([item])] += 1
    print_frequent_itemsets(F, support_count)