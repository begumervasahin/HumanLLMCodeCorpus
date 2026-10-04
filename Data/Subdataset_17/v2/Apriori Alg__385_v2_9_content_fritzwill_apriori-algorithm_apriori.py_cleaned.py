def create_candidate_set(data):
    candidates = []
    for transaction in data:
        for item in transaction:
            if [item] not in candidates:
                candidates.append([item])
    candidates.sort()
    return list(map(frozenset, candidates))
def scan_data(data, candidate_set, min_support):
    subset_count = {}
    for transaction in data:
        for candidate in candidate_set:
            if candidate.issubset(transaction):
                if candidate not in subset_count:
                    subset_count[candidate] = 1
                else:
                    subset_count[candidate] += 1
    num_transactions = float(len(data))
    frequent_itemsets = []
    for itemset, count in subset_count.items():
        if count >= min_support:
            frequent_itemsets.append(itemset)
    return frequent_itemsets, subset_count
def generate_candidate_itemsets(frequent_itemsets, k):
    candidates = []
    num_itemsets = len(frequent_itemsets)
    for i in range(num_itemsets):
        for j in range(i + 1, num_itemsets):
            itemset1 = list(frequent_itemsets[i])[:k - 2]
            itemset2 = list(frequent_itemsets[j])[:k - 2]
            itemset1.sort()
            itemset2.sort()
            if itemset1 == itemset2:
                candidates.append(frequent_itemsets[i] | frequent_itemsets[j])
    return candidates
def apriori(data, min_support):
    candidate_set = create_candidate_set(data)
    transaction_list = list(map(set, data))
    frequent_itemsets, itemset_counts = scan_data(transaction_list, candidate_set, min_support)
    all_frequent_itemsets = [frequent_itemsets]
    k = 2
    while len(all_frequent_itemsets[k - 2]) > 0:
        candidate_set = generate_candidate_itemsets(all_frequent_itemsets[k - 2], k)
        frequent_itemsets, new_counts = scan_data(transaction_list, candidate_set, min_support)
        itemset_counts.update(new_counts)
        all_frequent_itemsets.append(frequent_itemsets)
        k += 1
    return all_frequent_itemsets, itemset_counts
if __name__ == "__main__":
    data = []
    dataset_filename = 'Dataset-apriori.txt'
    with open(dataset_filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    min_support = int(input("What min. support do you want to use? "))
    print("\n**** Apriori with minSupport = {} ****".format(min_support))
    frequent_itemsets, itemset_counts = apriori(data, min_support)
    print("\nFrequent Itemsets:\n")
    for itemset_level in frequent_itemsets:
        for itemset in itemset_level:
            print(itemset)
    print("\nItemset Counts:\n")
    for itemset, count in itemset_counts.items():
        print(itemset, count)