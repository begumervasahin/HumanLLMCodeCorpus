
def get_subsets(pattern, subsets1, subsets2, length, temp, base):
    if length < 1:
        if temp not in subsets1:
            temp.sort()
            pattern.sort()
            subsets1.append(temp)
            subsets2.append(pattern)
    else:
        for i in range(base, len(pattern)):
            get_subsets(pattern[:i] + pattern[i+1:], subsets1, subsets2, length-1, temp + [pattern[i]], i)
def generate_association_rules(frequent_itemsets, total_transactions, min_confidence, min_lift):
    rules = []
    fi_dict = {}
    for itemset in frequent_itemsets:
        items = itemset[:-1]
        items.sort()
        fi_dict[tuple(items)] = itemset[-1]
    for itemset in frequent_itemsets:
        ps_len = (len(itemset) - 1)
        pattern = itemset[:-1]
        support_pattern = itemset[-1]
        subsets1, subsets2 = [], []
        for j in range(1, ps_len + 1):
            get_subsets(pattern, subsets1, subsets2, j, [], 0)
        for j in range(len(subsets1)):
            if subsets1.count(subsets2[j]) != 0:
                subsets1[j] = [-1, -9]
                subsets2[j] = [-2, -5]
            pat2 = subsets1[j]
            pat3 = subsets2[j]
            pat2.sort()
            pat3.sort()
            if tuple(pat2) in fi_dict and tuple(pat3) in fi_dict:
                support_pat2 = fi_dict[tuple(pat2)]
                support_pat3 = fi_dict[tuple(pat3)]
                lift = support_pattern * total_transactions / (support_pat2 * support_pat3)
                if lift > min_lift:
                    confidence1 = support_pattern / support_pat2
                    if confidence1 > min_confidence:
                        new_rule = [pat2, pat3, support_pattern, confidence1, lift]
                        rules.append(new_rule)
                    confidence2 = support_pattern / support_pat3
                    if confidence2 > min_confidence:
                        new_rule = [pat3, pat2, support_pattern, confidence2, lift]
                        rules.append(new_rule)
    return rules