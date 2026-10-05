def read_dataset(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        id_hold = {}
        for line in lines:
            parts = line.strip().split(',')
            id_hold.setdefault(parts[0], []).append(parts[1])
    return list(id_hold.values())
def find_candidates(dataset):
    freq_sets = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in freq_sets:
                freq_sets.append([item])
    freq_sets.sort()
    return map(frozenset, freq_sets)
def find_frequent_itemsets(dataset, candidates, min_support):
    item_count = {}
    num_transactions = len(dataset)
    for transaction in dataset:
        for candidate in candidates:
            if candidate.issubset(transaction):
                item_count[candidate] = item_count.get(candidate, 0) + 1
    freq_sets = []
    support_data = {}
    for itemset, count in item_count.items():
        support = count / num_transactions
        if support >= min_support:
            freq_sets.insert(0, itemset)
        support_data[itemset] = support
    return freq_sets, support_data
def generate_joint_sets(freq_sets, k):
    joint_sets = []
    len_lk = len(freq_sets)
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            l1 = list(freq_sets[i])[:k - 2]
            l2 = list(freq_sets[j])[:k - 2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                joint_sets.append(freq_sets[i] | freq_sets[j])
    return joint_sets
def apriori(dataset, min_support=0.05):
    candidates = list(find_candidates(dataset))
    freq_sets = [candidates]
    support_data = {}
    k = 2
    while len(freq_sets[k - 2]) > 0:
        candidates = generate_joint_sets(freq_sets[k - 2], k)
        freq, support = find_frequent_itemsets(dataset, candidates, min_support)
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