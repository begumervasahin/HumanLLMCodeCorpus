from collections import defaultdict
def read_dataset(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        dataset = [line.strip().split(',') for line in lines]
    return dataset
def find_candidates(dataset):
    candidates = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in candidates:
                candidates.append([item])
    return list(map(frozenset, candidates))
def find_frequent_itemsets(dataset, candidates, min_support):
    item_count = defaultdict(int)
    num_transactions = len(dataset)
    for transaction in dataset:
        for candidate in candidates:
            if candidate.issubset(transaction):
                item_count[candidate] += 1
    frequent_itemsets = []
    support_data = {}
    for itemset, count in item_count.items():
        support = count / num_transactions
        if support >= min_support:
            frequent_itemsets.append(itemset)
        support_data[itemset] = support
    return frequent_itemsets, support_data
def generate_joint_sets(frequent_itemsets, k):
    joint_sets = []
    num_frequent_itemsets = len(frequent_itemsets)
    for i in range(num_frequent_itemsets):
        for j in range(i + 1, num_frequent_itemsets):
            l1 = list(frequent_itemsets[i])[:k - 2]
            l2 = list(frequent_itemsets[j])[:k - 2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                joint_sets.append(frequent_itemsets[i] | frequent_itemsets[j])
    return joint_sets
def apriori(dataset, min_support=0.05):
    candidates = find_candidates(dataset)
    frequent_itemsets = [candidates]
    support_data = {}
    k = 2
    while len(frequent_itemsets[k - 2]) > 0:
        candidates = generate_joint_sets(frequent_itemsets[k - 2], k)
        frequent_sets, support = find_frequent_itemsets(dataset, candidates, min_support)
        support_data.update(support)
        frequent_itemsets.append(frequent_sets)
        k += 1
    return frequent_itemsets, support_data
def generate_association_rules(frequent_itemsets, support_data, min_confidence=0.9):
    association_rules = []
    for i in range(1, len(frequent_itemsets)):
        for frequent_set in frequent_itemsets[i]:
            h1 = [frozenset([item]) for item in frequent_set]
            if i > 1:
                pass
            else:
                pass
    return association_rules
dataset = read_dataset("10000_dataset.txt")
frequent_itemsets, support_data = apriori(dataset, 0.5)
association_rules = generate_association_rules(frequent_itemsets, support_data)