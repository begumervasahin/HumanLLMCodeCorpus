def create_candidate_set(data):
    candidates = []
    for row in data:
        for item in row:
            if [item] not in candidates:
                candidates.append([item])
    candidates.sort()
    return list(map(frozenset, candidates))
def scan_data(data, candidate_set, min_support):
    subset_count = {}
    for cur_set in data:
        for candidate in candidate_set:
            if candidate.issubset(cur_set):
                if candidate not in subset_count:
                    subset_count[candidate] = 1
                else:
                    subset_count[candidate] += 1
    n = float(len(data))
    valid = []
    for key, count in subset_count.items():
        if count >= min_support:
            valid.insert(0, key)
    return valid, subset_count
def generate_apriori(freq_sets, k):
    valid = []
    n_freq_sets = len(freq_sets)
    for i in range(n_freq_sets):
        for j in range(i + 1, n_freq_sets):
            lst_cands1 = list(freq_sets[i])[:k-2]
            lst_cands2 = list(freq_sets[j])[:k-2]
            lst_cands1.sort()
            lst_cands2.sort()
            if lst_cands1 == lst_cands2:
                valid.append(freq_sets[i] | freq_sets[j])
    return valid
def apriori(data, min_support):
    candidate_set = create_candidate_set(data)
    set_data = list(map(set, data))
    lst_cands, subset_counts = scan_data(set_data, candidate_set, min_support)
    lst_cands = [lst_cands]
    k = 2
    while len(lst_cands[k-2]) > 0:
        candidate_set_x = generate_apriori(lst_cands[k-2], k)
        lst_cands_x, subset_counts_x = scan_data(set_data, candidate_set_x, min_support)
        subset_counts.update(subset_counts_x)
        lst_cands.append(candidate_set_x)
        k += 1
    return lst_cands, subset_counts
def main():
    data = []
    data_set_filename = 'Dataset-apriori.txt'
    with open(data_set_filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    min_support = int(input("What min. support do you want to use? "))
    print(f"\n**** Apriori with minSupport = {min_support} ****")
    sets, counts = apriori(data, min_support)
    print("\nSets:\n")
    for item_set in sets:
        for item in item_set:
            print(item)
    print("\nCounts:\n")
    for item_set, count in counts.items():
        print(item_set, count)
if __name__ == "__main__":
    main()