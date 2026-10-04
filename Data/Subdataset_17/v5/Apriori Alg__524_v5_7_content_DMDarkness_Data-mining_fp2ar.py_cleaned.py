
def get_subsets(pattern, subsets1, subsets2, length, temp, base):
    if length < 1:
        if temp not in subsets1:
            temp.sort()
            pattern.sort()
            subsets1.append(temp)
            subsets2.append(pattern)
    else:
        for i in range(base, len(pattern)):
            new_temp = temp + [pattern[i]]
            new_pattern = pattern[:i] + pattern[i+1:]
            get_subsets(new_pattern, subsets1, subsets2, length - 1, new_temp, i)
def generate_association_rules(frequent_itemsets, total_transactions, min_confidence, min_lift):
    rules = []
    fi_dict = {}
    for itemset in frequent_itemsets:
        items = itemset[:-1]
        items.sort()
        fi_dict[tuple(items)] = itemset[-1]
    for itemset in frequent_itemsets:
        pattern = itemset[:-1]
        support_pattern = itemset[-1]
        subsets1, subsets2 = [], []
        for length in range(1, len(pattern)):
            get_subsets(pattern, subsets1, subsets2, length, [], 0)
        for subset1, subset2 in zip(subsets1, subsets2):
            subset1.sort()
            subset2.sort()
            if tuple(subset1) in fi_dict and tuple(subset2) in fi_dict:
                support_subset1 = fi_dict[tuple(subset1)]
                support_subset2 = fi_dict[tuple(subset2)]
                lift = support_pattern * total_transactions / (support_subset1 * support_subset2)
                if lift >= min_lift:
                    confidence1 = support_pattern / support_subset1
                    if confidence1 >= min_confidence:
                        rules.append([subset1, subset2, support_pattern, confidence1, lift])
                    confidence2 = support_pattern / support_subset2
                    if confidence2 >= min_confidence:
                        rules.append([subset2, subset1, support_pattern, confidence2, lift])
    return rules