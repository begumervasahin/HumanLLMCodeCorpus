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
def find_freq(dataset, candidates, min_support):
    item_count = defaultdict(int)
    num_transactions = len(dataset)
    for transaction in dataset:
        for candidate in candidates:
            if candidate.issubset(transaction):
                item_count[candidate] += 1
    freq_sets = []
    support_data = {}
    for itemset, count in item_count.items():
        support = count / num_transactions
        if support >= min_support:
            freq_sets.append(itemset)
        support_data[itemset] = support
    return freq_sets, support_data
def joint_set(freq_sets, k):
    joint_freq = []
    len_lk = len(freq_sets)
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            l1 = list(freq_sets[i])[:k - 2]
            l2 = list(freq_sets[j])[:k - 2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                joint_freq.append(freq_sets[i] | freq_sets[j])
    return joint_freq
def apriori(dataset, min_support=0.05):
    candidates = find_candidates(dataset)
    freq_sets = [candidates]
    support_data = {}
    k = 2
    while len(freq_sets[k - 2]) > 0:
        candidates = joint_set(freq_sets[k - 2], k)
        freq, support = find_freq(dataset, candidates, min_support)
        support_data.update(support)
        freq_sets.append(freq)
        k += 1
    return freq_sets, support_data
def generate_rules(freq_sets, support_data, min_confidence=0.9):
    rules = []
    for i in range(1, len(freq_sets)):
        for freq_set in freq_sets[i]:
            h1 = [frozenset([item]) for item in freq_set]
            if i > 1:
                pass
            else:
                pass
    return rules
dataset = read_dataset("10000_dataset.txt")
freq_sets, support_data = apriori(dataset, 0.5)
rules = generate_rules(freq_sets, support_data)