
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
def generate_association_rules(frequent_itemsets, dataset_size, min_confidence, min_lift):
    rules = []
    num_frequent_itemsets = len(frequent_itemsets)
    frequency_dict = {}
    for i in range(num_frequent_itemsets):
        freq_pattern = frequent_itemsets[i][0:-1]
        freq_pattern.sort()
        frequency_dict[tuple(freq_pattern)] = frequent_itemsets[i][-1]
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
            pat2 = subset1[j]
            pat3 = subset2[j]
            pat2.sort()
            pat3.sort()
            if tuple(pat2) in frequency_dict and tuple(pat3) in frequency_dict:
                sup2 = frequency_dict[tuple(pat2)]
                sup3 = frequency_dict[tuple(pat3)]
                if support * dataset_size / (sup2 * sup3) > min_lift:
                    if support / sup2 > min_confidence:
                        new_rule = [pat2, pat3, support, support / sup2, support * dataset_size / (sup2 * sup3)]
                        rules.append(new_rule)
                    if support / sup3 > min_confidence:
                        new_rule = [pat3, pat2, support, support / sup3, support * dataset_size / (sup2 * sup3)]
                        rules.append(new_rule)
    return rules