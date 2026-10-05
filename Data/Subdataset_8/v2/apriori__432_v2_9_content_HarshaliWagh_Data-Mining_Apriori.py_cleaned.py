from collections import defaultdict
def generate_candidates(freq_itemset, count):
    combinations = []
    items = list(freq_itemset.keys())
    for i in range(len(freq_itemset) - 1):
        for j in range(i + 1, len(freq_itemset)):
            combination = [items[i], items[j]]
            combinations.append(combination)
    candidates = [comb.split(',') for comb in [','.join(comb) for comb in combinations]]
    duplicate_candidates = []
    pruned_candidates = []
    for i in range(len(candidates)):
        unique_set = set(candidates[i])
        unique_list = list(unique_set)
        duplicate_candidates.append(unique_list)
        if len(duplicate_candidates[i]) == count:
            pruned_candidates.append(duplicate_candidates[i])
    return pruned_candidates
def calculate_support(candidates, data):
    support_list = []
    candidate_sets = [set(candidates[p]) for p in range(len(candidates))]
    data_sets = [set(data[q]) for q in range(len(data))]
    for i in range(len(candidates)):
        counter = sum(1 for j in range(len(data)) if candidate_sets[i].issubset(data_sets[j]))
        support_list.append(counter)
    return support_list
def extract_frequent_itemsets(candidate_set, support, min_support):
    frequent_itemsets = {}
    for i in range(len(candidate_set)):
        itemset = candidate_set[i]
        itemset_string = ','.join(itemset)
        if support[i] >= min_support:
            frequent_itemsets[itemset_string] = support[i]
    return frequent_itemsets
def generate_freq_list(frequent_itemsets, count):
    n = count - 1
    freq_new = [x.split(',') for x in frequent_itemsets]
    while n != 0:
        for i in range(len(freq_new)):
            glue = []
            associations = generate_associations(freq_new[i], glue, n)
            for j in range(len(associations)):
                dumpy = [freq_new[i][k] for k in range(len(freq_new[i])) if freq_new[j][k] not in associations[j]]
                print(str(dumpy) + "--------->" + str(associations[j]))
        n = n - 1
def generate_associations(frequent_itemset, glue, n):
    if len(frequent_itemset) == n:
        if glue.count(frequent_itemset) == 0:
            glue.append(frequent_itemset)
        return glue
    elif len(frequent_itemset) != n:
        for i in range(len(frequent_itemset)):
            next_frequent_itemset = frequent_itemset[i+1:] + frequent_itemset[:i]
            glue = generate_associations(next_frequent_itemset, glue, n)
        return glue
def main():
    dataset = []
    print("Select the dataset:")
    print("1. Grocery")
    print("2. Clothing")
    print("3. Electronics")
    print("4. Utensils")
    print("5. Furniture")
    dataset_number = input("Enter the dataset number: ")
    min_support = int(input('Enter minimum Support: '))
    min_confidence = int(input('Enter minimum Confidence: '))
    dataset_file = ""
    if dataset_number == '1':
        dataset_file = "db1.txt"
    elif dataset_number == '2':
        dataset_file = "db2.txt"
    elif dataset_number == '3':
        dataset_file = "db3.txt"
    elif dataset_number == '4':
        dataset_file = "db4.txt"
    else:
        dataset_file = "db5.txt"
    with open(dataset_file, 'r') as fp:
        dataset = [line.strip().split(", ") for line in fp]
    item_dict = defaultdict(int)
    for data_row in dataset:
        for item in data_row:
            item_dict[item] += 1
    frequent_itemsets_1 = {item: count for item, count in item_dict.items() if count >= min_support}
    count = 2
    candidate_set_2 = generate_candidates(frequent_itemsets_1, count)
    support_2 = calculate_support(candidate_set_2, dataset)
    frequent_itemsets_2 = extract_frequent_itemsets(candidate_set_2, support_2, min_support)
    generate_freq_list(frequent_itemsets_2, count)
if __name__ == "__main__":
    main()