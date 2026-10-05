
def generate_subsets(pattern, subset1, subset2, length, temp, base):
    if length < 1:
        if subset1.count(temp) == 0:
            temp.sort()
            pattern.sort()
            subset1.append(temp)
            subset2.append(pattern)
    else:
        for i in range(base, len(pattern)):
            generate_subsets(pattern[0:i] + pattern[i+1:], subset1, subset2, length-1, temp + [pattern[i]], i)
def form_association_rules(frequent_itemsets, dataset_size, min_confidence, min_lift):
    association_rules = []
    num_frequent_itemsets = len(frequent_itemsets)
    frequency_dict = {}
    for i in range(num_frequent_itemsets):
        itemset = frequent_itemsets[i][0:-1]
        itemset.sort()
        frequency_dict[tuple(itemset)] = frequent_itemsets[i][-1]
    for i in range(num_frequent_itemsets):
        pattern_length = int((len(frequent_itemsets[i]) - 1) / 2)
        pattern = frequent_itemsets[i][0:-1]
        support = frequent_itemsets[i][-1]
        subset1 = []
        subset2 = []
        for j in range(1, pattern_length + 1):
            generate_subsets(pattern, subset1, subset2, j, [], 0)
        for j in range(len(subset1)):
            if subset1.count(subset2[j]) != 0:
                subset1[j] = [-1, -9]
                subset2[j] = [-2, -5]
            pattern2 = subset1[j]
            pattern3 = subset2[j]
            pattern2.sort()
            pattern3.sort()
            if tuple(pattern2) in frequency_dict and tuple(pattern3) in frequency_dict:
                support2 = frequency_dict[tuple(pattern2)]
                support3 = frequency_dict[tuple(pattern3)]
                if support * dataset_size / (support2 * support3) > min_lift:
                    if support / support2 > min_confidence:
                        new_rule = [pattern2, pattern3, support, support / support2, support * dataset_size / (support2 * support3)]
                        association_rules.append(new_rule)
                    if support / support3 > min_confidence:
                        new_rule = [pattern3, pattern2, support, support / support3, support * dataset_size / (support2 * support3)]
                        association_rules.append(new_rule)
    return association_rules