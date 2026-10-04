def create_candidate_set(data):
    candidates = set()
    for row in data:
        for item in row:
            candidates.add(frozenset([item]))
    return sorted(candidates)
def scan_data(data, candidate_set, min_support):
    subset_count = defaultdict(int)
    for transaction in data:
        for candidate in candidate_set:
            if candidate.issubset(transaction):
                subset_count[candidate] += 1
    valid = [key for key, count in subset_count.items() if count >= min_support]
    return valid, subset_count
def generate_apriori(freq_sets, k):
    candidates = []
    len_freq_sets = len(freq_sets)
    for i in range(len_freq_sets):
        for j in range(i + 1, len_freq_sets):
            lst_cands1, lst_cands2 = list(freq_sets[i])[:k-2], list(freq_sets[j])[:k-2]
            if sorted(lst_cands1) == sorted(lst_cands2):
                candidates.append(freq_sets[i] | freq_sets[j])
    return candidates
def apriori(data, min_support):
    candidate_set = create_candidate_set(data)
    set_data = list(map(set, data))
    lst_cands, subset_counts = scan_data(set_data, candidate_set, min_support)
    frequent_itemsets = [lst_cands]
    k = 2
    while len(frequent_itemsets[k-2]) > 0:
        candidate_set_k = generate_apriori(frequent_itemsets[k-2], k)
        lst_cands_k, subset_counts_k = scan_data(set_data, candidate_set_k, min_support)
        subset_counts.update(subset_counts_k)
        frequent_itemsets.append(lst_cands_k)
        k += 1
    return frequent_itemsets, subset_counts
def main():
    data = []
    data_set_filename = 'Dataset-apriori.txt'
    with open(data_set_filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    min_support = int(input("What min. support do you want to use? "))
    print(f"\n**** Apriori with minSupport = {min_support} ****")
    frequent_itemsets, support_counts = apriori(data, min_support)
    print("\nFrequent Itemsets:\n")
    for itemset_level in frequent_itemsets:
        for itemset in itemset_level:
            print(itemset)
    print("\nSupport Counts:\n")
    for itemset, count in support_counts.items():
        print(itemset, count)
if __name__ == "__main__":
    main()